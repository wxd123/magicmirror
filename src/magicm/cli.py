#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
magicm CLI 硬件检测工具
"""

import sys
import os

# 添加项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from magicm.detector.software.system import sys_detecter
from magicm.detector.hardware.cpu import cpu_detecter
from magicm.detector.hardware.gpu import gpu_detecter
from magicm.detector.hardware.mem import mem_detecter
from magicm.command.display import display_hardware_info


def get_system_info():
    """获取系统信息"""
    try:
        system_info = sys_detecter.detect()
        if not system_info or not isinstance(system_info, dict):
            system_info = {"name": "未知", "pretty_name": "未知系统"}
    except Exception as e:
        system_info = {"name": "未知", "pretty_name": "未知系统"}
    
    return system_info


def get_cpu_info():
    """获取CPU信息"""
    try:
        cpu_info = cpu_detecter.cpu_detected()
        if not cpu_info or not isinstance(cpu_info, dict):
            cpu_info = {"model": "未知", "simple_model": "未知CPU", "cores": "未知"}
    except Exception as e:
        cpu_info = {"model": "未知", "simple_model": "未知CPU", "cores": "未知"}
    
    return cpu_info


def get_gpu_info():
    """获取GPU信息"""
    try:
        gpu_result = gpu_detecter.gpu_detected()
        
        gpu_info = {
            "name": "未知", 
            "memory_gb": 0, 
            "driver_version": "未知",
            "type": "unknown"
        }
        
        if gpu_result and isinstance(gpu_result, dict):
            if gpu_result.get("discrete_gpu"):
                gpu_info["name"] = gpu_result["discrete_gpu"]
            elif gpu_result.get("integrated_gpu"):
                gpu_info["name"] = gpu_result["integrated_gpu"]
            elif gpu_result.get("gpu_name"):
                gpu_info["name"] = gpu_result["gpu_name"]
            
            if gpu_result.get("driver_version"):
                gpu_info["driver_version"] = gpu_result["driver_version"]
            
            all_gpus = gpu_result.get("all_gpus", [])
            if all_gpus and len(all_gpus) > 0:
                first_gpu = all_gpus[0]
                if first_gpu.get("memory_gb"):
                    gpu_info["memory_gb"] = first_gpu["memory_gb"]
    except Exception as e:
        pass
    
    return gpu_info


def get_memory_info():
    """获取内存信息"""
    try:
        memory_info = mem_detecter.mem_detected()
        if not memory_info or not isinstance(memory_info, dict):
            memory_info = {"total_gb": 0, "total_mb": 0, "total_str": "未知"}
    except Exception as e:
        memory_info = {"total_gb": 0, "total_mb": 0, "total_str": "未知"}
    
    return memory_info


def main():
    """主函数：顺序调用各检测模块，然后交给 display 显示"""
    print("\n🔍 正在检测硬件信息...\n")
    
    # 1. 操作系统检测
    system_info = get_system_info()
    os_name = system_info.get('pretty_name', system_info.get('name', '未知'))
    # print(f"  [1/4] 检测操作系统... {os_name}")
    
    # 2. CPU 检测
    cpu_info = get_cpu_info()
    cpu_name = cpu_info.get('simple_model', cpu_info.get('model', '未知'))
    # print(f"  [2/4] 检测 CPU... {cpu_name}")
    
    # 3. GPU 检测
    gpu_info = get_gpu_info()
    gpu_name = gpu_info.get('name', '未知')
    vram = gpu_info.get('memory_gb', 0)
    driver = gpu_info.get('driver_version', '未知')
    # print(f"  [3/4] 检测 GPU... {gpu_name} (显存: {vram}GB, 驱动: {driver})")
    
    # 4. 内存检测
    memory_info = get_memory_info()
    mem_gb = memory_info.get('total_gb', 0)
    # print(f"  [4/4] 检测内存... {mem_gb}GB")
    
    # 5. 交给 display 模块处理
    # print("\n  [5/5] 生成检测报告...")
    display_hardware_info(system_info, cpu_info, gpu_info, memory_info)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())