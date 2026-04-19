# magicm/detector/software/system/sys_detecter.py

import sys
import platform
from .linux_detecter import detect as linux_detect
from .win_detecter import detect as windows_detect
from .mac_detecter import detect as mac_detect


def detect():
    """检测操作系统信息 - 统一接口"""
    
    try:
        if sys.platform == 'win32':
            # Windows系统
            try:
                return windows_detect()
            except Exception as e:
                print(f"Windows系统检测出错: {e}")
                return _fallback_windows()
        
        elif sys.platform.startswith('linux'):
            # Linux系统
            try:
                return linux_detect()
            except Exception as e:
                print(f"Linux系统检测出错: {e}")
                return _fallback_linux()
        
        elif sys.platform == 'darwin':
            # macOS系统
            try:
                return mac_detect()
            except Exception as e:
                print(f"Mac系统检测出错: {e}")
                return _fallback_macos()
        
        else:
            return _fallback_unknown()
    
    except Exception as e:
        print(f"系统检测出错: {e}")
        return _fallback_error()


def _fallback_windows():
    """Windows 降级返回"""
    return {
        "platform": "windows",
        "platform_name": "Windows",
        "distribution": {
            "name": "Windows",
            "version": "",
            "pretty_name": f"Windows {platform.release()}"
        },
        "kernel": {
            "name": "NT",
            "version": "",
            "build": "",
            "pretty_version": platform.release()
        },
        "compatibility": {
            "key": platform.release(),
            "raw": platform.release()
        }
    }


def _fallback_linux():
    """Linux 降级返回"""
    release_str = platform.release()
    return {
        "platform": "linux",
        "platform_name": "Linux",
        "distribution": {
            "name": "Linux",
            "version": "",
            "pretty_name": f"Linux {release_str}"
        },
        "kernel": {
            "name": "Linux",
            "version": release_str.split('.')[0] if release_str else "",
            "build": "",
            "pretty_version": release_str
        },
        "compatibility": {
            "key": release_str,
            "raw": release_str
        }
    }


def _fallback_macos():
    """macOS 降级返回"""
    return {
        "platform": "darwin",
        "platform_name": "macOS",
        "distribution": {
            "name": "macOS",
            "version": "",
            "pretty_name": f"macOS {platform.release()}"
        },
        "kernel": {
            "name": "Darwin",
            "version": platform.release(),
            "build": "",
            "pretty_version": platform.release()
        },
        "compatibility": {
            "key": platform.release(),
            "raw": platform.release()
        }
    }


def _fallback_unknown():
    """未知平台降级返回"""
    return {
        "platform": sys.platform,
        "platform_name": "Unknown",
        "distribution": {
            "name": "Unknown",
            "version": "",
            "pretty_name": f"{sys.platform} {platform.release()}"
        },
        "kernel": {
            "name": "Unknown",
            "version": "",
            "build": "",
            "pretty_version": platform.release()
        },
        "compatibility": {
            "key": platform.release(),
            "raw": platform.release()
        }
    }


def _fallback_error():
    """错误降级返回"""
    return {
        "platform": "error",
        "platform_name": "Error",
        "distribution": {
            "name": "未知",
            "version": "",
            "pretty_name": "未知系统"
        },
        "kernel": {
            "name": "Unknown",
            "version": "",
            "build": "",
            "pretty_version": ""
        },
        "compatibility": {
            "key": "",
            "raw": ""
        }
    }