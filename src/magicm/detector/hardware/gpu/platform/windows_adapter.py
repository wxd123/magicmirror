# detector/hardware/gpu/platform/windows_adapter.py
from typing import List, Dict, Any, Tuple
from ..core.base import PlatformAdapter, SystemType
from ..vendor.utils import run_cmd_safe

class WindowsPlatformAdapter(PlatformAdapter):
    """Windows平台适配器"""
    
    def get_system_type(self) -> SystemType:
        return SystemType.WINDOWS
    
    def run_command(self, cmd: str) -> Tuple[int, str, str]:
        return run_cmd_safe(cmd)
    
    def get_gpu_list(self) -> List[Dict[str, Any]]:
        """获取Windows GPU列表"""
        rc, out, _ = self.run_command('wmic path win32_VideoController get name /format:csv')
        if rc != 0 or not out:
            return []
        
        gpus = []
        lines = out.strip().split('\n')[1:]  # 跳过标题
        for line in lines:
            if line and ',' in line:
                name = line.split(',')[-1].strip()
                if name and not any(x in name.lower() for x in ['remote', 'mirror']):
                    gpus.append({
                        'raw_line': line,
                        'name': name
                    })
        return gpus