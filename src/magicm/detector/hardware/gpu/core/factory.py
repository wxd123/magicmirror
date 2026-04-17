from typing import List, Optional
from .base import BaseGPUDetector, DetectionResult, GPUInfo
from ..vendor.nvidia import NVIDIADetector
from ..vendor.amd import AMDDetector
from ..vendor.intel import IntelDetector
from ..vendor.huawei import HuaweiDetector
from ..vendor.utils import extract_gpu_name, run_cmd_safe, get_gpu_memory, get_gpu_specs


class GPUDetectorFactory:
    """GPU检测器工厂"""
    
    def __init__(self):
        self._detectors = [
            NVIDIADetector(),
            AMDDetector(),
            IntelDetector(),
            HuaweiDetector(),
        ]
    
    def get_detector(self, lspci_line: str, gpu_name: str) -> Optional[BaseGPUDetector]:
        """根据lspci行获取合适的检测器"""
        for detector in self._detectors:
            if detector.supports_vendor(lspci_line, gpu_name):
                return detector
        return None
    
    def detect_all(self) -> DetectionResult:
        """检测所有GPU"""
        result = DetectionResult()
        
        # 获取lspci输出
        rc, out, _ = run_cmd_safe('lspci | grep -E "VGA|3D|Display"')
        if rc != 0 or not out:
            return result
        
        lines = out.strip().split('\n')
        
        for line in lines:
            if not line.strip():
                continue
            
            # 提取GPU名称
            gpu_name = extract_gpu_name(line)
            if not gpu_name:
                gpu_name = line.strip()
            
            # 获取检测器
            detector = self.get_detector(line, gpu_name)
            if not detector:
                continue
            
            # 检测GPU信息
            gpu_info = detector.detect_from_lspci(line, gpu_name)
            if not gpu_info:
                continue
            
            # 获取显存和规格
            gpu_info.memory_gb = get_gpu_memory(gpu_name, line)
            gpu_info.specs = get_gpu_specs(gpu_name)
            
            # 增强信息
            gpu_info = detector.enhance_gpu_info(gpu_info)
            
            # 分类存储
            result.all_gpus.append(gpu_info)
            if gpu_info.gpu_type.value == 'discrete':
                if not result.discrete_gpu:  # 只保留第一个离散GPU
                    result.discrete_gpu = gpu_info
            elif gpu_info.gpu_type.value == 'integrated':
                if not result.integrated_gpu:  # 只保留第一个集成GPU
                    result.integrated_gpu = gpu_info
        
        result.gpu_present = len(result.all_gpus) > 0
        return result