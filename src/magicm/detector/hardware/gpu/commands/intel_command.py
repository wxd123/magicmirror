# detector/hardware/gpu/commands/intel_command.py

from typing import List, Dict, Any, Optional

from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs


class IntelCommand(GPUDetectionCommand):
    """Intel GPU检测命令"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.INTEL
    
    def get_priority(self) -> int:
        return 30
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行Intel GPU检测"""
        gpus = []
        
        system_type = context.get('system_type')
        
        if system_type.value == 'linux':
            rc, out, _ = run_cmd_safe('lspci | grep -i "VGA.*Intel"')
            if rc == 0 and out:
                for line in out.strip().split('\n'):
                    if not line.strip():
                        continue
                    
                    gpu = GPUInfo(
                        name=self._extract_name(line),
                        vendor=GPUVendor.INTEL,
                        gpu_type=GPUType.INTEGRATED,
                        raw_line=line
                    )
                    
                    # 获取驱动版本
                    rc2, out2, _ = run_cmd_safe('modinfo i915 | grep "^version:"')
                    if rc2 == 0 and out2:
                        gpu.driver_version = out2.split(':')[-1].strip()
                    
                    gpu.specs = get_gpu_specs(gpu.name)
                    gpus.append(gpu)
        
        return gpus
    
    def _extract_name(self, line: str) -> str:
        import re
        bracket_match = re.search(r'\[([^\]]+)\]', line)
        if bracket_match:
            return bracket_match.group(1).strip()
        return line.strip()
