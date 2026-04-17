#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linux 系统检测模块
"""

import subprocess
import platform
from pathlib import Path


def detect():
    """检测 Linux 系统信息"""
    info = {'name': 'Linux', 'pretty_name': 'Linux'}
    
    try:
        # 方法1: 使用 lsb_release
        result = subprocess.run(['lsb_release', '-ds'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            pretty_name = result.stdout.strip().strip('"')
            info['pretty_name'] = pretty_name
            # 提取简短名称
            if 'Ubuntu' in pretty_name:
                info['name'] = 'Ubuntu'
            elif 'Debian' in pretty_name:
                info['name'] = 'Debian'
            elif 'CentOS' in pretty_name or 'CentOS' in pretty_name:
                info['name'] = 'CentOS'
            elif 'Fedora' in pretty_name:
                info['name'] = 'Fedora'
            else:
                info['name'] = pretty_name.split()[0] if pretty_name.split() else 'Linux'
            return info
    except:
        pass
    
    try:
        # 方法2: 读取 /etc/os-release
        os_release_path = Path('/etc/os-release')
        if os_release_path.exists():
            with open(os_release_path, 'r') as f:
                for line in f:
                    if line.startswith('NAME='):
                        name = line.split('=', 1)[1].strip().strip('"')
                        info['name'] = name
                    elif line.startswith('PRETTY_NAME='):
                        pretty_name = line.split('=', 1)[1].strip().strip('"')
                        info['pretty_name'] = pretty_name
    except:
        pass
    
    # 方法3: 回退到 platform
    if info['name'] == 'Linux' or info['pretty_name'] == 'Linux':
        info['name'] = f"Linux {platform.release()}"
        info['pretty_name'] = info['name']
    
    return info