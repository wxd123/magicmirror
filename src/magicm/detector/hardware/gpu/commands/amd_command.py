
# detector/hardware/gpu/commands/amd_command.py

from typing import List, Dict, Any, Optional
import re
import math
from ..core.base import GPUDetectionCommand, GPUInfo, GPUVendor, GPUType
from ..vendor.utils import run_cmd_safe, get_gpu_specs

class AMDCommand(GPUDetectionCommand):
    """AMD GPU检测命令"""
    
    def get_vendor(self) -> GPUVendor:
        return GPUVendor.AMD
    
    def get_priority(self) -> int:
        return 20
    
    def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
        """执行AMD GPU检测"""
        gpus = []
        
        # 获取平台信息
        platform = context.get('platform_adapter')
        system_type = context.get('system_type')
        
        if system_type.value == 'linux':
            gpus = self._detect_linux()
        elif system_type.value == 'windows':
            gpus = self._detect_windows()
        
        return gpus
    
    def _detect_linux(self) -> List[GPUInfo]:
        """Linux下检测AMD GPU"""
        gpus = []
        
        rc, out, _ = run_cmd_safe('lspci | grep -i "VGA.*AMD"')
        if rc != 0 or not out:
            return gpus
        
        for line in out.strip().split('\n'):
            if not line.strip():
                continue
            
            gpu = GPUInfo(
                name=self._extract_name(line),
                vendor=GPUVendor.AMD,
                gpu_type=self._determine_type(line),
                raw_line=line
            )
            
            # 获取驱动版本
            rc2, out2, _ = run_cmd_safe('modinfo amdgpu | grep "^version:"')
            if rc2 == 0 and out2:
                gpu.driver_version = out2.split(':')[-1].strip()
            
            # 获取ROCm版本
            rc3, out3, _ = run_cmd_safe('rocm-smi --version 2>/dev/null')
            if rc3 == 0 and out3:
                match = re.search(r'([0-9]+\.[0-9]+(?:\.[0-9]+)?)', out3)
                if match:
                    gpu.rocm_version = match.group(1)
            
            # 获取规格
            gpu.specs = get_gpu_specs(gpu.name)
            
            gpus.append(gpu)
        
        return gpus
    
    def _detect_windows(self) -> List[GPUInfo]:
        """Windows下检测AMD GPU"""
        # Windows检测逻辑
        return []
    
    def _extract_name(self, line: str) -> str:
        import re
        bracket_match = re.search(r'\[([^\]]+)\]', line)
        if bracket_match:
            return bracket_match.group(1).strip()
        return line.strip()
    
    def _determine_type(self, line: str) -> GPUType:
        """判断GPU类型"""
        line_lower = line.lower()
        integrated_keywords = ['radeon graphics', 'vega', 'renoir', 'cezanne']
        if any(keyword in line_lower for keyword in integrated_keywords):
            return GPUType.INTEGRATED
        return GPUType.DISCRETE

