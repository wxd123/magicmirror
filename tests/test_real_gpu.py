# tests/test_real_gpu.py
import pytest
import sys
import os
import json

# 添加src目录
src_path = '/mnt/workspace/py_project/magicmirror/src'
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from magicm.detector.hardware.gpu.gpu_detecter import gpu_detected, get_gpu_summary
from magicm.detector.hardware.gpu.core.command_executor import GPUCommandExecutor
from magicm.detector.hardware.gpu.core.base import GPUVendor


def test_real_gpu_detection():
    """测试真实GPU检测 - 使用assert而不是return"""
    result = gpu_detected()
    
    # 使用assert验证结果
    assert 'gpu_present' in result
    assert 'all_gpus' in result
    assert isinstance(result['all_gpus'], list)
    
    # 打印信息用于调试
    print(f"\n✅ GPU存在: {result['gpu_present']}")
    
    if result['gpu_present']:
        print(f"   主GPU: {result['gpu_name']}")
        print(f"   驱动版本: {result['driver_version']}")
        print(f"   CUDA版本: {result['cuda_version']}")
        
        # 验证GPU信息不为空
        assert result['gpu_name'] is not None
    else:
        print("   ⚠️  未检测到GPU设备")


def test_gpu_summary():
    """测试GPU摘要信息"""
    summary = get_gpu_summary()
    
    # 验证返回字段
    assert 'total_count' in summary
    assert 'discrete_count' in summary
    assert 'integrated_count' in summary
    assert 'main_gpu' in summary
    assert 'gpu_list' in summary
    assert 'vendors' in summary
    
    # 验证数据类型
    assert isinstance(summary['total_count'], int)
    assert isinstance(summary['gpu_list'], list)
    
    print(f"\n📊 GPU摘要:")
    print(f"   总GPU数: {summary['total_count']}")
    print(f"   独立显卡: {summary['discrete_count']}")
    print(f"   集成显卡: {summary['integrated_count']}")


def test_command_executor_real():
    """测试命令执行器"""
    executor = GPUCommandExecutor()
    result = executor.detect_all()
    
    # 验证结果对象
    assert result is not None
    assert hasattr(result, 'all_gpus')
    assert hasattr(result, 'gpu_present')
    assert isinstance(result.all_gpus, list)
    
    print(f"\n🚀 发现 {len(result.all_gpus)} 个GPU")
    
    for gpu in result.all_gpus:
        assert gpu.name is not None
        print(f"   - {gpu.name} ({gpu.vendor.value if gpu.vendor else 'Unknown'})")


def test_vendor_specific():
    """测试厂商特定检测"""
    executor = GPUCommandExecutor()
    
    # 测试NVIDIA检测（不应抛出异常）
    nvidia_gpus = executor.detect_by_vendor(GPUVendor.NVIDIA)
    assert isinstance(nvidia_gpus, list)
    
    for gpu in nvidia_gpus:
        assert gpu.vendor == GPUVendor.NVIDIA
    
    # 测试AMD检测
    amd_gpus = executor.detect_by_vendor(GPUVendor.AMD)
    assert isinstance(amd_gpus, list)
    
    print(f"\n🏭 厂商检测完成:")
    print(f"   NVIDIA GPU数量: {len(nvidia_gpus)}")
    print(f"   AMD GPU数量: {len(amd_gpus)}")


def test_performance():
    """测试检测性能"""
    import time
    
    executor = GPUCommandExecutor()
    
    # 执行多次取平均
    times = []
    for i in range(5):
        start = time.perf_counter()
        result = executor.detect_all()
        elapsed = time.perf_counter() - start
        times.append(elapsed)
    
    avg_time = sum(times) / len(times)
    
    # 验证性能（平均时间应小于5秒）
    assert avg_time < 5.0, f"检测时间过长: {avg_time:.2f}秒"
    
    print(f"\n⏱️  平均检测时间: {avg_time:.3f}秒")


def test_nvlink():
    """测试NVLink检测"""
    result = gpu_detected()
    nvlink = result.get('nvlink')
    
    # NVLink可能为None（非NVIDIA GPU），所以不强制断言
    if nvlink is not None:
        assert isinstance(nvlink, dict)
        assert 'supported' in nvlink
        print(f"\n🔗 NVLink支持: {nvlink.get('supported', False)}")
    else:
        print("\nℹ️  未检测到NVLink信息（可能不是NVIDIA GPU）")


# 如果需要测试真实硬件，使用pytest.mark标记
@pytest.mark.gpu
@pytest.mark.slow
def test_full_hardware_scan():
    """完整硬件扫描测试（标记为需要GPU）"""
    executor = GPUCommandExecutor()
    result = executor.detect_all()
    
    # 基本验证
    assert result is not None
    print(f"\n🖥️  完整硬件扫描完成")
    print(f"   检测到 {len(result.all_gpus)} 个GPU设备")
    
    # 输出详细结果
    for i, gpu in enumerate(result.all_gpus, 1):
        print(f"\n   GPU {i}:")
        print(f"      名称: {gpu.name}")
        print(f"      厂商: {gpu.vendor.value if gpu.vendor else 'Unknown'}")
        if gpu.memory_gb:
            print(f"      显存: {gpu.memory_gb} GB")
        if gpu.driver_version:
            print(f"      驱动: {gpu.driver_version}")


if __name__ == '__main__':
    # 直接运行脚本时执行
    pytest.main([__file__, '-v', '-s', '--tb=short'])