
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/deploy/enviroment/env_setup.py
"""环境一键设置模块"""

from pathlib import Path
from .env_manage import EnvManager
from .env_uv_installer import uv_util


def setup_env(
    env_name: str,
    env_path: Path,
    python_version: str = '3.11',
    force: bool = False
) -> bool:
    """
    一键设置环境：确保 UV 已安装，确保虚拟环境已创建
    
    Args:
        env_name: 环境名称
        env_path: 环境路径
        python_version: Python版本
        force: 是否强制重建虚拟环境
    
    Returns:
        是否成功
    """
    # 1. 检测并安装 UV
    print("检查 UV 安装状态...")
    if not uv_util.ensure():
        print("UV 安装失败，无法继续")
        return False
    print(f"UV 已就绪: {uv_util.version()}")
    
    # 2. 检测虚拟环境
    manager = EnvManager(env_name, env_path, python_version)
    
    if manager.exists():
        if force:
            print(f"强制删除已存在的环境: {env_name}")
            manager.delete()
        else:
            print(f"环境已存在: {env_name}")
            return True
    
    # 3. 创建虚拟环境
    print(f"创建虚拟环境: {env_name}")
    return manager.create()


def quick_setup(env_name: str, base_path: str = '/opt/magicm') -> bool:
    """
    快速设置 - 使用默认配置
    
    Args:
        env_name: 环境名称
        base_path: 基础路径，默认为 /opt/magicm
    
    Returns:
        是否成功
    """
    return setup_env(env_name, Path(base_path) / env_name)