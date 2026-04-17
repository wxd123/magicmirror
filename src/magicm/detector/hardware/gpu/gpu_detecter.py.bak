# magicm/detector/hardware/gpu/gpu_detecter.py
import sys
import re
from magicm.utils.util import run_cmd
from .system.linux_detecter import detect as linux_func
from .system.win_detecter import detect as win_func
from .system.mac_detecter import detect as mac_func

def gpu_detected():
    """检测GPU信息（独立显卡和集成显卡）"""
    info = {
        'gpu_present': False,
        'discrete_gpu': None,  # 独立显卡
        'integrated_gpu': None,  # 集成显卡
        'driver_version': None,
        'cuda_supported_by_driver': None,
        'gpu_name': None,
        'all_gpus': []  # 所有GPU列表
    }
    
    try:
        if sys.platform == 'win32':
            # Windows系统 - 使用多种方法检测所有GPU
            result = win_func()
            if result and isinstance(result, dict):
                info.update(result)
        elif sys.platform.startswith('linux'):
            # Linux系统
            result = linux_func()
            if result and isinstance(result, dict):
                info.update(result)
        elif sys.platform == 'darwin':
            # macOS系统
            result = mac_func()
            if result and isinstance(result, dict):
                info.update(result)
    except Exception as e:
        print(f"GPU检测出错: {e}")
    
    # 确保 all_gpus 是列表
    if 'all_gpus' not in info or not isinstance(info['all_gpus'], list):
        info['all_gpus'] = []
    
    # 设置gpu_present标志
    info['gpu_present'] = len(info['all_gpus']) > 0
    
    # 为了兼容旧代码，设置gpu_name为第一个GPU
    if info['all_gpus'] and len(info['all_gpus']) > 0:
        first_gpu = info['all_gpus'][0]
        info['gpu_name'] = first_gpu.get('name', '未知')
        
        # 安全地获取 GPU 类型，避免 KeyError
        gpu_type = first_gpu.get('type', '')
        
        if gpu_type == 'discrete':
            info['discrete_gpu'] = first_gpu.get('name')
        elif gpu_type == 'integrated':
            info['integrated_gpu'] = first_gpu.get('name')
        else:
            # 如果没有 type 字段，尝试根据名称判断
            name_lower = first_gpu.get('name', '').lower()
            if any(integrated_keyword in name_lower for integrated_keyword in 
                   ['intel', 'uhd', 'iris', 'radeon graphics', 'apple', 'm1', 'm2', 'm3']):
                info['integrated_gpu'] = first_gpu.get('name')
            else:
                info['discrete_gpu'] = first_gpu.get('name')
    
    return info


def get_gpu_summary():
    """获取GPU摘要信息"""
    info = gpu_detected()
    
    if info.get('discrete_gpu') and info.get('integrated_gpu'):
        # 同时有独立和集成显卡
        return f"独立: {info['discrete_gpu']} / 集成: {info['integrated_gpu']}"
    elif info.get('discrete_gpu'):
        # 只有独立显卡
        return info['discrete_gpu']
    elif info.get('integrated_gpu'):
        # 只有集成显卡
        return f"集成显卡: {info['integrated_gpu']}"
    elif info.get('all_gpus') and len(info['all_gpus']) > 0:
        # 有其他显卡
        return info['all_gpus'][0].get('name', '未检测到显卡')
    else:
        return "未检测到显卡"
    """获取GPU摘要信息"""
    info = gpu_detected()
    
    if info['discrete_gpu'] and info['integrated_gpu']:
        # 同时有独立和集成显卡
        return f"独立: {info['discrete_gpu']} / 集成: {info['integrated_gpu']}"
    elif info['discrete_gpu']:
        # 只有独立显卡
        return info['discrete_gpu']
    elif info['integrated_gpu']:
        # 只有集成显卡
        return f"集成显卡: {info['integrated_gpu']}"
    elif info['all_gpus']:
        # 有其他显卡
        return info['all_gpus'][0]['name']
    else:
        return "未检测到显卡"