
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/management/config/configManager.py
"""
配置管理器 - 纯代理模块

该模块提供统一的配置管理入口，通过代理模式将具体功能委托给专门的组件：
- ConfigPathManager: 路径管理
- ConfigLoader: 配置加载
- ConfigReader: 配置读取
- ConfigWriter: 配置写入

使用示例:
    from magicm.management.config import ConfigManager
    
    cm = ConfigManager()
    
    # 获取配置文件路径
    path = cm.get_config_path('display', 'config.yaml')
    
    # 加载配置
    config = cm.load('display', 'config.yaml')
    
    # 读取嵌套配置
    value = cm.get(config, 'gpu_ratings.nuclear', default=[])
    
    # 修改配置
    cm.set(config, 'timeout', 30)
    cm.save(config, path)
"""

from pathlib import Path
from typing import Any, Dict, Optional
from .configPathManager import ConfigPathManager
from .configLoader import ConfigLoader
from .configReader import ConfigReader
from .configWriter import ConfigWriter


class ConfigManager:
    """
    配置管理器 - 纯代理类
    
    该类不包含任何业务逻辑，仅作为统一门面，将所有方法调用委托给专门的组件。
    这样设计的好处是：
    1. 统一入口：调用方只需知道 ConfigManager
    2. 职责单一：每个组件只负责自己的功能
    3. 易于扩展：添加新功能只需添加新的代理方法
    
    组件职责：
    - ConfigPathManager: 项目 config 目录下的路径管理
    - ConfigLoader: YAML 配置文件加载
    - ConfigReader: 配置项读取（支持嵌套键）
    - ConfigWriter: 配置项写入和保存
    """
    
    def __init__(self):
        """
        初始化配置管理器
        
        创建四个专门组件的实例，用于处理不同的配置管理任务。
        """
        self.path = ConfigPathManager()
        """ConfigPathManager: 路径管理器实例"""
        
        self.loader = ConfigLoader()
        """ConfigLoader: 配置加载器实例"""
        
        self.reader = ConfigReader()
        """ConfigReader: 配置读取器实例"""
        
        self.writer = ConfigWriter()
        """ConfigWriter: 配置写入器实例"""
    
    # ==================== ConfigPathManager 代理方法 ====================
    
    def get_config_path(self, *paths: str) -> Path:
        """
        获取配置文件路径
        
        代理 ConfigPathManager.get_path() 方法。
        根据传入的路径组件，构建 config 目录下的完整文件路径。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: get_config_path('display', 'config.yaml')
                   例如: get_config_path('detector', 'gpu', 'nvidia.yaml')
        
        Returns:
            Path: 完整的配置文件路径
        
        Example:
            >>> cm = ConfigManager()
            >>> path = cm.get_config_path('display', 'config.yaml')
            >>> print(path)
            /project/root/config/display/config.yaml
        """
        return self.path.get_path(*paths)
    
    def config_exists(self, *paths: str) -> bool:
        """
        检查配置文件是否存在
        
        代理 ConfigPathManager.exists() 方法。
        
        Args:
            *paths: config 目录下的路径组件
        
        Returns:
            bool: 配置文件存在返回 True，否则返回 False
        
        Example:
            >>> cm = ConfigManager()
            >>> if cm.config_exists('display', 'config.yaml'):
            ...     print("配置文件存在")
        """
        return self.path.exists(*paths)
    
    # ==================== ConfigLoader 代理方法 ====================
    
    def load(self, *paths: str) -> Dict[str, Any]:
        """
        加载 YAML 配置文件
        
        代理 ConfigLoader.load() 方法。
        从项目 config 目录下加载指定的 YAML 配置文件。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: load('display', 'config.yaml')
                   例如: load('detector', 'gpu', 'nvidia.yaml')
        
        Returns:
            Dict[str, Any]: 解析后的配置字典，文件为空时返回空字典
        
        Raises:
            FileNotFoundError: 配置文件不存在时抛出
        
        Example:
            >>> cm = ConfigManager()
            >>> config = cm.load('display', 'config.yaml')
            >>> print(config.get('gpu_ratings'))
        """
        return self.loader.load(*paths)
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
        return self.loader.load_all_from_directory(*paths)
    

    def load_merged(self) -> Dict[str, Any]:
        """
        加载合并后的配置（项目配置 + 用户配置）
        
        代理 ConfigLoader.load_merged() 方法。
        先加载项目配置，再用用户配置覆盖，实现配置的自定义。
        
        注意：此方法使用 ConfigManager 初始化时指定的模块名和配置文件名，
        因此调用前需要先创建 ConfigManager 实例时传入相应参数。
        
        Returns:
            Dict[str, Any]: 合并后的配置字典
        
        Example:
            >>> cm = ConfigManager('display', 'config.yaml')
            >>> config = cm.load_merged()  # 自动加载并合并用户配置
        """
        return self.loader.load_merged()
    
    # ==================== ConfigReader 代理方法 ====================
    
    def get(self, config: dict, key: str, default: Any = None) -> Any:
        """
        从配置字典中获取指定键的值
        
        代理 ConfigReader.get() 方法。
        支持点号分隔的嵌套键，如 'gpu_ratings.nuclear'。
        
        Args:
            config: 配置字典
            key: 配置键名，支持点号分隔的嵌套路径
            default: 键不存在时返回的默认值
        
        Returns:
            Any: 配置值，键不存在时返回 default
        
        Example:
            >>> cm = ConfigManager()
            >>> config = cm.load('display', 'config.yaml')
            >>> nuclear = cm.get(config, 'gpu_ratings.nuclear', default=[])
            >>> print(nuclear)
            ['rtx 5090', 'rx 8900']
        """
        return self.reader.get(config, key, default)
    
    def get_path(self, config: dict, path: str, default: Any = None) -> Any:
        """
        从配置字典中获取指定路径的值（别名方法）
        
        代理 ConfigReader.get_path() 方法。
        与 get() 方法功能相同，提供更语义化的方法名。
        
        Args:
            config: 配置字典
            path: 点号分隔的嵌套路径
            default: 路径不存在时返回的默认值
        
        Returns:
            Any: 配置值
        
        Example:
            >>> cm = ConfigManager()
            >>> config = cm.load('display', 'config.yaml')
            >>> value = cm.get_path(config, 'system_ratings.linux.rating')
        """
        return self.reader.get_path(config, path, default)
    
    # ==================== ConfigWriter 代理方法 ====================
    
    def set(self, config: dict, key: str, value: Any) -> None:
        """
        设置配置字典中指定键的值
        
        代理 ConfigWriter.set() 方法。
        直接修改传入的配置字典，不自动保存到文件。
        
        Args:
            config: 配置字典（会被直接修改）
            key: 配置键名
            value: 要设置的值
        
        Example:
            >>> cm = ConfigManager()
            >>> config = cm.load('display', 'config.yaml')
            >>> cm.set(config, 'timeout', 30)
            >>> # 需要手动调用 save 保存到文件
            >>> cm.save(config, '/path/to/config.yaml')
        """
        self.writer.set(config, key, value)
    
    def set_path(self, config: dict, path: str, value: Any) -> None:
        """
        设置配置字典中指定路径的值
        
        代理 ConfigWriter.set_path() 方法。
        支持点号分隔的嵌套路径，自动创建不存在的中间键。
        
        Args:
            config: 配置字典（会被直接修改）
            path: 点号分隔的嵌套路径，如 'a.b.c'
            value: 要设置的值
        
        Example:
            >>> cm = ConfigManager()
            >>> config = {}
            >>> cm.set_path(config, 'gpu_ratings.nuclear', ['rtx 5090'])
            >>> print(config)
            {'gpu_ratings': {'nuclear': ['rtx 5090']}}
        """
        self.writer.set_path(config, path, value)
    
    def save(self, config: dict, path: str) -> bool:
        """
        保存配置字典到 YAML 文件
        
        代理 ConfigWriter.save() 方法。
        将配置字典以 YAML 格式写入指定文件。
        
        Args:
            config: 配置字典
            path: 目标文件路径
        
        Returns:
            bool: 保存成功返回 True，失败返回 False
        
        Example:
            >>> cm = ConfigManager()
            >>> config = {'timeout': 30}
            >>> success = cm.save(config, '/path/to/config.yaml')
            >>> if success:
            ...     print("保存成功")
        """
        return self.writer.save(config, path)