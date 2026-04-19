#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/detector/software/system/win_detecter.py
"""
Windows 系统检测模块
"""

import platform
import sys


def detect():
    """检测 Windows 系统信息"""
    
    # Windows 版本映射
    version_map = {
        (10, 0, 22000): "11",
        (10, 0, 22621): "11",
        (10, 0, 22631): "11",
        (10, 0, 26100): "11",
        (10, 0, 19045): "10",
        (10, 0, 19044): "10",
        (10, 0, 19043): "10",
        (10, 0, 19042): "10",
        (10, 0, 18363): "10",
        (10, 0, 17763): "10",
        (6, 3, 9600): "8.1",
        (6, 2, 9200): "8",
        (6, 1, 7601): "7",
    }
    
    # 获取版本信息
    version_info = sys.getwindowsversion()
    major = version_info.major
    minor = version_info.minor
    build = version_info.build
    
    # 确定 Windows 版本名称
    win_version = version_map.get((major, minor, build), f"{major}.{minor}")
    if win_version in ["11", "10"]:
        # 尝试获取更精确的版本
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                 r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
            product_name = winreg.QueryValueEx(key, "ProductName")[0]
            if "Windows 11" in product_name:
                win_version = "11"
            elif "Windows 10" in product_name:
                win_version = "10"
            winreg.CloseKey(key)
        except Exception:
            pass
    
    # 构建完整名称
    pretty_name = f"Windows {win_version}"
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                             r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        edition = winreg.QueryValueEx(key, "EditionID")[0]
        if edition:
            pretty_name = f"Windows {win_version} {edition}"
        winreg.CloseKey(key)
    except Exception:
        pass
    
    return {
        "platform": "windows",
        "platform_name": "Windows",
        "distribution": {
            "name": "Windows",
            "version": win_version,
            "pretty_name": pretty_name
        },
        "kernel": {
            "name": "NT",
            "version": f"{major}.{minor}",
            "build": str(build),
            "pretty_version": f"{major}.{minor}.{build}"
        },
        "compatibility": {
            "key": str(build),      # Windows 驱动判断用 Build 号
            "raw": f"{major}.{minor}.{build}"
        }
    }