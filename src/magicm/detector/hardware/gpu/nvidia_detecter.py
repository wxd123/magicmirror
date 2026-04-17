# magicm/detector/hardware/gpu/nvidia_detecter.py
import re
from magicm.utils.util import run_cmd
def nvidia_driver(output):
    """从nvidia-smi输出中提取驱动版本"""
    match = re.search(r'Driver Version:\s+(\S+)', output)
    return match.group(1) if match else None

def cuda_version(output):
    """从nvidia-smi输出中提取CUDA版本"""
    match = re.search(r'CUDA Version:\s+(\S+)', output)
    return match.group(1) if match else None

def nvidia_gpu_name(output):
    """从nvidia-smi输出中提取GPU名称"""
    lines = output.split('\n')
    for line in lines:
        if '|' in line and any(x in line for x in ['GeForce', 'Tesla', 'Quadro', 'RTX', 'GTX']):
            parts = line.split('|')
            for part in parts:
                if any(x in part for x in ['GeForce', 'Tesla', 'Quadro', 'RTX', 'GTX']):
                    return part.strip()
    
    # 备用方法
    rc, out, _ = run_cmd('nvidia-smi --query-gpu=name --format=csv,noheader')
    if rc == 0 and out:
        return out.strip()
    
    return None
