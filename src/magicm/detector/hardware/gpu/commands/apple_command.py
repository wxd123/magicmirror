# detector/hardware/gpu/commands/apple_command.py

from typing import List, Dict, Any
from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs

class AppleCommand(GPUDetectionCommand):
    """Apple Silicon GPU检测命令 - 新增厂商示例"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.APPLE
    
    def get_priority(self) -> int:
        return 60
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行Apple Silicon GPU检测"""
        gpus = []
        
        system_type = context.get('system_type')
        
        if system_type.value == 'macos':
            rc, out, _ = run_cmd_safe('system_profiler SPDisplaysDataType | grep "Chipset Model"')
            if rc == 0 and out:
                for line in out.split('\n'):
                    if 'Chipset Model' in line:
                        name = line.split(':')[-1].strip()
                        if 'M' in name:  # Apple M1/M2/M3
                            gpu = GPUInfo(
                                name=name,
                                vendor=GPUVendor.APPLE,
                                gpu_type=GPUType.INTEGRATED
                            )
                            gpus.append(gpu)
        
        return gpus