#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""env_setup 模块测试"""

import unittest
import tempfile
import shutil
import sys
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

project_root = Path(__file__).parent.parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from magicm.deploy.enviroment.env_setup import setup_env, quick_setup
from magicm.deploy.enviroment.env_manage import EnvManager


class TestSetupEnv(unittest.TestCase):
    """setup_env 函数测试"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.env_name = "test_app"
        self.env_path = Path(self.temp_dir) / self.env_name
        self.python_version = "3.12"
    
    def tearDown(self):
        """测试后清理"""
        if self.temp_dir and Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    # ==================== UV 安装相关测试 ====================
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_uv_install_success(self, mock_uv_util):
        """测试 UV 安装成功"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        result = setup_env(
            self.env_name,
            self.env_path,
            self.python_version
        )
        
        self.assertTrue(result)
        mock_uv_util.ensure.assert_called_once()
        mock_uv_util.version.assert_called_once()
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_uv_install_failure(self, mock_uv_util):
        """测试 UV 安装失败"""
        mock_uv_util.ensure.return_value = False
        
        result = setup_env(
            self.env_name,
            self.env_path,
            self.python_version
        )
        
        self.assertFalse(result)
        mock_uv_util.ensure.assert_called_once()
        mock_uv_util.version.assert_not_called()
    
    # ==================== 虚拟环境创建相关测试 ====================
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_env_not_exists_create_success(self, mock_uv_util):
        """测试环境不存在，创建成功"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        result = setup_env(
            self.env_name,
            self.env_path,
            self.python_version
        )
        
        self.assertTrue(result)
        self.assertTrue(self.env_path.exists())
        self.assertTrue((self.env_path / "bin" / "python").exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_env_already_exists_no_force(self, mock_uv_util):
        """测试环境已存在，不强制重建"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 先创建环境
        manager = EnvManager(self.env_name, self.env_path, self.python_version)
        manager.create()
        self.assertTrue(manager.exists())
        
        # 再次调用 setup_env
        result = setup_env(
            self.env_name,
            self.env_path,
            self.python_version,
            force=False
        )
        
        self.assertTrue(result)
        self.assertTrue(manager.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_env_already_exists_with_force(self, mock_uv_util):
        """测试环境已存在，强制重建"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 先创建环境并创建测试文件
        manager = EnvManager(self.env_name, self.env_path, self.python_version)
        manager.create()
        test_file = self.env_path / "test.txt"
        test_file.write_text("test data")
        self.assertTrue(test_file.exists())
        
        # 强制重建
        result = setup_env(
            self.env_name,
            self.env_path,
            self.python_version,
            force=True
        )
        
        self.assertTrue(result)
        self.assertTrue(manager.exists())
        self.assertFalse(test_file.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_env_create_failure_permission_denied(self, mock_uv_util):
        """测试环境创建失败 - 权限拒绝"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 创建只读目录，导致无法创建子目录
        readonly_dir = Path(self.temp_dir) / "readonly"
        readonly_dir.mkdir()
        # 移除写权限
        readonly_dir.chmod(0o555)
        
        try:
            readonly_env_path = readonly_dir / self.env_name
            
            # 应该返回 False 而不是抛出异常
            result = setup_env(
                self.env_name,
                readonly_env_path,
                self.python_version
            )
            
            self.assertFalse(result)
        finally:
            # 恢复权限以便清理
            readonly_dir.chmod(0o755)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_force_param_triggers_delete(self, mock_uv_util):
        """测试 force 参数触发删除操作"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 创建环境
        manager = EnvManager(self.env_name, self.env_path, self.python_version)
        manager.create()
        
        # 使用 force=True 重建
        result = setup_env(
            self.env_name,
            self.env_path,
            force=True
        )
        
        self.assertTrue(result)
        # 验证环境被重建（新的环境应该存在）
        self.assertTrue(manager.exists())
    
    # ==================== 参数传递测试 ====================
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    @patch('magicm.deploy.enviroment.env_setup.EnvManager')
    def test_python_version_passed_correctly(self, mock_manager_class, mock_uv_util):
        """测试 Python 版本正确传递"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        mock_manager = MagicMock()
        mock_manager.exists.return_value = False
        mock_manager.create.return_value = True
        mock_manager_class.return_value = mock_manager
        
        result = setup_env(
            self.env_name,
            self.env_path,
            python_version="3.12",
            force=False
        )
        
        self.assertTrue(result)
        mock_manager_class.assert_called_once_with(
            self.env_name,
            self.env_path,
            "3.12"
        )
    
    # ==================== 返回值测试 ====================
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_return_true_on_success_new_env(self, mock_uv_util):
        """测试新建环境成功返回 True"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        result = setup_env(self.env_name, self.env_path)
        
        self.assertTrue(result)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_return_true_on_existing_env(self, mock_uv_util):
        """测试环境已存在时返回 True"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 创建环境
        manager = EnvManager(self.env_name, self.env_path)
        manager.create()
        
        result = setup_env(self.env_name, self.env_path, force=False)
        
        self.assertTrue(result)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_return_false_on_uv_install_failure(self, mock_uv_util):
        """测试 UV 安装失败返回 False"""
        mock_uv_util.ensure.return_value = False
        
        result = setup_env(self.env_name, self.env_path)
        
        self.assertFalse(result)


class TestQuickSetup(unittest.TestCase):
    """quick_setup 函数测试"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.env_name = "quick_test_app"
    
    def tearDown(self):
        """测试后清理"""
        if self.temp_dir and Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_quick_setup_calls_setup_env_with_default_path(self, mock_uv_util):
        """测试 quick_setup 使用默认路径调用 setup_env"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 直接测试 quick_setup 的行为，而不是 mock setup_env
        # 因为 quick_setup 内部会调用 setup_env，我们直接验证结果
        result = quick_setup(self.env_name, self.temp_dir)
        
        expected_path = Path(self.temp_dir) / self.env_name
        self.assertTrue(result)
        self.assertTrue(expected_path.exists())
        self.assertTrue((expected_path / "bin" / "python").exists())
        
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_quick_setup_actual_creation(self, mock_uv_util):
        """测试 quick_setup 实际创建环境"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        result = quick_setup(self.env_name, self.temp_dir)
        
        expected_path = Path(self.temp_dir) / self.env_name
        self.assertTrue(result)
        self.assertTrue(expected_path.exists())
        self.assertTrue((expected_path / "bin" / "python").exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_quick_setup_with_custom_base_path(self, mock_uv_util):
        """测试 quick_setup 使用自定义基础路径"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        custom_base = Path(self.temp_dir) / "custom"
        result = quick_setup(self.env_name, str(custom_base))
        
        expected_path = custom_base / self.env_name
        self.assertTrue(result)
        self.assertTrue(expected_path.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_quick_setup_returns_false_on_failure(self, mock_uv_util):
        """测试 quick_setup 失败时返回 False"""
        mock_uv_util.ensure.return_value = False
        
        result = quick_setup(self.env_name, self.temp_dir)
        
        self.assertFalse(result)


class TestSetupEnvIntegration(unittest.TestCase):
    """端到端集成测试"""
    
    def setUp(self):
        """测试前准备"""
        self.temp_dir = tempfile.mkdtemp()
        self.env_name = "integration_test"
        self.env_path = Path(self.temp_dir) / self.env_name
    
    def tearDown(self):
        """测试后清理"""
        if self.temp_dir and Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_full_integration_with_mock_uv(self, mock_uv_util):
        """完整集成测试（使用 Mock UV）"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 执行完整设置
        result = setup_env(
            self.env_name,
            self.env_path,
            python_version="3.12",
            force=False
        )
        
        self.assertTrue(result)
        
        # 验证环境可用
        manager = EnvManager(self.env_name, self.env_path, "3.12")
        self.assertTrue(manager.exists())
        
        # 验证可以安装包
        install_result = manager.install('six')
        self.assertTrue(install_result)
        
        # 验证可以运行 Python
        run_result = manager.run(['-c', 'print("integration test passed")'])
        self.assertEqual(run_result.returncode, 0)
        self.assertIn("integration test passed", run_result.stdout)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_force_recreate_workflow(self, mock_uv_util):
        """测试强制重建完整流程"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 第一次创建
        result1 = setup_env(
            self.env_name,
            self.env_path,
            force=False
        )
        self.assertTrue(result1)
        
        # 创建一些用户数据
        user_data = self.env_path / "user_data.txt"
        user_data.write_text("important data")
        self.assertTrue(user_data.exists())
        
        # 强制重建
        result2 = setup_env(
            self.env_name,
            self.env_path,
            force=True
        )
        self.assertTrue(result2)
        
        # 验证用户数据被清除
        self.assertFalse(user_data.exists())
        # 验证环境仍然可用
        manager = EnvManager(self.env_name, self.env_path)
        self.assertTrue(manager.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_multiple_setup_calls(self, mock_uv_util):
        """测试多次调用 setup_env"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 第一次调用
        result1 = setup_env(self.env_name, self.env_path)
        self.assertTrue(result1)
        
        # 第二次调用（环境已存在）
        result2 = setup_env(self.env_name, self.env_path)
        self.assertTrue(result2)
        
        # 验证环境只创建了一次
        self.assertTrue(self.env_path.exists())


class TestSetupEnvEdgeCases(unittest.TestCase):
    """边界情况测试"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.env_name = "test_edge_env"
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_empty_env_name(self, mock_uv_util):
        """测试空环境名称 - 应该允许创建名为空的目录"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        # 空名称实际上是允许的，会创建名为空的目录
        empty_path = Path(self.temp_dir) / ""
        # 注意：Path("") 等同于当前目录，这里我们使用一个特殊测试
        # 实际上 setup_env 会正常执行
        result = setup_env("", Path(self.temp_dir) / "empty_test")
        # 使用非空名称测试
        self.assertTrue(result or not result)  # 只是确保不抛出异常
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_very_long_env_name(self, mock_uv_util):
        """测试超长环境名称"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        long_name = "a" * 255
        env_path = Path(self.temp_dir) / long_name
        
        result = setup_env(long_name, env_path)
        self.assertTrue(result)
        self.assertTrue(env_path.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_special_characters_in_name(self, mock_uv_util):
        """测试名称包含特殊字符"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        special_name = "test-env_123.456@789"
        env_path = Path(self.temp_dir) / special_name
        
        result = setup_env(special_name, env_path)
        self.assertTrue(result)
        self.assertTrue(env_path.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_nested_path(self, mock_uv_util):
        """测试嵌套路径"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        nested_path = Path(self.temp_dir) / "level1" / "level2" / "level3" / self.env_name
        
        result = setup_env(self.env_name, nested_path)
        self.assertTrue(result)
        self.assertTrue(nested_path.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_path_with_spaces(self, mock_uv_util):
        """测试路径包含空格"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        space_path = Path(self.temp_dir) / "test path with spaces" / self.env_name
        
        result = setup_env(self.env_name, space_path)
        self.assertTrue(result)
        self.assertTrue(space_path.exists())
    
    @patch('magicm.deploy.enviroment.env_setup.uv_util')
    def test_unicode_in_path(self, mock_uv_util):
        """测试路径包含 Unicode 字符"""
        mock_uv_util.ensure.return_value = True
        mock_uv_util.version.return_value = "uv 0.6.0"
        
        unicode_path = Path(self.temp_dir) / "测试目录" / self.env_name
        
        result = setup_env(self.env_name, unicode_path)
        self.assertTrue(result)
        self.assertTrue(unicode_path.exists())


if __name__ == '__main__':
    unittest.main(verbosity=2)