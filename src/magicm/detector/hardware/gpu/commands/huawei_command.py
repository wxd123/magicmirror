# detector/hardware/gpu/commands/huawei_command.py

from typing import List, Dict, Any, Optional
import re
from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs

class HuaweiCommand(GPUDetectionCommand):
    """华为昇腾GPU检测命令"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.HUAWEI
    
    def get_priority(self) -> int:
        return 40
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行华为昇腾GPU检测"""
        gpus = []
        
        # 检查是否有npu-smi
        rc, _, _ = run_cmd_safe('which npu-smi 2>/dev/null')
        if rc != 0:
            return gpus
        
        # 获取NPU信息
        rc, out, _ = run_cmd_safe('npu-smi info 2>/dev/null')
        if rc != 0 or not out:
            return gpus
        
        # 解析NPU名称
        for line in out.split('\n'):
            if 'Name' in line and ':' in line:
                name = line.split(':')[-1].strip()
                if name:
                    gpu = GPUInfo(
                        name=name,
                        vendor=GPUVendor.HUAWEI,
                        gpu_type=GPUType.DISCRETE
                    )
                    
                    # 获取驱动版本
                    for l in out.split('\n'):
                        if 'Driver Version' in l and ':' in l:
                            gpu.driver_version = l.split(':')[-1].strip()
                            break
                    
                    # 获取CANN版本
                    for l in out.split('\n'):
                        if 'Version' in l and ':' in l:
                            match = re.search(r'([0-9]+\.[0-9]+\.[0-9]+)', l)
                            if match:
                                gpu.ascend_version = match.group(1)
                                break
                    
                    gpu.specs = get_gpu_specs(name)
                    gpus.append(gpu)
                    break
        
        return gpus

