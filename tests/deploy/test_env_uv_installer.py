#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UV 安装器测试"""

import unittest
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from magicm.deploy.enviroment.env_uv_installer import uv_util


class TestUvUtil(unittest.TestCase):
    """uv_util 类测试"""
    
    def setUp(self):
        """测试前准备"""
        # 保存原始平台
        self.original_platform = sys.platform
    
    def tearDown(self):
        """测试后清理"""
        # 恢复原始平台
        sys.platform = self.original_platform
    
    # ==================== installed() 测试 ====================
    
    @patch('shutil.which')
    def test_installed_when_uv_exists(self, mock_which):
        """测试 uv 已安装时返回 True"""
        mock_which.return_value = '/usr/local/bin/uv'
        
        result = uv_util.installed()
        
        self.assertTrue(result)
        mock_which.assert_called_once_with('uv')
    
    @patch('shutil.which')
    def test_installed_when_uv_not_exists(self, mock_which):
        """测试 uv 未安装时返回 False"""
        mock_which.return_value = None
        
        result = uv_util.installed()
        
        self.assertFalse(result)
        mock_which.assert_called_once_with('uv')
    
    # ==================== version() 测试 ====================
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_version_when_uv_installed_success(self, mock_run, mock_installed):
        """测试 uv 已安装且获取版本成功"""
        mock_installed.return_value = True
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="uv 0.6.0\n",
            stderr=""
        )
        
        result = uv_util.version()
        
        self.assertEqual(result, "uv 0.6.0")
        mock_run.assert_called_once_with(['uv', '--version'], capture_output=True, text=True)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_version_when_uv_installed_but_command_fails(self, mock_run, mock_installed):
        """测试 uv 已安装但命令执行失败"""
        mock_installed.return_value = True
        mock_run.return_value = MagicMock(returncode=1, stdout="", stderr="error")
        
        result = uv_util.version()
        
        self.assertIsNone(result)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    def test_version_when_uv_not_installed(self, mock_installed):
        """测试 uv 未安装时返回 None"""
        mock_installed.return_value = False
        
        result = uv_util.version()
        
        self.assertIsNone(result)
        mock_installed.assert_called_once()
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_version_handles_exception(self, mock_run, mock_installed):
        """测试版本获取时的异常处理"""
        mock_installed.return_value = True
        mock_run.side_effect = subprocess.SubprocessError("Command failed")
        
        result = uv_util.version()
        
        self.assertIsNone(result)
    
    # ==================== install() 测试 ====================
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    def test_install_when_already_installed(self, mock_installed):
        """测试 uv 已安装时直接返回 True"""
        mock_installed.return_value = True
        
        result = uv_util.install()
        
        self.assertTrue(result)
        mock_installed.assert_called_once()
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_on_linux_success(self, mock_run, mock_installed):
        """测试 Linux 系统安装成功"""
        mock_installed.return_value = False
        mock_run.return_value = MagicMock(returncode=0)
        
        # 模拟 Linux 平台
        sys.platform = 'linux'
        result = uv_util.install()
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        # 验证使用正确的命令
        args = mock_run.call_args[0][0]
        self.assertEqual(args[0], 'sh')
        self.assertIn('install.sh', args[2])
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_on_macos_success(self, mock_run, mock_installed):
        """测试 macOS 系统安装成功"""
        mock_installed.return_value = False
        mock_run.return_value = MagicMock(returncode=0)
        
        # 模拟 macOS 平台
        sys.platform = 'darwin'
        result = uv_util.install()
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        # 验证使用正确的命令
        args = mock_run.call_args[0][0]
        self.assertEqual(args[0], 'sh')
        self.assertIn('install.sh', args[2])
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_on_windows_success(self, mock_run, mock_installed):
        """测试 Windows 系统安装成功"""
        mock_installed.return_value = False
        mock_run.return_value = MagicMock(returncode=0)
        
        # 模拟 Windows 平台
        sys.platform = 'win32'
        result = uv_util.install()
        
        self.assertTrue(result)
        mock_run.assert_called_once()
        # 验证使用正确的命令
        args = mock_run.call_args[0][0]
        self.assertEqual(args[0], 'powershell')
        self.assertIn('install.ps1', args[2])
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_failure_on_linux(self, mock_run, mock_installed):
        """测试 Linux 系统安装失败"""
        mock_installed.return_value = False
        mock_run.side_effect = subprocess.CalledProcessError(1, 'cmd', stderr='Installation failed')
        
        sys.platform = 'linux'
        result = uv_util.install()
        
        self.assertFalse(result)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_general_exception(self, mock_run, mock_installed):
        """测试安装过程中的一般异常"""
        mock_installed.return_value = False
        mock_run.side_effect = Exception("Network error")
        
        sys.platform = 'linux'
        result = uv_util.install()
        
        self.assertFalse(result)
    
    # ==================== ensure() 测试 ====================
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    def test_ensure_when_already_installed(self, mock_installed):
        """测试 ensure 时 uv 已安装"""
        mock_installed.return_value = True
        
        result = uv_util.ensure()
        
        self.assertTrue(result)
        mock_installed.assert_called_once()
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.install')
    def test_ensure_when_not_installed_and_install_success(self, mock_install, mock_installed):
        """测试 ensure 时 uv 未安装但安装成功"""
        mock_installed.return_value = False
        mock_install.return_value = True
        
        result = uv_util.ensure()
        
        self.assertTrue(result)
        mock_installed.assert_called_once()
        mock_install.assert_called_once()
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.install')
    def test_ensure_when_not_installed_and_install_fails(self, mock_install, mock_installed):
        """测试 ensure 时 uv 未安装且安装失败"""
        mock_installed.return_value = False
        mock_install.return_value = False
        
        result = uv_util.ensure()
        
        self.assertFalse(result)
        mock_installed.assert_called_once()
        mock_install.assert_called_once()
    
    # ==================== 集成测试 ====================
    
    @patch('shutil.which')
    @patch('subprocess.run')
    def test_full_workflow_uv_installed(self, mock_run, mock_which):
        """测试完整工作流：uv 已安装"""
        mock_which.return_value = '/usr/local/bin/uv'
        mock_run.return_value = MagicMock(returncode=0, stdout="uv 0.6.0\n")
        
        # 检查安装状态
        self.assertTrue(uv_util.installed())
        
        # 获取版本
        version = uv_util.version()
        self.assertEqual(version, "uv 0.6.0")
        
        # ensure 应该直接返回 True
        self.assertTrue(uv_util.ensure())
    
    @patch('shutil.which')
    @patch('subprocess.run')
    def test_full_workflow_uv_not_installed(self, mock_run, mock_which):
        """测试完整工作流：uv 未安装"""
        # 第一次检查：未安装
        mock_which.return_value = None
        
        self.assertFalse(uv_util.installed())
        
        # 模拟安装成功
        mock_which.side_effect = [None, '/usr/local/bin/uv']
        mock_run.return_value = MagicMock(returncode=0)
        
        sys.platform = 'linux'
        
        # 安装
        install_result = uv_util.install()
        self.assertTrue(install_result)


