#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/detector/software/system/mac_detecter.py
"""
macOS 系统检测模块
"""

import platform
import subprocess


def detect():
    """检测 macOS 系统信息"""
    
    # 获取内核版本 (Darwin)
    release_str = platform.release()
    # Darwin 版本与 macOS 版本的对应关系
    # Darwin 24.x -> macOS 15.x (Sequoia)
    # Darwin 23.x -> macOS 14.x (Sonoma)
    # Darwin 22.x -> macOS 13.x (Ventura)
    # Darwin 21.x -> macOS 12.x (Monterey)
    # Darwin 20.x -> macOS 11.x (Big Sur)
    
    darwin_version = release_str.split('.')[0] if release_str else "0"
    
    # 获取 macOS 版本信息
    mac_version = platform.mac_ver()[0]
    if not mac_version:
        # 尝试使用 sw_vers 命令
        try:
            result = subprocess.run(['sw_vers', '-productVersion'], 
                                   capture_output=True, text=True)
            if result.returncode == 0:
                mac_version = result.stdout.strip()
        except Exception:
            mac_version = ""
    
    # 解析版本号
    version_parts = mac_version.split('.') if mac_version else ["0", "0", "0"]
    major = version_parts[0] if len(version_parts) > 0 else "0"
    minor = version_parts[1] if len(version_parts) > 1 else "0"
    patch = version_parts[2] if len(version_parts) > 2 else "0"
    
    # macOS 版本名称映射
    version_names = {
        "15": "Sequoia",
        "14": "Sonoma", 
        "13": "Ventura",
        "12": "Monterey",
        "11": "Big Sur",
        "10.15": "Catalina",
        "10.14": "Mojave",
        "10.13": "High Sierra",
    }
    
    version_key = f"{major}" if int(major) >= 11 else f"{major}.{minor}"
    version_name = version_names.get(version_key, "")
    
    # 构建完整名称
    if version_name:
        pretty_name = f"macOS {major}.{minor} {version_name}"
    elif mac_version:
        pretty_name = f"macOS {mac_version}"
    else:
        pretty_name = f"macOS {darwin_version} (Darwin)"
    
    return {
        "platform": "darwin",
        "platform_name": "macOS",
        "distribution": {
            "name": "macOS",
            "version": mac_version or darwin_version,
            "pretty_name": pretty_name
        },
        "kernel": {
            "name": "Darwin",
            "version": darwin_version,
            "build": release_str,
            "pretty_version": release_str
        },
        "compatibility": {
            "key": darwin_version,      # macOS 驱动判断用 Darwin 版本
            "raw": release_str
        }
    }