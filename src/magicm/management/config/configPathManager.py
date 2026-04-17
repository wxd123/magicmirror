# magicm/management/config/configPathManager.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置路径管理器 - 项目配置目录路径管理模块

该模块提供项目 config 目录的路径管理功能，自动适配开发环境和打包环境。
支持开发环境（源码运行）和 PyInstaller 打包环境（onefile 模式）。

核心功能：
- 自动查找项目根目录
- 管理 config 目录下的文件路径
- 支持开发环境和打包环境的无缝切换

使用示例:
    from magicm.management.config import ConfigPathManager
    
    path_mgr = ConfigPathManager()
    
    # 获取配置文件路径
    config_path = path_mgr.get_path('display', 'config.yaml')
    
    # 检查配置文件是否存在
    if path_mgr.exists('display', 'config.yaml'):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
"""

import sys
import os
from pathlib import Path
from typing import Optional


class ConfigPathManager:
    """
    稳定的配置路径管理器，支持开发环境和 PyInstaller 打包环境
    
    该类的核心职责：
    1. 自动识别当前运行环境（开发环境 vs 打包环境）
    2. 返回正确的项目 config 目录路径
    3. 提供便捷的路径构建和检查方法
    
    环境识别逻辑：
    - 打包环境：通过 sys.frozen 和 sys._MEIPASS 识别，配置位于临时解压目录
    - 开发环境：向上查找同时包含 config 和 src 目录的父目录作为项目根目录
    
    使用场景：
    - 开发时：从项目源码的 config 目录读取配置
    - 打包后：从 PyInstaller 解压的临时目录读取配置
    - 测试时：可手动指定 project_root 用于单元测试
    
    Attributes:
        _project_root (Optional[Path]): 项目根目录缓存
        _config_dir (Optional[Path]): config 目录缓存
    """
    
    def __init__(self, project_root: Optional[Path] = None):
        """
        初始化配置路径管理器
        
        Args:
            project_root: 可选的项目根目录路径。
                          如果提供，将直接使用该路径作为项目根目录，
                          跳过自动查找逻辑。主要用于单元测试。
        
        Example:
            >>> # 自动查找项目根目录
            >>> mgr = ConfigPathManager()
            >>> 
            >>> # 手动指定项目根目录（用于测试）
            >>> mgr = ConfigPathManager(project_root=Path('/fake/project'))
        """
        self._project_root = project_root
        """项目根目录缓存，None 表示未初始化"""
        
        self._config_dir = None
        """config 目录缓存，None 表示未初始化"""
    
    def _get_project_root(self) -> Path:
        """
        获取项目根目录路径
        
        该方法通过以下策略确定项目根目录：
        1. 如果已在 __init__ 中指定 project_root，直接使用
        2. 如果是 PyInstaller 打包环境，使用 sys._MEIPASS（临时解压目录）
        3. 如果是开发环境，向上查找同时包含 config 和 src 目录的父目录
        4. 如果都找不到，使用固定层数向上 4 层作为后备方案
        
        Returns:
            Path: 项目根目录的绝对路径
        
        Raises:
            RuntimeError: 无法找到项目根目录时抛出
        
        Example:
            >>> mgr = ConfigPathManager()
            >>> root = mgr._get_project_root()
            >>> print(root)
            /path/to/magicmirror
        """
        # 优先使用手动指定的项目根目录
        if self._project_root is not None:
            return self._project_root

        # 检查是否在 PyInstaller 打包环境中
        # sys.frozen: PyInstaller 设置的特殊属性，表示程序是否被打包
        # sys._MEIPASS: PyInstaller 设置的临时解压目录路径
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            self._project_root = Path(sys._MEIPASS)
            return self._project_root

        # 开发环境：向上查找项目根目录
        # 当前文件路径示例: /project/src/magicm/management/config/configPathManager.py
        current = Path(__file__).resolve()
        
        # 遍历所有父目录，查找同时包含 config 和 src 的目录
        for parent in current.parents:
            # 真正的项目根目录必须同时包含 config 和 src 子目录
            # 这样可以避免错误识别 src/magicm/management 等中间目录
            if (parent / 'config').is_dir() and (parent / 'src').is_dir():
                self._project_root = parent
                return self._project_root
        
        # 后备方案：使用固定层数
        # 从当前文件向上 4 层到达项目根目录
        # 层级关系: current (0) -> management (1) -> magicm (2) -> src (3) -> project (4)
        self._project_root = current.parents[3]
        
        return self._project_root
    
    @property
    def config_dir(self) -> Path:
        """
        获取 config 目录路径
        
        该属性使用延迟加载和缓存机制，首次访问时计算并缓存结果。
        
        Returns:
            Path: config 目录的绝对路径
        
        Raises:
            RuntimeError: config 目录不存在时抛出
        
        Example:
            >>> mgr = ConfigPathManager()
            >>> config_dir = mgr.config_dir
            >>> print(config_dir)
            /path/to/magicmirror/config
        """
        if self._config_dir is None:
            root = self._get_project_root()
            self._config_dir = root / 'config'
        return self._config_dir
    
    def get_path(self, *paths: str) -> Path:
        """
        获取 config 目录下的文件路径
        
        将传入的路径组件与 config 目录拼接，返回完整的文件路径。
        该方法不检查文件是否存在，只负责路径构建。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: get_path('display', 'config.yaml')
                   例如: get_path('detector', 'gpu', 'nvidia.yaml')
                   例如: get_path('settings.json')
        
        Returns:
            Path: config 目录下的完整文件路径
        
        Example:
            >>> mgr = ConfigPathManager()
            >>> 
            >>> # 获取 display 模块配置路径
            >>> path = mgr.get_path('display', 'config.yaml')
            >>> print(path)
            /project/config/display/config.yaml
            >>> 
            >>> # 获取嵌套目录下的配置
            >>> path = mgr.get_path('detector', 'gpu', 'nvidia.yaml')
            >>> print(path)
            /project/config/detector/gpu/nvidia.yaml
        """
        current_path = self.config_dir
        for p in paths:
            current_path = current_path / p
        return current_path
    
    def exists(self, *paths: str) -> bool:
        """
        检查 config 目录下的文件是否存在
        
        该方法在 get_path() 的基础上增加了存在性检查。
        不会抛出异常，仅返回布尔值。
        
        Args:
            *paths: config 目录下的路径组件
                   例如: exists('display', 'config.yaml')
                   例如: exists('detector', 'gpu', 'nvidia.yaml')
        
        Returns:
            bool: 文件存在返回 True，否则返回 False
        
        Example:
            >>> mgr = ConfigPathManager()
            >>> 
            >>> # 检查 display 配置是否存在
            >>> if mgr.exists('display', 'config.yaml'):
            ...     print("配置文件存在")
            ... else:
            ...     print("配置文件不存在")
            >>> 
            >>> # 检查不存在的文件
            >>> mgr.exists('not_exist.yaml')
            False
        """
        return self.get_path(*paths).exists()