from typing import List, Dict, Any, Optional, Type
from .base import GPUDetectionCommand, GPUInfo, DetectionResult, GPUVendor, SystemType
from ..platform.factory import PlatformAdapterFactory
from ..vendor.utils import get_gpu_memory


class CommandRegistry:
    """命令注册器"""
    
    _commands: Dict[GPUVendor, GPUDetectionCommand] = {}
    
    @classmethod
    def register(cls, command: GPUDetectionCommand):
        """注册命令"""
        cls._commands[command.get_vendor()] = command
    
    @classmethod
    def get(cls, vendor: GPUVendor) -> Optional[GPUDetectionCommand]:
        """获取命令"""
        return cls._commands.get(vendor)
    
    @classmethod
    def get_all(cls) -> List[GPUDetectionCommand]:
        """获取所有命令（按优先级排序）"""
        return sorted(cls._commands.values(), key=lambda c: c.get_priority())
    
    @classmethod
    def clear(cls):
        """清空所有命令"""
        cls._commands.clear()


class GPUCommandExecutor:
    """GPU命令执行器 - 核心业务逻辑"""
    
    def __init__(self, system: str = None):
        """
        初始化执行器
        
        Args:
            system: 系统类型 (linux/windows/macos)，None表示自动检测
        """
        self.platform_adapter = PlatformAdapterFactory.create(system)
        self.system_type = self.platform_adapter.get_system_type()
        self._init_default_commands()
    
    def _init_default_commands(self):
        """初始化默认命令"""
        from ..commands.nvidia_command import NVIDIACommand
        from ..commands.amd_command import AMDCommand
        from ..commands.intel_command import IntelCommand
        from ..commands.huawei_command import HuaweiCommand
        
        CommandRegistry.clear()
        CommandRegistry.register(NVIDIACommand())
        CommandRegistry.register(AMDCommand())
        CommandRegistry.register(IntelCommand())
        CommandRegistry.register(HuaweiCommand())
    
    def _create_context(self) -> Dict[str, Any]:
        """创建执行上下文"""
        return {
            'platform_adapter': self.platform_adapter,
            'system_type': self.system_type,
            'system': self.system_type.value if self.system_type else 'linux'
        }
    
    def detect_all(self) -> DetectionResult:
        """检测所有GPU - 返回DetectionResult"""
        result = DetectionResult()
        context = self._create_context()
        
        # 执行所有命令
        for command in CommandRegistry.get_all():
            try:
                gpus = command.execute(context)
                for gpu in gpus:
                    # 补充显存信息（如果还没有）
                    if not gpu.memory_gb:
                        gpu.memory_gb = get_gpu_memory(gpu.name, None)
                    
                    result.all_gpus.append(gpu)
                    
                    # 分类存储
                    if gpu.gpu_type and gpu.gpu_type.value == 'discrete':
                        if not result.discrete_gpu:
                            result.discrete_gpu = gpu
                    elif gpu.gpu_type and gpu.gpu_type.value == 'integrated':
                        if not result.integrated_gpu:
                            result.integrated_gpu = gpu
            except Exception as e:
                print(f"Error executing {command.get_vendor().value} command: {e}")
        
        # 设置主GPU信息
        main = result.main_gpu
        if main:
            result.gpu_name = main.name
            result.driver_version = main.driver_version
            result.cuda_version = main.cuda_version
            result.rocm_version = main.rocm_version
            result.ascend_version = main.ascend_version
            result.nvlink = main.nvlink
            result.specs = main.specs
        
        result.gpu_present = len(result.all_gpus) > 0
        return result
    
    def detect_by_vendor(self, vendor: GPUVendor) -> List[GPUInfo]:
        """检测特定厂商的GPU"""
        command = CommandRegistry.get(vendor)
        if command:
            context = self._create_context()
            return command.execute(context)
        return []
    
    def add_command(self, command: GPUDetectionCommand):
        """动态添加命令（用于扩展）"""
        CommandRegistry.register(command)
    
    def remove_command(self, vendor: GPUVendor):
        """移除命令"""
        if vendor in CommandRegistry._commands:
            del CommandRegistry._commands[vendor]
    
    def get_registered_vendors(self) -> List[GPUVendor]:
        """获取已注册的厂商列表"""
        return list(CommandRegistry._commands.keys())
