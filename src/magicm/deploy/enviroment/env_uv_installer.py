#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/deploy/enviroment/env_uv_installer.py
"""UV 安装器"""

import subprocess
import sys
import shutil
from typing import Optional


class uv_util:
    """UV 包管理器安装器"""
    
    @staticmethod
    def installed() -> bool:
        """检查是否已安装"""
        return shutil.which('uv') is not None
    
    @staticmethod
    def version() -> Optional[str]:
        """获取版本号"""
        if not uv_util.installed():
            return None
        try:
            result = subprocess.run(['uv', '--version'], capture_output=True, text=True)
            return result.stdout.strip() if result.returncode == 0 else None
        except Exception:
            return None
    
    @staticmethod
    def install() -> bool:
        """安装 UV"""
        if uv_util.installed():
            return True
        
        print("正在安装 uv...")
        
        if sys.platform == 'win32':
            cmd = ['powershell', '-c', 'irm https://astral.sh/uv/install.ps1 | iex']
        else:
            cmd = ['sh', '-c', 'curl -LsSf https://astral.sh/uv/install.sh | sh']
        
        try:
            subprocess.run(cmd, capture_output=True, text=True, check=True)
            print("安装成功")
            return True
        except subprocess.CalledProcessError as e:
            print(f"安装失败: {e.stderr}")
            return False
        except Exception as e:
            print(f"安装异常: {e}")
            return False
    
    @staticmethod
    def ensure() -> bool:
        """确保已安装，未安装则自动安装"""
        return uv_util.installed() or uv_util.install()