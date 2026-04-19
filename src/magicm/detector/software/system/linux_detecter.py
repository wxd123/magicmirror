#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/detector/software/system/linux_detecter.py
"""
Linux 系统检测模块
支持: Ubuntu、Debian、CentOS、RHEL、Fedora、统信UOS、银河麒麟等
"""

import platform
import re
from pathlib import Path


def detect():
    """检测 Linux 系统信息"""
    
    # ========== 1. 内核版本信息 ==========
    release_str = platform.release()
    match = re.match(r'(\d+)\.(\d+)\.(\d+)', release_str)
    
    if match:
        major = match.group(1)
        minor = match.group(2)
        build = match.group(3)
        kernel_version = f"{major}.{minor}.{build}"
        # 提取 build 后缀（如 -generic, -amd64 等）
        build_suffix = release_str.split(f"{kernel_version}")[-1].lstrip('-')
    else:
        parts = release_str.split('.')
        major = parts[0] if len(parts) > 0 else "0"
        minor = parts[1] if len(parts) > 1 else "0"
        build = parts[2].split('-')[0] if len(parts) > 2 else "0"
        kernel_version = f"{major}.{minor}.{build}"
        build_suffix = ""
    
    # ========== 2. 发行版信息 ==========
    distro_info = get_distro_info()
    
    # ========== 3. 返回统一格式 ==========
    return {
        "platform": "linux",
        "platform_name": "Linux",
        "distribution": {
            "name": distro_info["name"],
            "version": distro_info["version"],
            "pretty_name": distro_info["pretty_name"]
        },
        "kernel": {
            "name": "Linux",
            "version": kernel_version,
            "build": build_suffix,
            "pretty_version": release_str
        },
        "compatibility": {
            "key": kernel_version,
            "raw": release_str
        }
    }


def get_distro_info():
    """获取 Linux 发行版信息"""
    
    # 默认值
    info = {
        "name": "Linux",
        "version": "",
        "pretty_name": f"Linux {platform.release()}"
    }
    
    # 读取 /etc/os-release
    os_release_paths = ['/etc/os-release', '/usr/lib/os-release']
    
    for path in os_release_paths:
        if Path(path).exists():
            try:
                with open(path, 'r') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('NAME='):
                            name = line.split('=', 1)[1].strip('"').strip("'")
                            info["name"] = name
                        elif line.startswith('VERSION_ID='):
                            info["version"] = line.split('=', 1)[1].strip('"').strip("'")
                        elif line.startswith('PRETTY_NAME='):
                            info["pretty_name"] = line.split('=', 1)[1].strip('"').strip("'")
                break
            except Exception:
                pass
    
    # 美化国产系统名称
    china_os_map = {
        'uos': '统信UOS',
        'kylin': '银河麒麟',
        'neokylin': '中标麒麟',
        'openEuler': 'OpenEuler',
        'kylinsec': '麒麟信安'
    }
    
    for os_id, os_name in china_os_map.items():
        if info["name"].lower() == os_id or info["name"].lower().startswith(os_id):
            info["name"] = os_name
            break
    
    return info