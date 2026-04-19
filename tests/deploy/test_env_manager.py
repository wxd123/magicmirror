#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EnvManager 测试类"""

import unittest
import tempfile
import shutil
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
project_root = Path(__file__).parent.parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from magicm.deploy.enviroment.env_manage import EnvManager


class TestEnvManager(unittest.TestCase):
    """EnvManager 测试类"""
    
    def setUp(self):
        """测试前准备 - 创建临时目录"""
        self.temp_dir = tempfile.mkdtemp()
        self.env_name = "test_env"
        self.env_path = Path(self.temp_dir) / self.env_name
        self.manager = EnvManager(self.env_name, self.env_path, "3.11")
    
    def tearDown(self):
        """测试后清理 - 删除临时目录"""
        if self.temp_dir and Path(self.temp_dir).exists():
            shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    # ==================== 初始化测试 ====================
    
    def test_init(self):
        """测试初始化"""
        self.assertEqual(self.manager.name, self.env_name)
        self.assertEqual(self.manager.path, self.env_path)
        self.assertEqual(self.manager.python_version, "3.11")
        self.assertIn(self.manager._bin_dir, ['bin', 'Scripts'])
    
    def test_init_with_path_object(self):
        """测试使用 Path 对象初始化"""
        manager = EnvManager("test", Path("/tmp/test"))
        self.assertEqual(manager.path, Path("/tmp/test"))
    
    def test_init_with_string_path(self):
        """测试使用字符串路径初始化"""
        manager = EnvManager("test", "/tmp/test")
        self.assertEqual(manager.path, Path("/tmp/test"))
    
    # ==================== 属性测试 ====================
    
    def test_python_path_property(self):
        """测试 _python_path 属性"""
        python_path = self.manager._python_path
        expected_name = 'python.exe' if sys.platform == 'win32' else 'python'
        self.assertEqual(python_path.name, expected_name)
        self.assertEqual(python_path.parent, self.env_path / self.manager._bin_dir)
    
    def test_pip_path_property(self):
        """测试 _pip_path 属性"""
        pip_path = self.manager._pip_path
        expected_name = 'pip.exe' if sys.platform == 'win32' else 'pip'
        self.assertEqual(pip_path.name, expected_name)
        self.assertEqual(pip_path.parent, self.env_path / self.manager._bin_dir)
    
    # ==================== exists 测试 ====================
    
    def test_exists_when_not_created(self):
        """测试环境未创建时 exists 返回 False"""
        self.assertFalse(self.manager.exists())
    
    def test_exists_when_created(self):
        """测试环境创建后 exists 返回 True"""
        self.manager.create()
        self.assertTrue(self.manager.exists())
    
    def test_exists_with_partial_files(self):
        """测试只有部分文件时 exists 返回 False"""
        self.env_path.mkdir(parents=True, exist_ok=True)
        self.assertFalse(self.manager.exists())
    
    # ==================== create 测试 ====================
    
    def test_create_success(self):
        """测试成功创建环境"""
        result = self.manager.create()
        self.assertTrue(result)
        self.assertTrue(self.manager.exists())
        self.assertTrue(self.manager._python_path.exists())
    
    def test_create_when_already_exists(self):
        """测试环境已存在时创建失败"""
        self.manager.create()
        result = self.manager.create()
        self.assertFalse(result)
    
    def test_create_creates_parent_dirs(self):
        """测试创建时自动创建父目录"""
        deep_path = self.env_path / "nested" / "deep" / "path"
        manager = EnvManager(self.env_name, deep_path)
        manager.create()
        self.assertTrue(deep_path.exists())
    
    @patch('subprocess.run')
    def test_create_subprocess_failure(self, mock_run):
        """测试 subprocess 失败时的处理"""
        mock_run.return_value = MagicMock(
            returncode=1,
            stderr="Error creating venv"
        )
        result = self.manager.create()
        self.assertFalse(result)
    
    # ==================== delete 测试 ====================
    
    def test_delete_success(self):
        """测试成功删除环境"""
        self.manager.create()
        self.assertTrue(self.manager.exists())
        
        result = self.manager.delete()
        self.assertTrue(result)
        self.assertFalse(self.manager.exists())
    
    def test_delete_when_not_exists(self):
        """测试删除不存在的环境"""
        result = self.manager.delete()
        self.assertFalse(result)
    
    def test_delete_removes_directory(self):
        """测试删除会移除整个目录"""
        self.manager.create()
        test_file = self.env_path / "test.txt"
        test_file.write_text("test")
        
        self.manager.delete()
        self.assertFalse(self.env_path.exists())
    
    # ==================== run 测试 ====================
    
    def test_run_success(self):
        """测试成功运行命令"""
        self.manager.create()
        result = self.manager.run(['-c', 'print("hello")'])
        self.assertEqual(result.returncode, 0)
        self.assertIn("hello", result.stdout)
    
    def test_run_when_env_not_exists(self):
        """测试环境不存在时运行命令"""
        with self.assertRaises(RuntimeError) as context:
            self.manager.run(['--version'])
        self.assertIn("环境不存在", str(context.exception))
    
    def test_run_with_args(self):
        """测试带参数运行"""
        self.manager.create()
        result = self.manager.run(['-c', 'import sys; print(sys.version[:3])'])
        self.assertEqual(result.returncode, 0)
        self.assertTrue(result.stdout.strip().startswith('3.'))
    
    def test_run_captures_stderr(self):
        """测试捕获 stderr"""
        self.manager.create()
        result = self.manager.run(['-c', 'import sys; sys.stderr.write("error msg")'])
        self.assertEqual(result.stderr, "error msg")
    
    # ==================== install 测试 ====================
    
    def test_install_success(self):
        """测试成功安装包"""
        self.manager.create()
        # 安装一个小包进行测试
        result = self.manager.install('six')
        self.assertTrue(result)
    
    def test_install_when_env_not_exists(self):
        """测试环境不存在时安装包"""
        with self.assertRaises(RuntimeError):
            self.manager.install('requests')
    
    def test_install_invalid_package(self):
        """测试安装无效包"""
        self.manager.create()
        result = self.manager.install('this_package_does_not_exist_xyz')
        self.assertFalse(result)
    
    # ==================== 集成测试 ====================
    
    def test_full_workflow(self):
        """测试完整工作流：创建 -> 安装 -> 运行 -> 删除"""
        # 创建
        self.assertTrue(self.manager.create())
        self.assertTrue(self.manager.exists())
        
        # 安装
        self.assertTrue(self.manager.install('six'))
        
        # 运行验证
        result = self.manager.run(['-c', 'import six; print(six.__version__)'])
        self.assertEqual(result.returncode, 0)
        
        # 删除
        self.assertTrue(self.manager.delete())
        self.assertFalse(self.manager.exists())
    
    def test_multiple_environments(self):
        """测试多个环境独立运行"""
        env2_path = Path(self.temp_dir) / "test_env2"
        manager2 = EnvManager("test_env2", env2_path)
        
        # 创建两个环境
        self.manager.create()
        manager2.create()
        
        # 验证独立性
        self.assertTrue(self.manager.exists())
        self.assertTrue(manager2.exists())
        self.assertNotEqual(self.manager._python_path, manager2._python_path)
        
        # 删除第一个
        self.manager.delete()
        self.assertFalse(self.manager.exists())
        self.assertTrue(manager2.exists())
    
    # ==================== 边界测试 ====================
    
    def test_path_with_spaces(self):
        """测试路径包含空格"""
        space_path = Path(self.temp_dir) / "test env with spaces"
        manager = EnvManager("test", space_path)
        result = manager.create()
        self.assertTrue(result)
        self.assertTrue(manager.exists())
    
    def test_path_with_special_chars(self):
        """测试路径包含特殊字符"""
        special_path = Path(self.temp_dir) / "test_env_中文_@#$"
        manager = EnvManager("test", special_path)
        result = manager.create()
        self.assertTrue(result)
        self.assertTrue(manager.exists())
    
    def test_long_name(self):
        """测试长名称"""
        long_name = "a" * 200
        long_path = Path(self.temp_dir) / long_name
        manager = EnvManager(long_name, long_path)
        result = manager.create()
        self.assertTrue(result)
        self.assertTrue(manager.exists())


class TestEnvManagerPerformance(unittest.TestCase):
    """性能测试"""
    
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_create_performance(self):
        """测试创建性能（应该在合理时间内完成）"""
        import time
        manager = EnvManager("perf_test", Path(self.temp_dir) / "perf_test")
        
        start = time.time()
        manager.create()
        duration = time.time() - start
        
        # 创建环境应该在 5 秒内完成
        self.assertLess(duration, 5)
    
    def test_multiple_create_delete(self):
        """测试多次创建删除"""
        for i in range(5):
            env_path = Path(self.temp_dir) / f"test_{i}"
            manager = EnvManager(f"test_{i}", env_path)
            self.assertTrue(manager.create())
            self.assertTrue(manager.delete())


if __name__ == '__main__':
    unittest.main(verbosity=2)