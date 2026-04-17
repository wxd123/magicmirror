# detector/hardware/gpu/core/base.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class SystemType(Enum):
    """系统类型 - 扩展少"""
    LINUX = "linux"
    WINDOWS = "windows"
    MACOS = "macos"
    UNKNOWN = "unknown"


class GPUVendor(Enum):
    """GPU厂商 - 扩展多"""
    NVIDIA = "nvidia"
    AMD = "amd"
    INTEL = "intel"
    HUAWEI = "huawei"
    QUALCOMM = "qualcomm"
    APPLE = "apple"
    UNKNOWN = "unknown"


class GPUType(Enum):
    """GPU类型"""
    DISCRETE = "discrete"
    INTEGRATED = "integrated"
    VIRTUAL = "virtual"
    UNKNOWN = "unknown"


@dataclass
class GPUInfo:
    """GPU信息数据类 - 兼容原有API"""
    name: str
    vendor: Optional[GPUVendor] = None
    gpu_type: Optional[GPUType] = None
    memory_gb: Optional[int] = None
    driver_version: Optional[str] = None
    cuda_version: Optional[str] = None
    rocm_version: Optional[str] = None
    ascend_version: Optional[str] = None
    nvlink: Optional[Dict[str, Any]] = None
    specs: Optional[Dict[str, Any]] = None
    raw_line: Optional[str] = None
    system: Optional[SystemType] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典 - 兼容原有格式"""
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
            'raw': self.raw_line,
        }
        return {k: v for k, v in result.items() if v is not None}


@dataclass
class DetectionResult:
    """检测结果数据类 - 兼容原有API"""
    gpu_present: bool = False
    discrete_gpu: Optional[GPUInfo] = None
    integrated_gpu: Optional[GPUInfo] = None
    all_gpus: List[GPUInfo] = field(default_factory=list)
    gpu_name: Optional[str] = None
    driver_version: Optional[str] = None
    cuda_version: Optional[str] = None
    rocm_version: Optional[str] = None
    ascend_version: Optional[str] = None
    nvlink: Optional[Dict[str, Any]] = None
    specs: Optional[Dict[str, Any]] = None
    
    @property
    def main_gpu(self) -> Optional[GPUInfo]:
        """获取主GPU（优先离散，其次集成）"""
        return self.discrete_gpu or self.integrated_gpu
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典 - 兼容原有格式"""
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


# 命令接口
class GPUDetectionCommand(ABC):
    """GPU检测命令接口"""
    
    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行检测命令"""
        pass
    
    @abstractmethod
    def get_vendor(self) -> GPUVendor:
        """返回厂商类型"""
        pass
    
    def get_priority(self) -> int:
        """优先级（数值越小越先执行）"""
        return 100


# 平台适配器接口
class PlatformAdapter(ABC):
    """平台适配器接口"""
    
    @abstractmethod
    def get_system_type(self) -> SystemType:
        """获取系统类型"""
        pass
    
    @abstractmethod
    def run_command(self, cmd: str) -> tuple:
        """执行命令"""
        pass
    
    @abstractmethod
    def get_gpu_list(self) -> List[Dict[str, Any]]:
        """获取GPU原始列表"""
        pass