from typing import Optional
from .base import BaseGPUDetector, GPUVendor, GPUInfo, GPUType
from .utils import run_cmd_safe


class IntelDetector(BaseGPUDetector):
    """Intel GPU检测器"""
    
    @property
    def vendor(self) -> GPUVendor:
        return GPUVendor.INTEL
    
    def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
        """检测Intel GPU"""
        return GPUInfo(
            name=gpu_name,
            vendor=self.vendor,
            gpu_type=GPUType.INTEGRATED,
            raw_line=lspci_line
        )
    
    def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
        """检测Intel驱动版本"""
        # Intel通常使用i915驱动
        rc, out, _ = run_cmd_safe('modinfo i915 2>/dev/null | grep "^version:"')
        if rc == 0 and out:
            import re
            match = re.search(r'version:\s*(.+)', out)
            if match:
                return match.group(1).strip()
        return None