class TestUvUtilIntegration(unittest.TestCase):
    """uv_util 集成测试（可能实际调用系统命令）"""
    
    def test_actual_uv_check(self):
        """测试实际检查 uv 是否安装（不执行安装）"""
        is_installed = uv_util.installed()
        self.assertIsInstance(is_installed, bool)
    
    def test_actual_version_check(self):
        """测试实际获取版本（如果已安装）"""
        if uv_util.installed():
            version = uv_util.version()
            self.assertIsNotNone(version)
            self.assertIn('uv', version.lower())
        else:
            self.assertIsNone(uv_util.version())


class TestUvUtilEdgeCases(unittest.TestCase):
    """边界情况测试"""
    
    @patch('shutil.which')
    def test_installed_with_path_traversal(self, mock_which):
        """测试 uv 路径包含特殊字符"""
        mock_which.return_value = '/path with spaces/uv'
        
        result = uv_util.installed()
        
        self.assertTrue(result)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_version_with_empty_output(self, mock_run, mock_installed):
        """测试版本命令返回空输出"""
        mock_installed.return_value = True
        mock_run.return_value = MagicMock(returncode=0, stdout="", stderr="")
        
        result = uv_util.version()
        
        self.assertEqual(result, "")
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_version_with_unicode_output(self, mock_run, mock_installed):
        """测试版本命令返回 Unicode 输出"""
        mock_installed.return_value = True
        mock_run.return_value = MagicMock(
            returncode=0, 
            stdout="uv 0.6.0 (中文测试)\n",
            stderr=""
        )
        
        result = uv_util.version()
        
        self.assertIsNotNone(result)
        self.assertIn("uv", result)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_timeout_handling(self, mock_run, mock_installed):
        """测试安装超时处理"""
        mock_installed.return_value = False
        mock_run.side_effect = subprocess.TimeoutExpired('cmd', 30)
        
        sys.platform = 'linux'
        result = uv_util.install()
        
        self.assertFalse(result)
    
    @patch('magicm.deploy.enviroment.env_uv_installer.uv_util.installed')
    @patch('subprocess.run')
    def test_install_permission_denied(self, mock_run, mock_installed):
        """测试安装权限不足"""
        mock_installed.return_value = False
        mock_run.side_effect = PermissionError("Permission denied")
        
        sys.platform = 'linux'
        result = uv_util.install()
        
        self.assertFalse(result)
    
    @patch('shutil.which')
    def test_installed_multiple_calls_caching(self, mock_which):
        """测试多次调用 installed()"""
        mock_which.return_value = '/usr/bin/uv'
        
        result1 = uv_util.installed()
        result2 = uv_util.installed()
        
        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertEqual(mock_which.call_count, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)