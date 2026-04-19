# tests/test_system_detector.py

import sys
import unittest
from unittest.mock import patch, MagicMock
import platform

# 添加项目根目录到路径
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from magicm.detector.software.system.sys_detecter import detect


class TestSysDetecter(unittest.TestCase):
    """测试 sys_detecter 模块"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.expected_keys = ['platform', 'name', 'pretty_name']
    
    def test_detect_returns_dict(self):
        """测试 detect 函数返回字典类型"""
        result = detect()
        self.assertIsInstance(result, dict)
    
    def test_detect_contains_required_keys(self):
        """测试 detect 返回的字典包含必需的键"""
        result = detect()
        for key in self.expected_keys:
            self.assertIn(key, result)
    
    def test_detect_no_empty_values(self):
        """测试 detect 返回的值不为空"""
        result = detect()
        for key in self.expected_keys:
            self.assertIsNotNone(result[key])
            self.assertNotEqual(result[key], '')
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_windows_platform(self, mock_sys):
        """测试 Windows 平台检测"""
        mock_sys.platform = 'win32'
        
        with patch('magicm.detector.software.system.sys_detecter.windows_detect') as mock_windows:
            mock_windows.return_value = {
                'name': 'Windows 11 Pro',
                'pretty_name': 'Windows 11 Pro',
                'version': '10.0.22000'
            }
            
            result = detect()
            
            self.assertEqual(result['platform'], 'win32')
            self.assertEqual(result['name'], 'Windows 11 Pro')
            mock_windows.assert_called_once()
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_linux_platform(self, mock_sys):
        """测试 Linux 平台检测"""
        mock_sys.platform = 'linux'
        
        with patch('magicm.detector.software.system.sys_detecter.linux_detect') as mock_linux:
            mock_linux.return_value = {
                'name': 'Ubuntu',
                'pretty_name': 'Ubuntu 22.04 LTS',
                'version': '22.04'
            }
            
            result = detect()
            
            self.assertEqual(result['platform'], 'linux')
            self.assertEqual(result['name'], 'Ubuntu')
            mock_linux.assert_called_once()
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_macos_platform(self, mock_sys):
        """测试 macOS 平台检测"""
        mock_sys.platform = 'darwin'
        
        with patch('magicm.detector.software.system.sys_detecter.mac_detect') as mock_mac:
            mock_mac.return_value = {
                'name': 'macOS',
                'pretty_name': 'macOS Sonoma 14.0',
                'version': '14.0'
            }
            
            result = detect()
            
            self.assertEqual(result['platform'], 'darwin')
            self.assertEqual(result['name'], 'macOS')
            mock_mac.assert_called_once()
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_unknown_platform(self, mock_sys):
        """测试未知平台检测"""
        mock_sys.platform = 'unknown'
        
        with patch('platform.release', return_value='1.0'):
            result = detect()
            
            self.assertEqual(result['platform'], 'unknown')
            self.assertEqual(result['name'], 'unknown 1.0')
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_windows_detection_error(self, mock_sys):
        """测试 Windows 检测出错时的降级处理"""
        mock_sys.platform = 'win32'
        
        with patch('magicm.detector.software.system.sys_detecter.windows_detect') as mock_windows:
            mock_windows.side_effect = Exception('检测失败')
            
            with patch('platform.release', return_value='10.0.22000'):
                result = detect()
                
                self.assertEqual(result['platform'], 'win32')
                self.assertIn('Windows', result['name'])
                self.assertIn('Windows', result['pretty_name'])
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_linux_detection_error(self, mock_sys):
        """测试 Linux 检测出错时的降级处理"""
        mock_sys.platform = 'linux'
        
        with patch('magicm.detector.software.system.sys_detecter.linux_detect') as mock_linux:
            mock_linux.side_effect = Exception('检测失败')
            
            with patch('platform.release', return_value='5.15.0'):
                result = detect()
                
                self.assertEqual(result['platform'], 'linux')
                self.assertIn('Linux', result['name'])
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_macos_detection_error(self, mock_sys):
        """测试 macOS 检测出错时的降级处理"""
        mock_sys.platform = 'darwin'
        
        with patch('magicm.detector.software.system.sys_detecter.mac_detect') as mock_mac:
            mock_mac.side_effect = Exception('检测失败')
            
            with patch('platform.release', return_value='22.0.0'):
                result = detect()
                
                self.assertEqual(result['platform'], 'darwin')
                self.assertIn('Mac', result['name'])
    
    def test_detect_real_platform(self):
        """测试真实平台的检测（集成测试）"""
        result = detect()
        
        # 根据实际运行平台验证
        if sys.platform == 'win32':
            self.assertEqual(result['platform'], 'win32')
        elif sys.platform.startswith('linux'):
            self.assertEqual(result['platform'], 'linux')
        elif sys.platform == 'darwin':
            self.assertEqual(result['platform'], 'darwin')
        
        # 验证基本字段存在且非空
        self.assertIsNotNone(result['name'])
        self.assertIsNotNone(result['pretty_name'])
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    @patch('magicm.detector.software.system.sys_detecter.linux_detect')
    def test_detect_preserves_original_keys(self, mock_linux, mock_sys):
        """测试检测结果保留原有键值，并正确合并子检测器的结果"""
        mock_sys.platform = 'linux'
        mock_linux.return_value = {
            'name': 'Ubuntu',
            'pretty_name': 'Ubuntu 22.04',
            'version': '22.04',
            'codename': 'Jammy'
        }
        
        result = detect()
        
        # 原有键存在
        self.assertIn('platform', result)
        # 子检测器的额外键被合并
        self.assertEqual(result['version'], '22.04')
        self.assertEqual(result['codename'], 'Jammy')
    
    @patch('magicm.detector.software.system.sys_detecter.sys')
    def test_detect_global_exception_handling(self, mock_sys):
        """测试全局异常处理"""
        # 修复：正确模拟 sys.platform 引发异常
        # 创建一个属性抛出异常的对象
        class MockSys:
            @property
            def platform(self):
                raise Exception('全局错误')
        
        mock_sys_instance = MockSys()
        
        # 使用 side_effect 模拟整个模块
        with patch('magicm.detector.software.system.sys_detecter.sys', mock_sys_instance):
            result = detect()
            
            # 验证返回了默认值
            self.assertEqual(result['platform'], '未知')
            self.assertEqual(result['name'], '未知')
            self.assertEqual(result['pretty_name'], '未知系统')


class TestSysDetecterIntegration(unittest.TestCase):
    """集成测试类 - 测试与其他模块的交互"""
    
    def test_import_modules(self):
        """测试能否正常导入依赖模块"""
        try:
            from magicm.detector.software.system import linux_detecter
            from magicm.detector.software.system import win_detecter
            from magicm.detector.software.system import mac_detecter
        except ImportError as e:
            self.fail(f"导入模块失败: {e}")


if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)