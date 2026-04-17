#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/management/config/configWriter.py
"""
配置写入器 - 配置修改和保存模块

该模块提供配置的读写功能，支持修改配置并将修改保存到用户配置文件中。
配置写入器支持延迟加载，在首次使用时才加载配置。

核心功能：
- 读取配置：支持读取配置项
- 修改配置：支持横向设置、纵向设置（嵌套路径）、批量更新
- 保存配置：将修改保存到用户配置文件
- 配置管理：支持重载配置、切换配置来源

使用示例:
    from magicm.management.config import ConfigWriter
    
    # 无参构造，调用时传入模块名
    writer = ConfigWriter()
    
    # 修改配置
    writer.set('display', 'timeout', 30)
    writer.set_path('display', 'gpu_ratings.nuclear', ['RTX 5090', 'RX 8900'])
    
    # 批量更新
    writer.update('display', {
        'version': '2.0',
        'author': 'magicm'
    })
    
    # 保存到用户配置
    writer.save('display')
    
    # 重新加载（从文件重新读取）
    writer.reload('display')
"""

from typing import Dict, Any, Optional
from .configLoader import ConfigLoader


class ConfigWriter:
    """
    配置写入器 - 可读写的配置管理类
    
    该类提供完整的配置读写功能，所有修改默认保存在用户配置目录中，
    不会影响项目默认配置。支持横向和纵向（嵌套）的配置操作。
    支持延迟加载，在首次使用时才加载配置。
    
    配置存储策略：
    - 项目配置：存储在项目源码 config 目录，只读，作为默认配置
    - 用户配置：存储在用户配置目录（如 ~/.config/magicm/），可写，
      用户修改会保存到这里，优先级高于项目配置
    
    特点：
    - 延迟加载：首次使用时才加载配置
    - 写入能力：支持修改和添加配置项
    - 嵌套操作：支持点号分隔的路径访问嵌套配置
    - 安全保存：修改保存到用户配置，不影响项目配置
    
    Attributes:
        _loaders (Dict[str, ConfigLoader]): 各模块的配置加载器缓存
        _configs (Dict[str, Dict[str, Any]]): 各模块的配置字典缓存
    """
    
    def __init__(self):
        """
        初始化配置写入器
        
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
    
    def _set_config(self, module_name: str, config: Dict[str, Any], config_filename: str = "config.yaml"):
        """
        设置指定模块的配置
        
        Args:
            module_name: 模块名称
            config: 配置字典
            config_filename: 配置文件名
        """
        key = f"{module_name}:{config_filename}"
        self._configs[key] = config
    
    # ============================================================
    # 读取方法
    # ============================================================
    
    def get(self, module_name: str, key: str, default: Any = None, config_filename: str = "config.yaml") -> Any:
        """
        横向获取配置项
        
        直接从配置字典的顶层获取指定键的值。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            key: 配置键名（顶层键）
            default: 键不存在时返回的默认值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Any: 配置值，键不存在时返回 default
        
        Example:
            >>> writer = ConfigWriter()
            >>> version = writer.get('display', 'version', default='1.0')
        """
        config = self._get_config(module_name, config_filename)
        return config.get(key, default)
    
    def get_path(self, module_name: str, path: str, default: Any = None, config_filename: str = "config.yaml") -> Any:
        """
        纵向获取配置项（点分隔路径）
        
        通过点号分隔的路径字符串访问嵌套配置。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            path: 点号分隔的嵌套路径，如 'gpu_ratings.nuclear'
            default: 路径不存在时返回的默认值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            Any: 路径对应的配置值，路径不存在时返回 default
        
        Example:
            >>> writer = ConfigWriter()
            >>> nuclear = writer.get_path('display', 'gpu_ratings.nuclear', default=[])
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
            >>> writer = ConfigWriter()
            >>> ratings = writer.get_multi('display', [
            ...     'gpu_ratings.nuclear',
            ...     'gpu_ratings.flagship',
            ...     'version'
            ... ])
        """
        result = {}
        for key in keys:
            if '.' in key:
                result[key] = self.get_path(module_name, key, default, config_filename)
            else:
                result[key] = self.get(module_name, key, default, config_filename)
        return result
    
    # ============================================================
    # 写入方法
    # ============================================================
    
    def set(self, module_name: str, key: str, value: Any, config_filename: str = "config.yaml"):
        """
        横向设置配置项
        
        直接设置配置字典顶层的键值对。
        修改后需要调用 save() 方法才能持久化到文件。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            key: 配置键名（顶层键）
            value: 要设置的值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.set('display', 'timeout', 30)
            >>> writer.set('display', 'version', '2.0')
            >>> writer.save('display')  # 保存到文件
        """
        config = self._get_config(module_name, config_filename)
        config[key] = value
    
    def set_path(self, module_name: str, path: str, value: Any, config_filename: str = "config.yaml"):
        """
        纵向设置嵌套配置项
        
        通过点号分隔的路径设置嵌套配置的值。
        如果路径中的中间键不存在，会自动创建。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            path: 点号分隔的嵌套路径，如 'gpu_ratings.nuclear'
            value: 要设置的值
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> 
            >>> # 设置嵌套配置
            >>> writer.set_path('display', 'gpu_ratings.nuclear', ['RTX 5090', 'RX 8900'])
            >>> writer.set_path('display', 'system_ratings.linux.rating', '稳得一批')
            >>> 
            >>> # 自动创建中间键
            >>> writer.set_path('display', 'a.b.c.d', 'value')  # 自动创建 a, b, c 字典
            >>> writer.save('display')
        """
        config = self._get_config(module_name, config_filename)
        keys = path.split('.')
        target = config
        # 遍历到倒数第二个键，确保存在所有中间字典
        for key in keys[:-1]:
            if key not in target:
                target[key] = {}
            target = target[key]
        # 设置最后一个键的值
        target[keys[-1]] = value
    
    def update(self, module_name: str, updates: Dict[str, Any], config_filename: str = "config.yaml"):
        """
        批量更新配置
        
        使用字典批量更新多个顶层配置项。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            updates: 包含键值对的字典，键为顶层配置键名
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.update('display', {
            ...     'timeout': 30,
            ...     'retry_count': 3,
            ...     'version': '2.0'
            ... })
            >>> writer.save('display')
        """
        config = self._get_config(module_name, config_filename)
        for key, value in updates.items():
            config[key] = value
    
    def update_path(self, module_name: str, updates: Dict[str, Any], config_filename: str = "config.yaml"):
        """
        批量更新嵌套配置
        
        使用字典批量更新多个嵌套配置项，键名支持点号分隔的路径。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            updates: 包含路径-值对的字典
                    键为点号分隔的路径，值为要设置的内容
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.update_path('display', {
            ...     'gpu_ratings.nuclear': ['RTX 5090'],
            ...     'gpu_ratings.flagship': ['RTX 4080'],
            ...     'system_ratings.linux.rating': '稳得一批'
            ... })
            >>> writer.save('display')
        """
        config = self._get_config(module_name, config_filename)
        for path, value in updates.items():
            keys = path.split('.')
            target = config
            for key in keys[:-1]:
                if key not in target:
                    target[key] = {}
                target = target[key]
            target[keys[-1]] = value
    
    # ============================================================
    # 保存方法
    # ============================================================
    
    def save(self, module_name: str, config_filename: str = "config.yaml") -> bool:
        """
        保存配置到用户文件
        
        将当前配置保存到用户配置目录，不会影响项目默认配置。
        用户配置优先级高于项目配置，下次加载时会自动合并。
        
        用户配置文件位置：
        - Linux: ~/.config/magicm/{module_name}/config.yaml
        - macOS: ~/Library/Application Support/magicm/{module_name}/config.yaml
        - Windows: C:\\Users\\<User>\\AppData\\Local\\magicm\\{module_name}\\config.yaml
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            bool: 保存成功返回 True，失败返回 False
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.set('display', 'timeout', 30)
            >>> writer.set_path('display', 'gpu_ratings.nuclear', ['RTX 5090'])
            >>> writer.save('display')  # 保存到用户配置
        """
        config = self._get_config(module_name, config_filename)
        loader = self._get_loader(module_name, config_filename)
        return loader.save(config, to_user_config=True)
    
    def save_as_project(self, module_name: str, config_filename: str = "config.yaml") -> bool:
        """
        保存配置到项目文件（需要权限）
        
        将当前配置保存到项目源码的 config 目录，覆盖项目默认配置。
        通常需要管理员权限，且不建议在生产环境使用。
        
        警告：
        - 需要项目目录的写入权限
        - 会影响所有用户的默认配置
        - 建议仅在开发或调试时使用
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Returns:
            bool: 保存成功返回 True，失败返回 False
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.set('display', 'version', '2.0')
            >>> # 谨慎使用，需要权限
            >>> writer.save_as_project('display')
        """
        config = self._get_config(module_name, config_filename)
        loader = self._get_loader(module_name, config_filename)
        return loader.save(config, to_user_config=False)
    
    # ============================================================
    # 配置管理
    # ============================================================
    
    def reload(self, module_name: str, config_filename: str = "config.yaml"):
        """
        重新加载配置
        
        从文件系统重新加载配置（项目配置 + 用户配置合并），
        更新内存中的配置数据。会丢失未保存的修改。
        
        使用场景：
        - 外部程序修改了配置文件
        - 需要恢复到文件中的配置状态
        - 切换配置来源后
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.set('display', 'timeout', 100)  # 临时修改
            >>> writer.reload('display')  # 放弃修改，重新从文件加载
            >>> timeout = writer.get('display', 'timeout')  # 恢复到文件中的值
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
            >>> writer = ConfigWriter()
            >>> writer.reload_all()
        """
        self._loaders.clear()
        self._configs.clear()
    
    def switch_to_user_config(self, module_name: str, config_filename: str = "config.yaml"):
        """
        切换到用户配置
        
        重新加载配置，确保优先使用用户配置。
        如果用户配置存在，会覆盖项目配置中的相同项。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.switch_to_user_config('display')
            >>> # 现在配置来自用户目录（如果存在）
        """
        loader = self._get_loader(module_name, config_filename)
        loader.switch_to_user_config()
        self.reload(module_name, config_filename)
    
    def switch_to_project_config(self, module_name: str, config_filename: str = "config.yaml"):
        """
        切换到项目配置
        
        重新加载配置，只使用项目配置，忽略用户配置。
        
        Args:
            module_name: 模块名称，如 'display', 'detector'
            config_filename: 配置文件名，默认为 'config.yaml'
        
        Example:
            >>> writer = ConfigWriter()
            >>> writer.switch_to_project_config('display')
            >>> # 现在只使用项目默认配置
        """
        loader = self._get_loader(module_name, config_filename)
        loader.switch_to_project_config()
        self.reload(module_name, config_filename)
    
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
            >>> writer = ConfigWriter()
            >>> source = writer.get_config_source('display')
            >>> print(f"项目配置: {source['project_config']}")
            >>> print(f"用户配置: {source['user_config']}")
            >>> print(f"当前使用: {source['current_config']}")
        """
        loader = self._get_loader(module_name, config_filename)
        return {
            "project_config": str(loader.get_project_config_path()),
            "user_config": str(loader.get_user_config_path()),
            "current_config": str(loader.get_current_config_path()),
            "using_user_config": str(loader.is_using_user_config())
        }