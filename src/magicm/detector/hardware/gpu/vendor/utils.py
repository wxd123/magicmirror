import re
import math
from typing import Optional, Dict, Any
from functools import lru_cache

# 导入原有的规格加载器
from magicm.utils.util import run_cmd as _run_cmd
from .specs_loader import GPUSpecsLoader


_specs_loader = None


def _get_specs_loader():
    global _specs_loader
    if _specs_loader is None:
        _specs_loader = GPUSpecsLoader()
    return _specs_loader


def run_cmd_safe(cmd: str, timeout: int = 5):
    """安全执行命令"""
    try:
        return _run_cmd(cmd)
    except Exception as e:
        return -1, "", str(e)


def extract_gpu_name(line: str) -> str:
    """从 lspci 输出中提取干净的 GPU 名称"""
    # 优先提取括号内的内容
    bracket_match = re.search(r'\[([^\]]+)\]', line)
    if bracket_match:
        return bracket_match.group(1).strip()
    
    # 提取控制器类型后的名称
    for controller in ['controller:', '3D controller:', 'Display controller:']:
        if controller in line:
            parts = line.split(controller, 1)
            if len(parts) > 1:
                name = parts[1].strip()
                name = re.sub(r'\([^)]*\)', '', name).strip()
                return name
    
    # 通用清理
    cleaned = re.sub(r'^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9a-f]\s+', '', line)
    cleaned = re.sub(r'(VGA compatible controller|3D controller|Display controller):\s*', '', cleaned)
    cleaned = re.sub(r'\([^)]*\)', '', cleaned)
    
    return cleaned.strip()


@lru_cache(maxsize=32)
def get_gpu_memory(gpu_name: str, gpu_raw_line: Optional[str] = None) -> Optional[int]:
    """获取 GPU 显存大小（GB）"""
    # 优先从规格表获取
    loader = _get_specs_loader()
    specs = loader.get_specs(gpu_name)
    if specs and specs.get('vram_gb'):
        return specs['vram_gb']
    
    # NVIDIA GPU
    if 'nvidia' in gpu_name.lower():
        rc, out, _ = run_cmd_safe('nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits 2>/dev/null')
        if rc == 0 and out and out.strip():
            memory_mb_str = out.strip().split('\n')[0].strip()
            if memory_mb_str and memory_mb_str.isdigit():
                memory_mb = int(memory_mb_str)
                return math.ceil(memory_mb / 1024)
    
    # AMD GPU - glxinfo
    rc, out, _ = run_cmd_safe('glxinfo 2>/dev/null | grep "Video memory"')
    if rc == 0 and out:
        match = re.search(r'(\d+)\s*MB', out)
        if match:
            return int(match.group(1)) // 1024
    
    # 通用方法 - sysfs
    try:
        import glob
        for card in glob.glob('/sys/class/drm/card[0-9]*/device/mem_info_vram_total'):
            try:
                with open(card, 'r') as f:
                    total_bytes = int(f.read().strip())
                    if total_bytes > 0:
                        return total_bytes // (1024 * 1024 * 1024)
            except (IOError, OSError, ValueError):
                continue
    except ImportError:
        pass
    
    return None


def get_gpu_specs(gpu_name: str) -> Optional[Dict[str, Any]]:
    """根据GPU名称获取完整规格"""
    loader = _get_specs_loader()
    return loader.get_specs(gpu_name)