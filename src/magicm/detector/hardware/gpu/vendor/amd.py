from typing import Optional
import re
from .base import BaseGPUDetector, GPUVendor, GPUInfo, GPUType
from .utils import run_cmd_safe


class AMDDetector(BaseGPUDetector):
    """AMD GPU检测器"""
    
    @property
    def vendor(self) -> GPUVendor:
        return GPUVendor.AMD
    
    def _is_integrated(self, line: str) -> bool:
        """判断是否为集成显卡"""
        line_lower = line.lower()
        integrated_keywords = ['radeon graphics', 'vega', 'renoir', 'cezanne']
        return any(keyword in line_lower for keyword in integrated_keywords)
    
    def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
        """检测AMD GPU"""
        gpu_type = GPUType.INTEGRATED if self._is_integrated(lspci_line) else GPUType.DISCRETE
        
        return GPUInfo(
            name=gpu_name,
            vendor=self.vendor,
            gpu_type=gpu_type,
            raw_line=lspci_line
        )
    
    def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
        """检测AMD驱动版本"""
        rc, out, _ = run_cmd_safe('modinfo amdgpu 2>/dev/null | grep "^version:"')
        if rc == 0 and out:
            match = re.search(r'version:\s*(.+)', out)
            if match:
                return match.group(1).strip()
        return None
    
    def detect_rocm_version(self) -> Optional[str]:
        """检测ROCm版本"""
        rc, out, _ = run_cmd_safe('rocm-smi --version 2>/dev/null')
        if rc == 0 and out:
            match = re.search(r'([0-9]+\.[0-9]+(?:\.[0-9]+)?)', out)
            if match:
                return match.group(1)
        return None
    
    def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
        """增强AMD GPU信息"""
        gpu_info = super().enhance_gpu_info(gpu_info)
        gpu_info.rocm_version = self.detect_rocm_version()
        return gpu_info