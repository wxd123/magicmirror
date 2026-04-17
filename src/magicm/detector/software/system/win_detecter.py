#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows 系统检测模块
"""

import subprocess
import platform


def detect():
    """检测 Windows 系统信息"""
    info = {'name': 'Windows', 'pretty_name': 'Windows'}
    
    try:
        # 方法1: 使用 wmic
        result = subprocess.run(['wmic', 'os', 'get', 'Caption'], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                caption = lines[1].strip()
                if caption:
                    info['pretty_name'] = caption
                    if '11' in caption:
                        info['name'] = 'Windows 11'
                    elif '10' in caption:
                        info['name'] = 'Windows 10'
                    else:
                        info['name'] = 'Windows'
                    return info
    except:
        pass
    
    try:
        # 方法2: 使用 PowerShell
        result = subprocess.run(['powershell', '(Get-WmiObject Win32_OperatingSystem).Caption'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            caption = result.stdout.strip()
            info['pretty_name'] = caption
            if '11' in caption:
                info['name'] = 'Windows 11'
            elif '10' in caption:
                info['name'] = 'Windows 10'
            else:
                info['name'] = 'Windows'
            return info
    except:
        pass
    
    # 方法3: 回退到 platform
    release = platform.release()
    info['name'] = f"Windows {release}"
    info['pretty_name'] = info['name']
    
    return info