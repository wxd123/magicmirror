# magicm/detector/software/system/sys_detecter.py

import sys
import platform
from .linux_detecter import detect as linux_detect
from .win_detecter import detect as windows_detect


def detect():
    """检测操作系统信息 - 增强版"""
    info = {'platform': '未知', 'name': '未知', 'pretty_name': '未知系统'}
    
    try:
        if sys.platform == 'win32':
            # Windows系统
            info['platform'] = 'win32'
            # 调用 Windows 检测器获取详细信息
            try:
                windows_info = windows_detect()
                info.update(windows_info)
            except Exception as e:
                print(f"Windows系统检测出错: {e}")
                info['name'] = f"Windows {platform.release()}"
                info['pretty_name'] = info['name']
        
        elif sys.platform.startswith('linux'):
            # Linux系统
            info['platform'] = 'linux'
            # 调用 Linux 检测器获取详细信息
            try:
                linux_info = linux_detect()
                info.update(linux_info)
            except Exception as e:
                print(f"Linux系统检测出错: {e}")
                info['name'] = f"Linux {platform.release()}"
                info['pretty_name'] = info['name']
        
        elif sys.platform == 'darwin':
            # macOS系统
            info['platform'] = 'darwin'
            info['name'] = f"macOS {platform.mac_ver()[0]}"
            info['pretty_name'] = info['name']
        
        else:
            info['platform'] = sys.platform
            info['name'] = f"{sys.platform} {platform.release()}"
            info['pretty_name'] = info['name']
    
    except Exception as e:
        print(f"系统检测出错: {e}")
        info = {'platform': '未知', 'name': '未知', 'pretty_name': '未知系统'}

    return info