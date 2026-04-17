#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/management/config/configReader.py
"""
配置读取器 - 只读配置访问模块

该模块提供只读的配置访问功能，支持从项目配置和用户配置合并后的结果中读取配置。
配置读取器支持延迟加载，在首次使用时才加载配置。

核心功能：
- 横向获取：直接通过键名获取配置值
- 纵向获取：通过点号分隔的路径获取嵌套配置值
- 批量获取：同时获取多个配置项
- 配置重载：重新从文件加载配置
- 来源追踪：获取当前配置的来源信息

使用示例:
    from magicm.management.config import ConfigReader
    
    # 无参构造，调用时传入模块名
    reader = ConfigReader()
    
    # 横向获取
    timeout = reader.get('display', 'timeout', default=30)
    
    # 纵向获取嵌套配置
    nuclear = reader.get_path('display', 'gpu_ratings.nuclear', default=[])
    
    # 批量获取
    ratings = reader.get_multi('display', ['gpu_ratings.nuclear', 'gpu_ratings.flagship'])
    
    # 查看配置来源
    source = reader.get_config_source('display')
    print(f"当前使用: {source['current_config']}")
"""

from typing import Dict, Any, Optional
from .configLoader import ConfigLoader


class ConfigReader:
    """
    配置读取器 - 只读配置访问
    
    该类提供只读的配置访问接口，支持延迟加载配置。
    配置在首次访问时从文件加载并合并（项目配置 + 用户配置），
    后续读取操作直接使用缓存，性能高效。
    
    特点：
    - 只读：不提供任何写入或修改配置的方法
    - 延迟加载：首次使用时才加载配置
    - 自动合并：自动合并项目配置和用户配置
    - 支持嵌套：通过点号分隔的路径访问嵌套配置
    - 来源追踪：可以查询配置来自项目文件还是用户文件
    
    Attributes:
        _loaders (Dict[str, ConfigLoader]): 各模块的配置加载器缓存
        _configs (Dict[str, Dict[str, Any]]): 各模块的配置字典缓存
    """
    
    def __init__(self):
        """
        初始化配置读取器
        
        无参构造，配置在首次使用时才加载。
        """
        self._loaders: Dict[str, ConfigLoader] = {}
        """Dict[str, ConfigLoader]: 各模块的配置加载器缓存"""
        
        self._configs: Dict[str, Dict[str, Any]] = {}
        """Dict[str, Dict[str, Any]]: 各模块的配置字典缓存"""
    
    def _get_loader(self, module_name: str, config_filename: str = "config.yaml") -> ConfigLoader:
        """
        获取或创建指定模块的配置加载器
        
        Args:
            module_name: 模块名称
            config_filename: 配置文件名
        
        Returns:
            ConfigLoader: 配置加载器实例
        """
        key = f"{module_name}:{config_filename}"
        if key not in self._loaders:
            self._loaders[key] = ConfigLoader(module_name, config_filename)
        return self._loaders[key]
    
    def _get_config(self, module_name: str, config_filename: str = "config.yaml") -> Dict[str, Any]:
        """
        获取或加载指定模块的配置
        
        Args:
            module_name: 模块名称
            config_filename: 配置文件名
        
        Returns:
            Dict[str, Any]: 合并后的配置字典
        """
        key = f"{module_name}:{config_filename}"
        if key not in self._configs:
            loader = self._get_loader(module_name, config_filename)
            self._configs[key] = loader.load_merged()
        return self._configs[key]
    
    def get(self, module_name: str, key: str, default: Any = None, config_filename: str = "config.yaml") -> Any:
        """
        横向获取配置项
        
        直接从配置字典的顶层获取指定键的值。
        适用于获取非嵌套的顶级配置项。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            key: 配置键名（顶层键）
            default: 键不存在时返回的默认值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Any: 配置值，键不存在时返回 default
        
        Example:
            >>> reader = ConfigReader()
            >>> 
            >>> # 获取 display 模块的顶级配置
            >>> version = reader.get('display', 'version', default='1.0')
            >>> 
            >>> # 获取不存在的键
            >>> unknown = reader.get('display', 'unknown_key', default='默认值')
        """
        config = self._get_config(module_name, config_filename)
        return config.get(key, default)
    
    def get_path(self, module_name: str, path: str, default: Any = None, config_filename: str = "config.yaml") -> Any:
        """
        纵向获取配置项（点分隔路径）
        
        通过点号分隔的路径字符串访问嵌套配置。
        例如 'gpu_ratings.nuclear' 会访问 config['gpu_ratings']['nuclear']。
        
        路径解析规则：
        - 每个路径段作为字典的键
        - 如果中间任一键不存在或对应的值不是字典，返回 default
        - 支持任意深度的嵌套
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            path: 点号分隔的嵌套路径，如 'gpu_ratings.nuclear'
            default: 路径不存在时返回的默认值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Any: 路径对应的配置值，路径不存在时返回 default
        
        Example:
            >>> reader = ConfigReader()
            >>> 
            >>> # 获取 display 模块的嵌套配置
            >>> nuclear = reader.get_path('display', 'gpu_ratings.nuclear', default=[])
            >>> flagship = reader.get_path('display', 'gpu_ratings.flagship', default=[])
            >>> 
            >>> # 获取更深层的嵌套
            >>> rating = reader.get_path('display', 'system_ratings.linux.rating', default='未知')
        """
        config = self._get_config(module_name, config_filename)
        keys = path.split('.')
        value = config
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
                if value is None:
                    return default
            else:
                return default
        
        return value if value is not None else default
    
    def get_multi(self, module_name: str, keys: list, default: Any = None, config_filename: str = "config.yaml") -> Dict[str, Any]:
        """
        批量获取多个配置项
        
        同时获取多个配置项，返回包含键值对的字典。
        自动识别键名是否包含点号，分别调用 get() 或 get_path()。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            keys: 配置键名列表，支持点号分隔的路径
            default: 键不存在时返回的默认值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Dict[str, Any]: 键名到配置值的映射字典
        
        Example:
            >>> reader = ConfigReader()
            >>> 
            >>> # 批量获取多个配置
            >>> ratings = reader.get_multi('display', [
            ...     'gpu_ratings.nuclear',
            ...     'gpu_ratings.flagship', 
            ...     'gpu_ratings.high',
            ...     'version'
            ... ], default=[])
            >>> 
            >>> nuclear = ratings['gpu_ratings.nuclear']
            >>> version = ratings['version']
        """
        result = {}
        for key in keys:
            if '.' in key:
                result[key] = self.get_path(module_name, key, default, config_filename)
            else:
                result[key] = self.get(module_name, key, default, config_filename)
        return result
    
    def reload(self, module_name: str, config_filename: str = "config.yaml"):
        """
        重新加载配置
        
        从文件系统重新加载配置（项目配置 + 用户配置合并），
        更新内存中的配置数据。适用于配置文件在运行时被外部修改的场景。
        
        注意：重新加载会丢失所有未保存的内存修改（如果存在）。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> reader = ConfigReader()
            >>> 
            >>> # 外部修改了配置文件后，重新加载
            >>> reader.reload('display')
            >>> new_config = reader.get_path('display', 'some.key')
        """
        key = f"{module_name}:{config_filename}"
        if key in self._configs:
            loader = self._get_loader(module_name, config_filename)
            self._configs[key] = loader.load_merged()
    
    def reload_all(self):
        """
        重新加载所有已加载的配置
        
        清空所有缓存，下次访问时会重新从文件加载。
        
        Example:
            >>> reader = ConfigReader()
            >>> 
            >>> # 批量重新加载所有配置
            >>> reader.reload_all()
        """
        self._loaders.clear()
        self._configs.clear()
    
    def get_config_source(self, module_name: str, config_filename: str = "config.yaml") -> Dict[str, str]:
        """
        获取配置来源信息
        
        返回当前配置的来源详情，包括项目配置文件路径、用户配置文件路径、
        当前使用的配置文件路径以及是否使用了用户配置。
        
        此方法可用于调试和诊断配置加载问题。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Dict[str, str]: 包含以下键的字典：
                - 'project_config': 项目配置文件路径
                - 'user_config': 用户配置文件路径
                - 'current_config': 当前使用的配置文件路径
                - 'using_user_config': 是否使用了用户配置（字符串 'True'/'False'）
        
        Example:
            >>> reader = ConfigReader()
            >>> source = reader.get_config_source('display')
            >>> print(f"项目配置: {source['project_config']}")
            >>> print(f"用户配置: {source['user_config']}")
            >>> print(f"当前使用: {source['current_config']}")
            >>> print(f"使用用户配置: {source['using_user_config']}")
            >>> 
            >>> # 判断是否使用了用户自定义配置
            >>> if source['using_user_config'] == 'True':
            ...     print("正在使用用户自定义配置")
        """
        loader = self._get_loader(module_name, config_filename)
        return {
            "project_config": str(loader.get_project_config_path()),
            "user_config": str(loader.get_user_config_path()),
            "current_config": str(loader.get_current_config_path()),
            "using_user_config": str(loader.is_using_user_config())
        }