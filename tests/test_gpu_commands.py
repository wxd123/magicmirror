# tests/test_gpu_commands.py
import pytest
import sys
import os

# 添加src目录到Python路径
src_path = '/mnt/workspace/py_project/magicmirror/src'
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from magicm.detector.hardware.gpu.core.command_executor import GPUCommandExecutor
from magicm.detector.hardware.gpu.core.base import GPUVendor, GPUType
from magicm.detector.hardware.gpu.gpu_detecter import gpu_detected, get_gpu_summary


class TestGPUDetection:
    """GPU检测完整测试"""
    
    def test_basic_detection(self):
        """测试基础GPU检测"""
        result = gpu_detected()
        
        # 基本字段验证
        assert 'gpu_present' in result
        assert 'all_gpus' in result
        assert 'gpu_name' in result
        assert isinstance(result['all_gpus'], list)
        
        if result['gpu_present']:
            print(f"\n✅ 检测到GPU: {result['gpu_name']}")
            if result['driver_version']:
                print(f"   驱动版本: {result['driver_version']}")
            if result['cuda_version']:
                print(f"   CUDA版本: {result['cuda_version']}")
            if result['rocm_version']:
                print(f"   ROCm版本: {result['rocm_version']}")
    
    def test_gpu_summary(self):
        """测试GPU摘要信息"""
        summary = get_gpu_summary()
        
        # 验证返回字段
        assert 'total_count' in summary
        assert 'discrete_count' in summary
        assert 'integrated_count' in summary
        assert 'main_gpu' in summary
        assert 'gpu_list' in summary
        assert 'vendors' in summary
        
        print(f"\n📊 GPU摘要:")
        print(f"   总GPU数: {summary['total_count']}")
        print(f"   独立显卡: {summary['discrete_count']}")
        print(f"   集成显卡: {summary['integrated_count']}")
        print(f"   主GPU: {summary['main_gpu']}")
        if summary['vendors']:
            print(f"   厂商: {', '.join(summary['vendors'])}")
    
    def test_command_executor(self):
        """测试命令执行器"""
        executor = GPUCommandExecutor()
        result = executor.detect_all()
        
        assert result is not None
        assert hasattr(result, 'all_gpus')
        assert hasattr(result, 'gpu_present')
        
        print(f"\n🚀 命令执行器检测结果:")
        print(f"   GPU数量: {len(result.all_gpus)}")
        
        for i, gpu in enumerate(result.all_gpus, 1):
            print(f"   GPU{i}: {gpu.name}")
            print(f"      厂商: {gpu.vendor.value if gpu.vendor else 'Unknown'}")
            print(f"      类型: {gpu.gpu_type.value if gpu.gpu_type else 'Unknown'}")
            if gpu.memory_gb:
                print(f"      显存: {gpu.memory_gb} GB")
    
    def test_vendor_filter(self):
        """测试厂商过滤"""
        executor = GPUCommandExecutor()
        
        # 测试NVIDIA过滤
        nvidia_gpus = executor.detect_by_vendor(GPUVendor.NVIDIA)
        for gpu in nvidia_gpus:
            assert gpu.vendor == GPUVendor.NVIDIA
            print(f"\n🎮 NVIDIA GPU: {gpu.name}")
        
        # 测试AMD过滤
        amd_gpus = executor.detect_by_vendor(GPUVendor.AMD)
        for gpu in amd_gpus:
            assert gpu.vendor == GPUVendor.AMD
    
    def test_gpu_info_structure(self):
        """测试GPU信息结构"""
        executor = GPUCommandExecutor()
        result = executor.detect_all()
        
        if result.all_gpus:
            gpu = result.all_gpus[0]
            
            # 验证基本属性
            assert hasattr(gpu, 'name')
            assert hasattr(gpu, 'vendor')
            assert hasattr(gpu, 'to_dict')
            
            # 测试转换为字典
            gpu_dict = gpu.to_dict()
            assert 'name' in gpu_dict
            assert isinstance(gpu_dict, dict)
            
            print(f"\n📝 GPU信息结构测试通过")
            print(f"   GPU名称: {gpu.name}")
            print(f"   字典格式: {list(gpu_dict.keys())}")


class TestPlatformAdapter:
    """平台适配器测试"""
    
    def test_platform_detection(self):
        """测试平台检测"""
        from magicm.detector.hardware.gpu.platform.factory import PlatformAdapterFactory
        
        adapter = PlatformAdapterFactory.create()
        system_type = adapter.get_system_type()
        
        assert system_type is not None
        print(f"\n💻 当前系统: {system_type.value}")
    
    def test_gpu_list_command(self):
        """测试GPU列表命令"""
        from magicm.detector.hardware.gpu.platform.linux_adapter import LinuxPlatformAdapter
        
        adapter = LinuxPlatformAdapter()
        gpu_list = adapter.get_gpu_list()
        
        print(f"\n🔍 GPU列表命令执行结果:")
        print(f"   找到 {len(gpu_list)} 个GPU设备")
        
        for gpu in gpu_list:
            print(f"   - {gpu.get('name', 'Unknown')}")


class TestCommandRegistration:
    """命令注册测试"""
    
    def test_registered_commands(self):
        """测试已注册的命令"""
        from magicm.detector.hardware.gpu.core.command_executor import CommandRegistry
        
        commands = CommandRegistry.get_all()
        vendors = [cmd.get_vendor() for cmd in commands]
        
        print(f"\n📦 已注册的厂商检测器:")
        for vendor in vendors:
            print(f"   - {vendor.value}")
        
        # 验证至少有一个厂商注册
        assert len(commands) > 0
    
    def test_command_priority(self):
        """测试命令优先级"""
        from magicm.detector.hardware.gpu.core.command_executor import CommandRegistry
        
        commands = CommandRegistry.get_all()
        
        # 验证优先级排序
        for i in range(len(commands) - 1):
            assert commands[i].get_priority() <= commands[i + 1].get_priority()
        
        print(f"\n⚡ 命令优先级排序验证通过")


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s', '--tb=short'])