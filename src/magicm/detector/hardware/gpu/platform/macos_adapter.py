# detector/hardware/gpu/platform/macos_adapter.py

from typing import List, Dict, Any, Tuple
from ..core.base import PlatformAdapter, SystemType
from ..vendor.utils import run_cmd_safe

class MacOSPlatformAdapter(PlatformAdapter):
    """macOS平台适配器"""
    
    def get_system_type(self) -> SystemType:
        return SystemType.MACOS
    
    def run_command(self, cmd: str) -> Tuple[int, str, str]:
        return run_cmd_safe(cmd)
    
    def get_gpu_list(self) -> List[Dict[str, Any]]:
        """获取macOS GPU列表"""
        rc, out, _ = self.run_command('system_profiler SPDisplaysDataType | grep "Chipset Model"')
        if rc != 0 or not out:
            return []
        
        gpus = []
        for line in out.strip().split('\n'):
            if 'Chipset Model' in line:
                name = line.split(':')[-1].strip()
                gpus.append({
                    'raw_line': line,
                    'name': name
                })
        return gpus