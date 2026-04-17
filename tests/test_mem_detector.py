#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
内存检测模块的单元测试
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from magicm.detector.hardware.mem.mem_detecter import mem_detected


class TestMemDetector(unittest.TestCase):
    """测试内存检测器"""
    
    # ==================== 正常功能测试 ====================
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_normal(self, mock_psutil):
        """测试正常获取内存信息"""
        # 模拟 psutil.virtual_memory() 返回值
        mock_memory = MagicMock()
        mock_memory.total = 16 * 1024 * 1024 * 1024  # 16 GB
        mock_memory.available = 8 * 1024 * 1024 * 1024  # 8 GB
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        # 验证返回值结构
        self.assertIsInstance(result, dict)
        self.assertIn('total_mb', result)
        self.assertIn('total_gb', result)
        self.assertIn('total_str', result)
        self.assertIn('available_mb', result)
        self.assertIn('available_str', result)
        
        # 验证数值计算正确性
        self.assertEqual(result['total_mb'], 16384)  # 16 * 1024 = 16384 MB
        self.assertEqual(result['total_gb'], 16)
        self.assertEqual(result['total_str'], '16 GB')
        self.assertEqual(result['available_mb'], 8192)  # 8 * 1024 = 8192 MB
        self.assertEqual(result['available_str'], '8 GB')
        
        # 验证 psutil 被调用
        mock_psutil.virtual_memory.assert_called_once()
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_8gb(self, mock_psutil):
        """测试 8GB 内存"""
        mock_memory = MagicMock()
        mock_memory.total = 8 * 1024 * 1024 * 1024  # 8 GB
        mock_memory.available = 4 * 1024 * 1024 * 1024  # 4 GB
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 8192)
        self.assertEqual(result['total_gb'], 8)
        self.assertEqual(result['total_str'], '8 GB')
        self.assertEqual(result['available_mb'], 4096)
        self.assertEqual(result['available_str'], '4 GB')
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_32gb(self, mock_psutil):
        """测试 32GB 内存"""
        mock_memory = MagicMock()
        mock_memory.total = 32 * 1024 * 1024 * 1024  # 32 GB
        mock_memory.available = 16 * 1024 * 1024 * 1024  # 16 GB
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 32768)
        self.assertEqual(result['total_gb'], 32)
        self.assertEqual(result['total_str'], '32 GB')
        self.assertEqual(result['available_mb'], 16384)
        self.assertEqual(result['available_str'], '16 GB')
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_64gb(self, mock_psutil):
        """测试 64GB 内存"""
        mock_memory = MagicMock()
        mock_memory.total = 64 * 1024 * 1024 * 1024  # 64 GB
        mock_memory.available = 32 * 1024 * 1024 * 1024  # 32 GB
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 65536)
        self.assertEqual(result['total_gb'], 64)
        self.assertEqual(result['total_str'], '64 GB')
        self.assertEqual(result['available_mb'], 32768)
        self.assertEqual(result['available_str'], '32 GB')
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_128gb(self, mock_psutil):
        """测试 128GB 内存（大内存服务器）"""
        mock_memory = MagicMock()
        mock_memory.total = 128 * 1024 * 1024 * 1024  # 128 GB
        mock_memory.available = 64 * 1024 * 1024 * 1024  # 64 GB
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 131072)
        self.assertEqual(result['total_gb'], 128)
        self.assertEqual(result['total_str'], '128 GB')
        self.assertEqual(result['available_mb'], 65536)
        self.assertEqual(result['available_str'], '64 GB')
    
    # ==================== 边界情况测试 ====================
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_zero_available(self, mock_psutil):
        """测试可用内存为 0 的情况"""
        mock_memory = MagicMock()
        mock_memory.total = 16 * 1024 * 1024 * 1024  # 16 GB
        mock_memory.available = 0
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 16384)
        self.assertEqual(result['total_gb'], 16)
        self.assertEqual(result['total_str'], '16 GB')
        self.assertEqual(result['available_mb'], 0)
        self.assertEqual(result['available_str'], '0 GB')
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_full_memory(self, mock_psutil):
        """测试内存几乎用满的情况"""
        mock_memory = MagicMock()
        mock_memory.total = 16 * 1024 * 1024 * 1024  # 16 GB
        mock_memory.available = 128 * 1024 * 1024  # 128 MB 可用
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertEqual(result['total_mb'], 16384)
        self.assertEqual(result['total_gb'], 16)
        self.assertEqual(result['available_mb'], 128)
        self.assertEqual(result['available_str'], '0 GB')  # 128 MB < 1024 MB，显示 0 GB
    
    # ==================== 异常处理测试 ====================
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_exception(self, mock_psutil):
        """测试 psutil 异常处理"""
        mock_psutil.virtual_memory.side_effect = Exception("psutil 调用失败")
        
        result = mem_detected()
        
        # 验证返回默认值
        self.assertEqual(result['total_mb'], 0)
        self.assertEqual(result['total_gb'], 0)
        self.assertEqual(result['total_str'], '未知')
        self.assertEqual(result['available_mb'], 0)
        self.assertEqual(result['available_str'], '未知')
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_mem_detected_attribute_error(self, mock_psutil):
        """测试 psutil 返回值缺少属性"""
        mock_psutil.virtual_memory.return_value = None
        
        result = mem_detected()
        
        # 应该捕获 AttributeError 并返回默认值
        self.assertEqual(result['total_mb'], 0)
        self.assertEqual(result['total_str'], '未知')
    
    # ==================== 返回值类型测试 ====================
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_return_type_integers(self, mock_psutil):
        """测试返回值中的数值都是整数"""
        mock_memory = MagicMock()
        mock_memory.total = 16 * 1024 * 1024 * 1024
        mock_memory.available = 8 * 1024 * 1024 * 1024
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        self.assertIsInstance(result['total_mb'], int)
        self.assertIsInstance(result['total_gb'], int)
        self.assertIsInstance(result['available_mb'], int)
    
    @patch('magicm.detector.hardware.mem.mem_detecter.psutil')
    def test_return_strings_format(self, mock_psutil):
        """测试字符串格式正确"""
        mock_memory = MagicMock()
        mock_memory.total = 16 * 1024 * 1024 * 1024
        mock_memory.available = 8 * 1024 * 1024 * 1024
        mock_psutil.virtual_memory.return_value = mock_memory
        
        result = mem_detected()
        
        # 验证字符串格式
        self.assertRegex(result['total_str'], r'^\d+ GB$')
        self.assertRegex(result['available_str'], r'^\d+ GB$')
    
    # ==================== 集成测试 ====================
    
    @unittest.skip("集成测试，需要真实系统环境（会真实调用 psutil）")
    def test_integration_real_system(self):
        """真实系统集成测试（需要 psutil 已安装）"""
        try:
            import psutil
        except ImportError:
            self.skipTest("psutil 未安装")
        
        result = mem_detected()
        
        # 验证真实返回值
        self.assertIsInstance(result, dict)
        self.assertGreater(result['total_mb'], 0)
        self.assertGreater(result['total_gb'], 0)
        self.assertNotEqual(result['total_str'], '未知')
        self.assertIsInstance(result['available_mb'], int)
        self.assertIsInstance(result['available_str'], str)
        
        print(f"\n真实内存检测结果:")
        print(f"  总内存: {result['total_str']} ({result['total_mb']} MB)")
        print(f"  可用内存: {result['available_str']} ({result['available_mb']} MB)")


if __name__ == "__main__":
    unittest.main()