#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GPU检测模块的单元测试
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from magicm.detector.hardware.gpu import gpu_detecter


class TestGPUDetector(unittest.TestCase):
    """测试GPU检测器"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.original_platform = sys.platform
    
    def tearDown(self):
        """测试后的清理工作"""
        sys.platform = self.original_platform
    
    # ==================== 平台检测测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.win_func')
    def test_gpu_detected_windows(self, mock_win_func):
        """测试 Windows 平台 GPU 检测"""
        sys.platform = 'win32'
        
        mock_win_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4090',
            'integrated_gpu': None,
            'all_gpus': [{'name': 'NVIDIA RTX 4090', 'type': 'discrete', 'memory_gb': 24}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        mock_win_func.assert_called_once()
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get('gpu_present'))
        self.assertEqual(result.get('discrete_gpu'), 'NVIDIA RTX 4090')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_gpu_detected_linux(self, mock_linux_func):
        """测试 Linux 平台 GPU 检测"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'AMD Radeon RX 7900 XTX',
            'integrated_gpu': None,
            'all_gpus': [{'name': 'AMD Radeon RX 7900 XTX', 'type': 'discrete', 'memory_gb': 24}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        mock_linux_func.assert_called_once()
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get('gpu_present'))
        self.assertEqual(result.get('discrete_gpu'), 'AMD Radeon RX 7900 XTX')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.mac_func')
    def test_gpu_detected_macos(self, mock_mac_func):
        """测试 macOS 平台 GPU 检测"""
        sys.platform = 'darwin'
        
        mock_mac_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': None,
            'integrated_gpu': 'Apple M2 Pro',
            'all_gpus': [{'name': 'Apple M2 Pro', 'type': 'integrated', 'memory_gb': 16}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        mock_mac_func.assert_called_once()
        self.assertIsInstance(result, dict)
        self.assertTrue(result.get('gpu_present'))
        self.assertEqual(result.get('integrated_gpu'), 'Apple M2 Pro')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_gpu_detected_exception(self, mock_linux_func):
        """测试 GPU 检测异常处理"""
        sys.platform = 'linux'
        
        mock_linux_func.side_effect = Exception("测试异常")
        
        result = gpu_detecter.gpu_detected()
        
        self.assertIsInstance(result, dict)
        self.assertFalse(result.get('gpu_present'))
        self.assertEqual(result.get('all_gpus'), [])
    
    # ==================== 返回值结构测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.win_func')
    def test_return_structure(self, mock_win_func):
        """测试返回值结构"""
        sys.platform = 'win32'
        
        mock_win_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4080',
            'integrated_gpu': 'Intel UHD Graphics',
            'driver_version': '531.41',
            'cuda_supported_by_driver': '12.1',
            'gpu_name': 'NVIDIA RTX 4080',
            'all_gpus': [
                {'name': 'NVIDIA RTX 4080', 'type': 'discrete', 'memory_gb': 16},
                {'name': 'Intel UHD Graphics', 'type': 'integrated', 'memory_gb': 0}
            ]
        }
        
        result = gpu_detecter.gpu_detected()
        
        # 检查必需的键
        required_keys = ['gpu_present', 'discrete_gpu', 'integrated_gpu', 
                        'driver_version', 'cuda_supported_by_driver', 'gpu_name', 'all_gpus']
        for key in required_keys:
            self.assertIn(key, result)
        
        # 检查 all_gpus 是列表
        self.assertIsInstance(result['all_gpus'], list)
    
    # ==================== 独立显卡测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_discrete_gpu_only(self, mock_linux_func):
        """测试只有独立显卡的情况"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4090',
            'integrated_gpu': None,
            'all_gpus': [{'name': 'NVIDIA RTX 4090', 'type': 'discrete', 'memory_gb': 24}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertTrue(result['gpu_present'])
        self.assertEqual(result['discrete_gpu'], 'NVIDIA RTX 4090')
        self.assertIsNone(result['integrated_gpu'])
        self.assertEqual(result['gpu_name'], 'NVIDIA RTX 4090')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.win_func')
    def test_integrated_gpu_only(self, mock_win_func):
        """测试只有集成显卡的情况"""
        sys.platform = 'win32'
        
        mock_win_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': None,
            'integrated_gpu': 'Intel Iris Xe Graphics',
            'all_gpus': [{'name': 'Intel Iris Xe Graphics', 'type': 'integrated', 'memory_gb': 0}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertTrue(result['gpu_present'])
        self.assertIsNone(result['discrete_gpu'])
        self.assertEqual(result['integrated_gpu'], 'Intel Iris Xe Graphics')
        self.assertEqual(result['gpu_name'], 'Intel Iris Xe Graphics')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_both_gpus(self, mock_linux_func):
        """测试同时有独立和集成显卡的情况"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4080',
            'integrated_gpu': 'AMD Radeon Graphics',
            'all_gpus': [
                {'name': 'NVIDIA RTX 4080', 'type': 'discrete', 'memory_gb': 16},
                {'name': 'AMD Radeon Graphics', 'type': 'integrated', 'memory_gb': 0}
            ]
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertTrue(result['gpu_present'])
        self.assertEqual(result['discrete_gpu'], 'NVIDIA RTX 4080')
        self.assertEqual(result['integrated_gpu'], 'AMD Radeon Graphics')
        # gpu_name 应该是第一个 GPU（独立显卡）
        self.assertEqual(result['gpu_name'], 'NVIDIA RTX 4080')
        self.assertEqual(len(result['all_gpus']), 2)
    
    # ==================== GPU 摘要测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.gpu_detected')
    def test_get_gpu_summary_discrete_only(self, mock_gpu_detected):
        """测试只有独立显卡时的摘要"""
        mock_gpu_detected.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4090',
            'integrated_gpu': None,
            'all_gpus': []
        }
        
        result = gpu_detecter.get_gpu_summary()
        
        self.assertEqual(result, 'NVIDIA RTX 4090')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.gpu_detected')
    def test_get_gpu_summary_integrated_only(self, mock_gpu_detected):
        """测试只有集成显卡时的摘要"""
        mock_gpu_detected.return_value = {
            'gpu_present': True,
            'discrete_gpu': None,
            'integrated_gpu': 'Intel UHD Graphics',
            'all_gpus': []
        }
        
        result = gpu_detecter.get_gpu_summary()
        
        self.assertEqual(result, '集成显卡: Intel UHD Graphics')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.gpu_detected')
    def test_get_gpu_summary_both_gpus(self, mock_gpu_detected):
        """测试同时有独立和集成显卡时的摘要"""
        mock_gpu_detected.return_value = {
            'gpu_present': True,
            'discrete_gpu': 'NVIDIA RTX 4080',
            'integrated_gpu': 'Intel UHD Graphics',
            'all_gpus': []
        }
        
        result = gpu_detecter.get_gpu_summary()
        
        self.assertEqual(result, '独立: NVIDIA RTX 4080 / 集成: Intel UHD Graphics')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.gpu_detected')
    def test_get_gpu_summary_no_gpu(self, mock_gpu_detected):
        """测试没有检测到显卡时的摘要"""
        mock_gpu_detected.return_value = {
            'gpu_present': False,
            'discrete_gpu': None,
            'integrated_gpu': None,
            'all_gpus': []
        }
        
        result = gpu_detecter.get_gpu_summary()
        
        self.assertEqual(result, '未检测到显卡')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.gpu_detected')
    def test_get_gpu_summary_with_all_gpus(self, mock_gpu_detected):
        """测试使用 all_gpus 作为后备的摘要"""
        mock_gpu_detected.return_value = {
            'gpu_present': True,
            'discrete_gpu': None,
            'integrated_gpu': None,
            'all_gpus': [{'name': 'Unknown GPU', 'type': 'unknown'}]
        }
        
        result = gpu_detecter.get_gpu_summary()
        
        self.assertEqual(result, 'Unknown GPU')
    
    # ==================== gpu_present 标志测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_gpu_present_true(self, mock_linux_func):
        """测试 gpu_present 标志为 True"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'all_gpus': [{'name': 'GPU 1'}, {'name': 'GPU 2'}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertTrue(result['gpu_present'])
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_gpu_present_false(self, mock_linux_func):
        """测试 gpu_present 标志为 False"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'all_gpus': []
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertFalse(result['gpu_present'])
    
    # ==================== 兼容性测试 ====================
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.win_func')
    def test_gpu_name_compatibility(self, mock_win_func):
        """测试 gpu_name 兼容性（旧代码依赖）"""
        sys.platform = 'win32'
        
        mock_win_func.return_value = {
            'all_gpus': [{'name': 'Test GPU', 'type': 'discrete'}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        # 确保 gpu_name 被正确设置
        self.assertEqual(result['gpu_name'], 'Test GPU')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.mac_func')
    def test_driver_version_preserved(self, mock_mac_func):
        """测试驱动版本信息被保留"""
        sys.platform = 'darwin'
        
        mock_mac_func.return_value = {
            'all_gpus': [{'name': 'Apple GPU', 'type': 'integrated'}],
            'driver_version': 'Metal 3'
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertEqual(result.get('driver_version'), 'Metal 3')


class TestGPUDetectorEdgeCases(unittest.TestCase):
    """GPU检测边缘情况测试"""
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_empty_gpu_list(self, mock_linux_func):
        """测试空 GPU 列表"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'all_gpus': []
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertFalse(result['gpu_present'])
        self.assertIsNone(result['gpu_name'])
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.win_func')
    def test_gpu_without_type(self, mock_win_func):
        """测试没有 type 字段的 GPU"""
        sys.platform = 'win32'
        
        mock_win_func.return_value = {
            'all_gpus': [{'name': 'Unknown GPU'}]
        }
        
        result = gpu_detecter.gpu_detected()
        
        # 应该能处理没有 type 的情况
        self.assertTrue(result['gpu_present'])
        self.assertEqual(result['gpu_name'], 'Unknown GPU')
    
    @patch('magicm.detector.hardware.gpu.gpu_detecter.linux_func')
    def test_partial_gpu_info(self, mock_linux_func):
        """测试部分 GPU 信息"""
        sys.platform = 'linux'
        
        mock_linux_func.return_value = {
            'all_gpus': [{'name': 'NVIDIA GPU'}],
            'discrete_gpu': None,
            'integrated_gpu': None
        }
        
        result = gpu_detecter.gpu_detected()
        
        self.assertEqual(result['gpu_name'], 'NVIDIA GPU')
        self.assertEqual(result['discrete_gpu'], 'NVIDIA GPU')  # 应该被设置


if __name__ == "__main__":
    unittest.main()