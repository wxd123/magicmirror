#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/deploy/enviroment/env_manage.py

"""虚拟环境管理器"""

import subprocess
import sys
import os
import getpass
from pathlib import Path
from typing import Optional


class EnvManager:
    """虚拟环境管理器"""
    
    def __init__(self, name: str, env_root: Path, python_version: str = '3.11'):
        self.name = name
        self.env_root = Path(env_root)
        self.venv_path = self.env_root / '.venv'
        self.python_version = python_version
        self._bin_dir = 'Scripts' if sys.platform == 'win32' else 'bin'
    
    @property
    def _python_path(self) -> Path:
        if sys.platform == 'win32':
            return self.venv_path / self._bin_dir / 'python.exe'
        return self.venv_path / self._bin_dir / 'python'
    
    def exists(self) -> bool:
        """检查虚拟环境是否存在"""
        return self._python_path.exists() and self._python_path.is_file()
    
    def create(self, auto_sudo: bool = True) -> bool:
        """创建虚拟环境"""
        if self.exists():
            print(f"虚拟环境已存在: {self.venv_path}")
            return True
        
        print(f"正在创建虚拟环境: {self.name}")
        print(f"  根目录: {self.env_root}")
        print(f"  虚拟环境: {self.venv_path}")
        
        # 确保根目录存在
        try:
            self.env_root.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            if not auto_sudo:
                print(f"权限不足，无法创建目录: {self.env_root}")
                return False
            
            print(f"权限不足，使用 sudo 创建目录...")
            try:
                subprocess.run(['sudo', 'mkdir', '-p', str(self.env_root)], check=True)
                user = getpass.getuser()
                subprocess.run(['sudo', 'chown', '-R', user, str(self.env_root)], check=True)
            except Exception as e:
                print(f"sudo 创建目录失败: {e}")
                return False
        
        # 创建虚拟环境
        try:
            cmd = [sys.executable, '-m', 'venv', str(self.venv_path)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                # 尝试使用 sudo
                if auto_sudo and "Permission denied" in result.stderr:
                    print("权限不足，使用 sudo 创建虚拟环境...")
                    cmd = ['sudo', sys.executable, '-m', 'venv', str(self.venv_path)]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    if result.returncode == 0:
                        user = getpass.getuser()
                        subprocess.run(['sudo', 'chown', '-R', user, str(self.venv_path)], check=False)
                        print(f"虚拟环境创建成功: {self.venv_path}")
                        return True
                
                print(f"创建失败: {result.stderr}")
                return False
            
            print(f"虚拟环境创建成功: {self.venv_path}")
            return True
            
        except Exception as e:
            print(f"创建虚拟环境失败: {e}")
            return False
    
    def delete(self, auto_sudo: bool = True) -> bool:
        """删除虚拟环境"""
        if not self.exists():
            return True
        
        try:
            subprocess.run(['rm', '-rf', str(self.venv_path)], check=True)
            print(f"已删除虚拟环境: {self.venv_path}")
            return True
        except PermissionError:
            if auto_sudo and sys.platform != 'win32':
                try:
                    subprocess.run(['sudo', 'rm', '-rf', str(self.venv_path)], check=True)
                    print(f"已删除虚拟环境（使用 sudo）: {self.venv_path}")
                    return True
                except Exception as e:
                    print(f"删除失败: {e}")
                    return False
            print(f"删除失败: 权限不足")
            return False