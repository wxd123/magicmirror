# magicm/detector/hardware/cpu/cpu_detecter.py

import os
import sys
import platform

from .win_detecter import detecter as windows_detecter
from .linux_detecter import detecter as linux_detecter
from .mac_detecter import detect as mac_detecter
from .cpu_model import cpu_model as modeler

def cpu_detected():
    """检测CPU信息 - 增强版"""
    info = {'model': '未知', 'cores': os.cpu_count() or '未知', 'simple_model': '未知'}
    
    try:
        if sys.platform == 'win32':
            # Windows系统 - 使用多种方法获取CPU信息
            info = windows_detecter()
        
        elif sys.platform.startswith('linux'):
            # Linux系统
            info = linux_detecter()
        
        elif sys.platform == 'darwin':
            # macOS系统
            info = mac_detecter()
        
        # 如果还是没有获取到，使用platform模块
        if info['model'] == '未知':
            info['model'] = platform.processor() or '未知'
            info['simple_model'] = modeler(info['model'])
    
    except Exception as e:
        print(f"CPU检测出错: {e}")
    
    # 确保核心数是整数
    try:
        info['cores'] = str(os.cpu_count())
    except:
        info['cores'] = '未知'
    
    return info






def get_cpu_summary():
    """获取CPU摘要信息"""
    info = cpu_detected()
    
    if info['simple_model'] != '未知':
        cpu_text = info['simple_model']
    else:
        cpu_text = info['model']
    
    # 添加核心数
    if info['cores'] != '未知':
        cpu_text += f" ({info['cores']}核)"
    
    return cpu_text