#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
操作系统检测模块的单元测试
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from magicm.detector.software.system import sys_detecter


class TestSystemDetector(unittest.TestCase):
    """测试系统检测器"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.original_platform = sys.platform
    
    def tearDown(self):
        """测试后的清理工作"""
        sys.platform = self.original_platform
    
    # ==================== 平台检测测试 ====================
    
    def test_detect_windows(self):
        """测试 Windows 平台检测"""
        sys.platform = 'win32'
        
        with patch('magicm.detector.software.system.sys_detecter.windows_detect') as mock_windows:
            mock_windows.return_value = {'name': 'Windows 11', 'pretty_name': 'Windows 11 Pro'}
            result = sys_detecter.detect()
            
            self.assertIsInstance(result, dict)
            self.assertEqual(result.get('platform'), 'win32')
            self.assertEqual(result.get('name'), 'Windows 11')
            self.assertEqual(result.get('pretty_name'), 'Windows 11 Pro')
    
    def test_detect_linux(self):
        """测试 Linux 平台检测"""
        sys.platform = 'linux'
        
        with patch('magicm.detector.software.system.sys_detecter.linux_detect') as mock_linux:
            mock_linux.return_value = {'name': 'Ubuntu', 'pretty_name': 'Ubuntu 22.04'}
            result = sys_detecter.detect()
            
            self.assertIsInstance(result, dict)
            self.assertEqual(result.get('platform'), 'linux')
            self.assertEqual(result.get('name'), 'Ubuntu')
            self.assertEqual(result.get('pretty_name'), 'Ubuntu 22.04')
    
    def test_detect_macos(self):
        """测试 macOS 平台检测"""
        sys.platform = 'darwin'
        
        with patch('platform.mac_ver', return_value=('14.0', ('', '', ''), '')):
            result = sys_detecter.detect()
            
            self.assertIsInstance(result, dict)
            self.assertEqual(result.get('platform'), 'darwin')
            self.assertEqual(result.get('name'), 'macOS 14.0')
            self.assertEqual(result.get('pretty_name'), 'macOS 14.0')
    
    def test_detect_unknown_platform(self):
        """测试未知平台检测"""
        sys.platform = 'unknown'
        
        with patch('platform.release', return_value='1.0'):
            result = sys_detecter.detect()
            
            self.assertIsInstance(result, dict)
            self.assertEqual(result.get('platform'), 'unknown')
            self.assertEqual(result.get('name'), 'unknown 1.0')
            self.assertEqual(result.get('pretty_name'), 'unknown 1.0')
    
    # ==================== 异常处理测试 ====================
    
    def test_detect_exception_handling(self):
        """测试异常处理"""
        sys.platform = 'win32'
        
        # 模拟 windows_detect 抛出异常
        with patch('magicm.detector.software.system.sys_detecter.windows_detect') as mock_windows:
            mock_windows.side_effect = Exception("测试异常")
            with patch('platform.release', return_value='10.0'):
                result = sys_detecter.detect()
                
                self.assertIsInstance(result, dict)
                self.assertEqual(result.get('platform'), 'win32')
                # 异常时应该有默认值
                self.assertIsNotNone(result.get('name'))
                self.assertIsNotNone(result.get('pretty_name'))
    
    def test_detect_linux_exception(self):
        """测试 Linux 检测异常"""
        sys.platform = 'linux'
        
        with patch('magicm.detector.software.system.sys_detecter.linux_detect') as mock_linux:
            mock_linux.side_effect = Exception("Linux 检测失败")
            with patch('platform.release', return_value='5.15.0'):
                result = sys_detecter.detect()
                
                self.assertIsInstance(result, dict)
                self.assertEqual(result.get('platform'), 'linux')
                self.assertEqual(result.get('name'), 'Linux 5.15.0')
                self.assertEqual(result.get('pretty_name'), 'Linux 5.15.0')
    
    # ==================== 返回值结构测试 ====================
    
    def test_return_structure(self):
        """测试返回值结构"""
        sys.platform = 'linux'
        
        with patch('magicm.detector.software.system.sys_detecter.linux_detect') as mock_linux:
            mock_linux.return_value = {'name': 'Ubuntu', 'pretty_name': 'Ubuntu 22.04'}
            result = sys_detecter.detect()
            
            # 检查必需的键
            self.assertIn('platform', result)
            self.assertIn('name', result)
            self.assertIn('pretty_name', result)
    
    def test_return_values_not_empty(self):
        """测试返回值不为空"""
        sys.platform = 'win32'
        
        with patch('magicm.detector.software.system.sys_detecter.windows_detect') as mock_windows:
            mock_windows.return_value = {'name': 'Windows 10', 'pretty_name': 'Windows 10 Pro'}
            result = sys_detecter.detect()
            
            # 检查值不为空
            self.assertTrue(result.get('platform'))
            self.assertTrue(result.get('name'))
            self.assertTrue(result.get('pretty_name'))
            self.assertNotEqual(result.get('name'), '未知')
            self.assertNotEqual(result.get('pretty_name'), '未知系统')


class TestSystemDetectorIntegration(unittest.TestCase):
    """集成测试 - 需要真实系统环境"""
    
    def test_real_system_detection(self):
        """测试真实系统检测"""
        import pytest
        pytest.skip("集成测试，需要真实系统环境")
        
        result = sys_detecter.detect()
        
        self.assertIsInstance(result, dict)
        self.assertIn('platform', result)
        self.assertIn('name', result)
        self.assertIn('pretty_name', result)
        self.assertNotEqual(result.get('platform'), '未知')
        self.assertNotEqual(result.get('name'), '未知')
        self.assertNotEqual(result.get('pretty_name'), '未知系统')
        
        print(f"\n检测到的系统: {result}")


if __name__ == "__main__":
    # 运行测试
    unittest.main(verbosity=2)