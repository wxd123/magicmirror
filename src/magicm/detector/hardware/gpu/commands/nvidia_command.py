from typing import List, Dict, Any, Optional
import re
import math
import subprocess
from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs


class NVIDIACommand(GPUDetectionCommand):
    """NVIDIA GPU检测命令"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.NVIDIA
    
    def get_priority(self) -> int:
        return 10
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行NVIDIA GPU检测"""
        gpus = []
        
        # 检查是否有nvidia-smi
        rc, _, _ = run_cmd_safe('which nvidia-smi 2>/dev/null')
        if rc != 0:
            return gpus
        
        # 获取GPU列表
        rc, out, _ = run_cmd_safe('nvidia-smi --query-gpu=name,memory.total --format=csv,noheader')
        if rc != 0 or not out:
            return gpus
        
        for line in out.strip().split('\n'):
            if not line.strip():
                continue
            
            parts = line.split(',')
            name = parts[0].strip()
            memory_str = parts[1].strip() if len(parts) > 1 else None
            
            gpu = GPUInfo(
                name=name,
                vendor=GPUVendor.NVIDIA,
                gpu_type=GPUType.DISCRETE,
                memory_gb=self._parse_memory(memory_str)
            )
            
            # 获取驱动版本
            rc2, out2, _ = run_cmd_safe('nvidia-smi --query-gpu=driver_version --format=csv,noheader')
            if rc2 == 0 and out2:
                gpu.driver_version = out2.strip().split('\n')[0]
            
            # 获取CUDA版本
            rc3, out3, _ = run_cmd_safe('nvidia-smi --query-gpu=cuda_version --format=csv,noheader')
            if rc3 == 0 and out3:
                cuda_ver = out3.strip().split('\n')[0]
                if cuda_ver and cuda_ver != '[Not Supported]':
                    gpu.cuda_version = cuda_ver
            
            # 获取规格
            gpu.specs = get_gpu_specs(name)
            
            gpus.append(gpu)
        
        return gpus
    
    def _parse_memory(self, memory_str: str) -> Optional[int]:
        """解析显存大小"""
        if not memory_str:
            return None
        try:
            match = re.search(r'(\d+)\s*MiB', memory_str)
            if match:
                memory_mb = int(match.group(1))
                return math.ceil(memory_mb / 1024)
        except:
            pass
        return None
