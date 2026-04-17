#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
display 模块的单元测试
"""

import sys
import os
import unittest

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.magicm.command.display import HardwareDisplay


class TestHardwareDisplay(unittest.TestCase):
    """测试 HardwareDisplay 类"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.display = HardwareDisplay()
    
    def test_get_gpu_rating(self):
        """测试GPU评级"""
        # 核弹级
        self.assertEqual(self.display.get_gpu_rating("RTX 4090"), "【核弹级】")
        self.assertEqual(self.display.get_gpu_rating("RTX 5090"), "【核弹级】")
        
        # 旗舰级
        self.assertEqual(self.display.get_gpu_rating("RTX 4080"), "【旗舰级】")
        
        # 主流级
        self.assertEqual(self.display.get_gpu_rating("GTX 1060"), "【主流级】")
    
    def test_get_vram_rating(self):
        """测试显存评级"""
        self.assertEqual(self.display.get_vram_rating(24), "【显存富翁】")
        self.assertEqual(self.display.get_vram_rating(16), "【小资生活】")
        self.assertEqual(self.display.get_vram_rating(12), "【温饱有余】")
        self.assertEqual(self.display.get_vram_rating(8), "【勉强够用】")
        self.assertEqual(self.display.get_vram_rating(4), "【显存乞丐】")
        self.assertEqual(self.display.get_vram_rating(2), "【极限生存】")
    
    def test_get_driver_rating(self):
        """测试驱动评级"""
        self.assertEqual(self.display.get_driver_rating("570.86.16"), "【紧跟版本】")
        self.assertEqual(self.display.get_driver_rating("560.35.03"), "【版本适中】")
        self.assertEqual(self.display.get_driver_rating("545.29.06"), "【版本较旧】")
        self.assertEqual(self.display.get_driver_rating("535.54.03"), "【远古版本】")
        self.assertEqual(self.display.get_driver_rating(""), "【未检测】")
        self.assertEqual(self.display.get_driver_rating(None), "【未检测】")
    
    def test_get_system_rating(self):
        """测试系统评级"""
        self.assertEqual(self.display.get_system_rating("Ubuntu 22.04"), "【稳得一批】")
        self.assertEqual(self.display.get_system_rating("Debian 12"), "【稳得一批】")
        self.assertEqual(self.display.get_system_rating("CentOS 7"), "【企业级稳】")
        self.assertEqual(self.display.get_system_rating("Windows 11"), "【最新潮流】")
        self.assertEqual(self.display.get_system_rating("Windows 10"), "【经典永存】")
        self.assertEqual(self.display.get_system_rating("macOS 14"), "【果味十足】")
    
    def test_get_cpu_rating(self):
        """测试CPU评级"""
        self.assertEqual(self.display.get_cpu_rating("Ryzen 9 7950X"), "【性能怪兽】")
        self.assertEqual(self.display.get_cpu_rating("i9-14900K"), "【性能怪兽】")
        self.assertEqual(self.display.get_cpu_rating("Ryzen 7 7800X"), "【性能标杆】")
        self.assertEqual(self.display.get_cpu_rating("i7-14700K"), "【性能标杆】")
        self.assertEqual(self.display.get_cpu_rating("Ryzen 5 7600X"), "【主流利器】")
        self.assertEqual(self.display.get_cpu_rating("i5-14600K"), "【主流利器】")
        self.assertEqual(self.display.get_cpu_rating("Ryzen 3 4100"), "【入门首选】")
        self.assertEqual(self.display.get_cpu_rating("i3-14100"), "【入门首选】")
    
    def test_get_memory_rating(self):
        """测试内存评级"""
        self.assertEqual(self.display.get_memory_rating(64), "【内存自由】")
        self.assertEqual(self.display.get_memory_rating(32), "【大胃王】")
        self.assertEqual(self.display.get_memory_rating(16), "【小康生活】")
        self.assertEqual(self.display.get_memory_rating(8), "【温饱水平】")
        self.assertEqual(self.display.get_memory_rating(4), "【急需升级】")
    
    def test_display_methods(self):
        """测试显示方法（只测试不报错）"""
        # 测试各个显示方法
        gpu_info = {"name": "RTX 4090", "memory_gb": 24, "driver_version": "570.86.16"}
        system_info = {"name": "Ubuntu", "pretty_name": "Ubuntu 22.04"}
        cpu_info = {"model": "Ryzen 9 7950X", "simple_model": "Ryzen 9 7950X"}
        memory_info = {"total_gb": 32}
        
        # 这些方法只是打印，我们只测试它们不抛出异常
        try:
            self.display.show_gpu_info(gpu_info)
            self.display.show_vram_info(gpu_info)
            self.display.show_driver_info(gpu_info)
            self.display.show_system_info(system_info)
            self.display.show_cpu_info(cpu_info)
            self.display.show_memory_info(memory_info)
            self.display.show_banner()
            self.display.show_footer()
            self.display.display_all(system_info, cpu_info, gpu_info, memory_info)
        except Exception as e:
            self.fail(f"显示方法抛出异常: {e}")


class TestFormatHardwareInfo(unittest.TestCase):
    """测试 format_hardware_info 函数"""
    
    def test_format_function(self):
        """测试格式化函数"""
        from src.magicm.command.display import format_hardware_info
        
        system_info = {"name": "Ubuntu", "pretty_name": "Ubuntu 22.04"}
        cpu_info = {"model": "Ryzen 9 7950X", "simple_model": "Ryzen 9 7950X"}
        gpu_info = {"name": "RTX 4090", "memory_gb": 24, "driver_version": "570.86.16"}
        memory_info = {"total_gb": 32}
        
        result = format_hardware_info(system_info, cpu_info, gpu_info, memory_info)
        
        self.assertIsInstance(result, str)
        self.assertIn("你的硬件检测结果", result)
        self.assertIn("RTX 4090", result)
        self.assertIn("Ryzen 9", result)
        self.assertIn("Ubuntu", result)


if __name__ == "__main__":
    unittest.main()