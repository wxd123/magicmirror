#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/management/config/configLoader.py
"""
YAML 配置加载器 - 配置文件的加载和合并模块

该模块提供 YAML 配置文件的加载功能，支持项目配置和用户配置的自动合并。
支持开发环境和打包环境，自动处理不同环境下的路径问题。

核心功能：
- 加载项目配置文件
- 加载并合并用户配置（用户配置覆盖项目配置）
- 支持嵌套路径的配置路径获取
- 支持打包环境的路径适配

使用示例:
    from magicm.management.config import ConfigLoader
    
    # 方式1：直接加载指定路径的配置
    loader = ConfigLoader()
    config = loader.load('display', 'config.yaml')
    
    # 方式2：使用模块名加载（支持用户配置合并）
    loader = ConfigLoader('display', 'config.yaml')
    config = loader.load_merged()  # 自动合并用户配置
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from platformdirs import user_config_dir


class ConfigLoader:
    """
    YAML 配置加载器 - 支持嵌套路径和配置合并
    
    该类负责从文件系统加载 YAML 配置文件，支持：
    1. 直接加载指定路径的配置文件
    2. 按模块名加载（自动定位项目配置和用户配置）
    3. 项目配置与用户配置的深度合并
    4. 开发环境和打包环境的路径自动适配
    
    配置优先级（从低到高）：
    - 项目配置：项目源码中的默认配置（只读）
    - 用户配置：用户目录中的自定义配置（可写，覆盖项目配置）
    
    Attributes:
        module_name (str): 模块名称，如 'display'
        config_filename (str): 配置文件名，如 'config.yaml'
        _project_root (Optional[Path]): 项目根目录缓存
        _using_user_config (bool): 当前是否使用用户配置
        _current_config_path (Optional[Path]): 当前加载的配置文件路径
    """
    
    def __init__(self):
        """
        初始化配置加载器     
        
        
        Example:
            >>> # 用于直接加载（不使用模块名）
            >>> loader = ConfigLoader()
            >>> config = loader.load('display', 'config.yaml')
            >>> 
            >>> # 用于合并加载（需要模块名）
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> config = loader.load_merged()  # 自动合并用户配置
        """
        
        
        self._project_root = None
        """项目根目录缓存，避免重复查找"""
        
        self._using_user_config = False
        """标记当前是否使用了用户配置"""
        
        self._current_config_path = None
        """当前加载的配置文件路径（项目配置或用户配置）"""
    
    def _get_project_root(self) -> Path:
        """
        获取项目根目录
        
        通过向上查找包含 config 目录的父目录来确定项目根目录。
        支持开发环境和打包环境。
        
        Returns:
            Path: 项目根目录的绝对路径
        
        Example:
            >>> loader = ConfigLoader()
            >>> root = loader._get_project_root()
            >>> print(root)
            /path/to/magicmirror
        """
        if self._project_root is None:
            current = Path(__file__).resolve()
            # 向上查找包含 config 目录的父目录
            # for parent in current.parents:
            #     if (parent / 'config').is_dir():
            #         self._project_root = parent
            #         break
            # else:
                # 后备方案：从当前文件向上 4 层
            # 层级: current -> management -> magicm -> src -> project
            self._project_root = current.parent.parent.parent.parent.parent
        return self._project_root
    
    def get_config_path(self, *paths: str) -> Path:
        """
        获取配置文件路径（通用方法）
        
        根据传入的路径组件，构建 config 目录下的完整文件路径。
        该方法不检查文件是否存在，只负责路径构建。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: get_config_path('display', 'config.yaml')
                   例如: get_config_path('detector', 'gpu', 'nvidia.yaml')
        
        Returns:
            Path: 配置文件完整路径
        
        Example:
            >>> loader = ConfigLoader()
            >>> path = loader.get_config_path('display', 'config.yaml')
            >>> print(path)
            /project/config/display/config.yaml
        """
        project_root = self._get_project_root()
        config_path = project_root / 'config'
        for p in paths:
            config_path = config_path / p
        return config_path
    
    def get_project_config_path(self) -> Optional[Path]:
        """
        获取项目配置文件路径
        
        根据初始化时设置的 module_name 和 config_filename，返回项目配置文件的完整路径。
        项目配置文件位于项目源码的 config 目录下，是只读的默认配置。
        
        Returns:
            Optional[Path]: 项目配置文件路径，如果未设置 module_name 或 config_filename 则返回 None
        
        Example:
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> path = loader.get_project_config_path()
            >>> print(path)
            /project/config/display/config.yaml
        """
        if self.module_name is None or self.config_filename is None:
            return None
        return self.get_config_path(self.module_name, self.config_filename)
    
    def get_user_config_path(self) -> Optional[Path]:
        """
        获取用户配置文件路径
        
        用户配置文件存储在用户配置目录中，用于覆盖项目配置。
        不同操作系统的用户配置目录：
        - Linux: ~/.config/magicm/
        - macOS: ~/Library/Application Support/magicm/
        - Windows: C:\\Users\\<User>\\AppData\\Local\\magicm\\
        
        Returns:
            Optional[Path]: 用户配置文件路径，如果未设置 module_name 或 config_filename 则返回 None
        
        Example:
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> path = loader.get_user_config_path()
            >>> print(path)
            /home/user/.config/magicm/display/config.yaml
        """
        if self.module_name is None or self.config_filename is None:
            return None
        user_dir = user_config_dir("magicm", "magicm")
        return Path(user_dir) / self.module_name / self.config_filename
    
    def get_current_config_path(self) -> Optional[Path]:
        """
        获取当前使用的配置文件路径
        
        返回最近一次 load_merged() 实际加载的配置文件路径。
        可能是项目配置文件，也可能是用户配置文件（如果存在）。
        
        Returns:
            Optional[Path]: 当前使用的配置文件路径，未加载时返回 None
        
        Example:
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> config = loader.load_merged()
            >>> current_path = loader.get_current_config_path()
            >>> print(f"当前使用: {current_path}")
        """
        return self._current_config_path
    
    def is_using_user_config(self) -> bool:
        """
        是否正在使用用户配置
        
        检查最近一次 load_merged() 是否使用了用户配置覆盖项目配置。
        
        Returns:
            bool: 使用用户配置返回 True，否则返回 False
        
        Example:
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> config = loader.load_merged()
            >>> if loader.is_using_user_config():
            ...     print("正在使用自定义配置")
            ... else:
            ...     print("正在使用默认配置")
        """
        return self._using_user_config
    
    def load(self, *paths: str) -> Dict[str, Any]:
        """
        加载 YAML 配置文件（直接加载，不合并）
        
        直接从指定路径加载配置文件，不进行用户配置合并。
        适用于不需要用户自定义配置的场景。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: load('display', 'config.yaml')
                   例如: load('detector', 'gpu', 'nvidia.yaml')
        
        Returns:
            Dict[str, Any]: 解析后的配置字典，文件为空时返回空字典
        
        Raises:
            FileNotFoundError: 配置文件不存在时抛出
        
        Example:
            >>> loader = ConfigLoader()
            >>> config = loader.load('display', 'config.yaml')
            >>> print(config.get('gpu_ratings'))
        """
        file_path = self.get_config_path(*paths)
        
        if not file_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
        
    def load_all_from_directory(self, *paths: str) -> Dict[str, Dict[str, Any]]:
        """
        加载指定目录下的所有 YAML 配置文件        
        从指定目录加载所有 .yaml 和 .yml 文件，返回以文件名（不含扩展名）为键的配置字典。
        Args:
            *paths: config 目录下的路径(相对于config)        
        Returns:
            Dict[str, Dict[str, Any]]: 配置字典，格式为 {文件名: 配置内容}        
        Raises:
            FileNotFoundError: 目录不存在时抛出        
        Example:
            >>> loader = ConfigLoader()
            >>> configs = loader.load_all_from_directory('display')
            >>> print(configs.keys())  # ['config', 'settings']
        """
        dir_path = self.get_config_path(*paths)
        
        if not dir_path.exists():
            raise FileNotFoundError(f"目录不存在: {dir_path}")
        
        configs = {}
        # 同时匹配 .yaml 和 .yml 扩展名
        for file_path in list(dir_path.glob('*.yaml')) + list(dir_path.glob('*.yml')):
            with open(file_path, 'r', encoding='utf-8') as f:
                configs[file_path.stem] = yaml.safe_load(f) or {}        
        return configs    

    def load_merged(self) -> Dict[str, Any]:
        """
        加载合并后的配置（项目配置 + 用户配置）
        
        加载项目配置，如果用户配置存在，则用用户配置覆盖项目配置。
        用户配置的优先级高于项目配置，可以实现配置的自定义。
        
        配置合并规则：
        - 简单类型：用户配置直接覆盖项目配置
        - 字典类型：递归合并，用户配置的键值对覆盖项目配置的同名键
        - 列表类型：用户配置完全替换项目配置（不合并列表元素）
        
        Returns:
            Dict[str, Any]: 合并后的配置字典
        
        Raises:
            ValueError: 未设置 module_name 或 config_filename 时抛出
            FileNotFoundError: 项目配置文件不存在时抛出
        
        Example:
            >>> loader = ConfigLoader('display', 'config.yaml')
            >>> config = loader.load_merged()
            >>> # 用户配置会覆盖项目配置中的相同键
            >>> print(config.get('gpu_ratings'))
        """
        if self.module_name is None or self.config_filename is None:
            raise ValueError("未设置 module_name 和 config_filename")
        
        project_path = self.get_project_config_path()
        user_path = self.get_user_config_path()
        
        # 加载项目配置（必须存在）
        if not project_path.exists():
            raise FileNotFoundError(f"项目配置文件不存在: {project_path}")
        
        with open(project_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f) or {}
        
        # 如果用户配置存在，合并
        if user_path.exists():
            with open(user_path, 'r', encoding='utf-8') as f:
                user_config = yaml.safe_load(f) or {}
                self._deep_merge(config, user_config)
            self._using_user_config = True
            self._current_config_path = user_path
        else:
            self._using_user_config = False
            self._current_config_path = project_path
        
        return config
    
    def exists(self, *paths: str) -> bool:
        """
        检查配置文件是否存在
        
        判断指定路径的配置文件是否存在于文件系统中。
        
        Args:
            *paths: config 目录下的路径组件
        
        Returns:
            bool: 配置文件存在返回 True，否则返回 False
        
        Example:
            >>> loader = ConfigLoader()
            >>> if loader.exists('display', 'config.yaml'):
            ...     print("配置文件存在")
            ... else:
            ...     print("配置文件不存在")
        """
        return self.get_config_path(*paths).exists()
    
    def _deep_merge(self, base: dict, updates: dict):
        """
        深度合并两个字典
        
        将 updates 字典中的键值对合并到 base 字典中。
        对于字典类型的值，递归合并；其他类型的值直接覆盖。
        
        Args:
            base: 目标字典（会被修改）
            updates: 源字典（提供覆盖值）
        
        Example:
            >>> loader = ConfigLoader()
            >>> base = {'a': 1, 'b': {'c': 2, 'd': 3}}
            >>> updates = {'b': {'c': 4}, 'e': 5}
            >>> loader._deep_merge(base, updates)
            >>> print(base)
            {'a': 1, 'b': {'c': 4, 'd': 3}, 'e': 5}
        """
        for key, value in updates.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                # 都是字典，递归合并
                self._deep_merge(base[key], value)
            else:
                # 其他情况，直接覆盖
                base[key] = value