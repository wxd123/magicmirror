# detector/hardware/gpu/platform/factory.py

from ..core.base import PlatformAdapter
from .linux_adapter import LinuxPlatformAdapter
from .windows_adapter import WindowsPlatformAdapter
from .macos_adapter import MacOSPlatformAdapter

class PlatformAdapterFactory:
    """平台适配器工厂"""
    
    @staticmethod
    def create(system: str = None) -> PlatformAdapter:
        """创建平台适配器"""
        if system is None:
            import sys
            if sys.platform.startswith('linux'):
                system = 'linux'
            elif sys.platform.startswith('win'):
                system = 'windows'
            elif sys.platform.startswith('darwin'):
                system = 'macos'
            else:
                system = 'linux'
        
        if system == 'linux':
            return LinuxPlatformAdapter()
        elif system == 'windows':
            return WindowsPlatformAdapter()
        elif system == 'macos':
            return MacOSPlatformAdapter()
        else:
            return LinuxPlatformAdapter()