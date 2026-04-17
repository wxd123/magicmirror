# detector/hardware/gpu/commands/qualcomm_command.py

from typing import List, Dict, Any, Optional
from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs

class QualcommCommand(GPUDetectionCommand):
    """高通Adreno GPU检测命令 - 新增厂商示例"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.QUALCOMM
    
    def get_priority(self) -> int:
        return 50
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行高通Adreno GPU检测"""
        gpus = []
        
        # Android/Linux embedded检测
        rc, out, _ = run_cmd_safe('dmesg | grep -i "adreno" 2>/dev/null')
        if rc == 0 and out:
            gpu = GPUInfo(
                name="Qualcomm Adreno GPU",
                vendor=GPUVendor.QUALCOMM,
                gpu_type=GPUType.INTEGRATED
            )
            gpus.append(gpu)
        
        return gpus
