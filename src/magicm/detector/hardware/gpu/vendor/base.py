from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from enum import Enum


class GPUVendor(Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    INTEL = "intel"
    HUAWEI = "huawei"
    UNKNOWN = "unknown"


class GPUType(Enum):
    DISCRETE = "discrete"
    INTEGRATED = "integrated"
    VIRTUAL = "virtual"
    UNKNOWN = "unknown"


@dataclass
class GPUInfo:
    """GPU信息数据类"""
    name: str
    vendor: GPUVendor
    gpu_type: GPUType
    memory_gb: Optional[int] = None
    driver_version: Optional[str] = None
    cuda_version: Optional[str] = None
    rocm_version: Optional[str] = None
    ascend_version: Optional[str] = None
    nvlink: Optional[Dict[str, Any]] = None
    specs: Optional[Dict[str, Any]] = None
    raw_line: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        result = {
            'name': self.name,
            'vendor': self.vendor.value if self.vendor else None,
            'type': self.gpu_type.value if self.gpu_type else None,
            'memory_gb': self.memory_gb,
            'driver_version': self.driver_version,
            'cuda_version': self.cuda_version,
            'rocm_version': self.rocm_version,
            'ascend_version': self.ascend_version,
            'nvlink': self.nvlink,
            'specs': self.specs,
            'raw': self.raw_line
        }
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class DetectionResult:
    """检测结果数据类"""
    gpu_present: bool = False
    discrete_gpu: Optional[GPUInfo] = None
    integrated_gpu: Optional[GPUInfo] = None
    all_gpus: List[GPUInfo] = field(default_factory=list)
    
    @property
    def main_gpu(self) -> Optional[GPUInfo]:
        """获取主GPU（优先离散，其次集成）"""
        return self.discrete_gpu or self.integrated_gpu
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典（兼容原有格式）"""
        main = self.main_gpu
        return {
            'gpu_present': self.gpu_present,
            'discrete_gpu': self.discrete_gpu.name if self.discrete_gpu else None,
            'integrated_gpu': self.integrated_gpu.name if self.integrated_gpu else None,
            'all_gpus': [gpu.to_dict() for gpu in self.all_gpus],
            'gpu_name': main.name if main else None,
            'driver_version': main.driver_version if main else None,
            'cuda_version': main.cuda_version if main else None,
            'rocm_version': main.rocm_version if main else None,
            'ascend_version': main.ascend_version if main else None,
            'nvlink': main.nvlink if main else None,
            'specs': main.specs if main else None,
        }


class BaseGPUDetector(ABC):
    """GPU检测器基类"""
    
    @property
    @abstractmethod
    def vendor(self) -> GPUVendor:
        """返回检测器支持的厂商"""
        pass
    
    @abstractmethod
    def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
        """从lspci行检测GPU信息"""
        pass
    
    @abstractmethod
    def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
        """检测驱动版本"""
        pass
    
    def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
        """增强GPU信息（填充额外字段）"""
        gpu_info.driver_version = self.detect_driver_version(gpu_info)
        return gpu_info
    
    def supports_vendor(self, line: str, name: str) -> bool:
        """判断是否支持该厂商的GPU"""
        line_lower = line.lower()
        name_lower = name.lower()
        return self.vendor.value in line_lower or self.vendor.value in name_lower