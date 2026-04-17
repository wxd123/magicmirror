# magicm/detector/hardware/mem/mem_detecter.py

import psutil
import math

# 常见内存规格（GB）
MEMORY_SPECS = [2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]

def match_memory_spec(total_bytes):
    """
    根据实际内存大小，匹配最接近的标准规格
    512GB 及以下：向上匹配到标准规格
    512GB 以上：返回 512（表示 512GB 或更多）
    """
    total_gb = total_bytes / (1024**3)
    
    # 超过 512GB，返回 512（由调用方决定显示文案）
    if total_gb > 512:
        return 512
    
    # 512GB 及以下，向上匹配到标准规格
    for spec in sorted(MEMORY_SPECS):
        if spec >= total_gb:
            return spec
    
    return math.ceil(total_gb)

def mem_detected():
    """检测内存信息 - 使用规格匹配算法"""
    info = {
        'total_mb': 0,
        'total_gb': 0,
        'total_str': '未知',
        'available_mb': 0,
        'available_str': '未知'
    }
    
    try:
        mem = psutil.virtual_memory()
        
        total_bytes = mem.total
        available_bytes = mem.available
        
        # 规格匹配
        total_gb = match_memory_spec(total_bytes)
        available_gb = math.ceil(available_bytes / (1024**3))

        info['total_gb'] = total_gb
        info['total_mb'] = total_gb * 1024
        
        # 特殊处理：超过 512GB 时的显示文案
        actual_gb = total_bytes / (1024**3)
        if actual_gb > 512:
            info['total_str'] = f"{total_gb} GB 或更多"  # 显示 "512 GB 或更多"
        else:
            info['total_str'] = f"{total_gb} GB"
            
        info['available_mb'] = available_gb * 1024
        info['available_str'] = f"{available_gb} GB"
        
    except Exception as e:
        print(f"内存检测出错: {e}")
    
    return info