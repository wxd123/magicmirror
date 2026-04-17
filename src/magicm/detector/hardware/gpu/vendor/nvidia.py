from typing import Optional, Dict, Any
from .base import BaseGPUDetector, GPUVendor, GPUInfo, GPUType
from .utils import run_cmd_safe


class NVIDIADetector(BaseGPUDetector):
    """NVIDIA GPU检测器"""
    
    @property
    def vendor(self) -> GPUVendor:
        return GPUVendor.NVIDIA
    
    def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
        """检测NVIDIA GPU"""
        return GPUInfo(
            name=gpu_name,
            vendor=self.vendor,
            gpu_type=GPUType.DISCRETE,
            raw_line=lspci_line
        )
    
    def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
        """检测NVIDIA驱动版本"""
        rc, out, _ = run_cmd_safe('nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null')
        if rc == 0 and out:
            return out.split('\n')[0].strip()
        return None
    
    def detect_cuda_version(self) -> Optional[str]:
        """检测CUDA版本"""
        # 从nvidia-smi获取
        rc, out, _ = run_cmd_safe('nvidia-smi --query-gpu=cuda_version --format=csv,noheader 2>/dev/null')
        if rc == 0 and out:
            cuda_ver = out.strip().split('\n')[0]
            if cuda_ver and cuda_ver != '[Not Supported]':
                return cuda_ver
        
        # 从nvcc获取
        rc, out, _ = run_cmd_safe('nvcc --version 2>/dev/null | grep "release"')
        if rc == 0 and out:
            import re
            match = re.search(r'release\s+([0-9.]+)', out)
            if match:
                return match.group(1)
        
        return None
    
    def detect_nvlink(self) -> Dict[str, Any]:
        """检测NVLink状态"""
        nvlink_info = {
            "supported": False,
            "link_count": 0,
            "bandwidth_gb_s": 0
        }
        
        rc, out, _ = run_cmd_safe('nvidia-smi nvlink --status 2>/dev/null')
        if rc == 0 and out:
            import re
            nvlink_info["supported"] = True
            link_matches = re.findall(r'Link (\d+)', out)
            nvlink_info["link_count"] = len(set(link_matches))
            if nvlink_info["link_count"] > 0:
                nvlink_info["bandwidth_gb_s"] = nvlink_info["link_count"] * 50
        
        return nvlink_info
    
    def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
        """增强NVIDIA GPU信息"""
        gpu_info = super().enhance_gpu_info(gpu_info)
        gpu_info.cuda_version = self.detect_cuda_version()
        gpu_info.nvlink = self.detect_nvlink()
        return gpu_info