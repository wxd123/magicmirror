from typing import Optional
import re
from .base import BaseGPUDetector, GPUVendor, GPUInfo, GPUType
from .utils import run_cmd_safe


class HuaweiDetector(BaseGPUDetector):
    """华为昇腾GPU检测器"""
    
    @property
    def vendor(self) -> GPUVendor:
        return GPUVendor.HUAWEI
    
    def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
        """检测华为昇腾GPU"""
        return GPUInfo(
            name=gpu_name,
            vendor=self.vendor,
            gpu_type=GPUType.DISCRETE,
            raw_line=lspci_line
        )
    
    def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
        """检测昇腾驱动版本"""
        rc, out, _ = run_cmd_safe('npu-smi info 2>/dev/null | grep "Driver Version"')
        if rc == 0 and out:
            match = re.search(r'([0-9]+\.[0-9]+\.[0-9]+)', out)
            if match:
                return match.group(1)
        return None
    
    def detect_ascend_version(self) -> Optional[str]:
        """检测CANN版本"""
        rc, out, _ = run_cmd_safe('npu-smi info 2>/dev/null | grep "Version"')
        if rc == 0 and out:
            match = re.search(r'([0-9]+\.[0-9]+\.[0-9]+)', out)
            if match:
                return match.group(1)
        return None
    
    def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
        """增强昇腾GPU信息"""
        gpu_info = super().enhance_gpu_info(gpu_info)
        gpu_info.ascend_version = self.detect_ascend_version()
        return gpu_info