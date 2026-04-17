# detector/hardware/gpu/platform/linux_adapter.py
from typing import List, Dict, Any, Tuple
from ..core.base import PlatformAdapter, SystemType
from ..vendor.utils import run_cmd_safe


class LinuxPlatformAdapter(PlatformAdapter):
    """Linux平台适配器"""
    
    def get_system_type(self) -> SystemType:
        return SystemType.LINUX
    
    def run_command(self, cmd: str) -> Tuple[int, str, str]:
        return run_cmd_safe(cmd)
    
    def get_gpu_list(self) -> List[Dict[str, Any]]:
        """获取Linux GPU列表"""
        rc, out, _ = self.run_command('lspci | grep -E "VGA|3D|Display"')
        if rc != 0 or not out:
            return []
        
        gpus = []
        for line in out.strip().split('\n'):
            if line.strip():
                gpus.append({
                    'raw_line': line,
                    'name': self._extract_name(line)
                })
        return gpus
    
    def _extract_name(self, line: str) -> str:
        import re
        bracket_match = re.search(r'\[([^\]]+)\]', line)
        if bracket_match:
            return bracket_match.group(1).strip()
        
        if 'controller:' in line:
            parts = line.split('controller:', 1)
            if len(parts) > 1:
                name = parts[1].strip()
                name = re.sub(r'\([^)]*\)', '', name).strip()
                return name
        
        cleaned = re.sub(r'^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9a-f]\s+', '', line)
        cleaned = re.sub(r'(VGA compatible controller|3D controller|Display controller):\s*', '', cleaned)
        cleaned = re.sub(r'\([^)]*\)', '', cleaned)
        
        return cleaned.strip()