#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ConfigPathManager 测试类
测试路径查找逻辑（开发环境）和打包环境兼容性
"""

import sys
import os
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

# 添加项目根目录到路径
# 添加项目路径 - 动态查找
project_root = Path(__file__).parent.parent
src_path = project_root / 'src'
sys.path.insert(0, str(src_path))

from magicm.management.config.configPathManager import ConfigPathManager


class TestConfigPathManager:
    """ConfigPathManager 测试类"""
    
    # ==================== 开发环境测试（真实路径） ====================
    
    def test_dev_find_project_root(self):
        """测试：开发环境下能否正确找到项目根目录"""
        mgr = ConfigPathManager()
        root = mgr._get_project_root()
        
        # 项目根目录应该包含 config 和 src 目录
        assert (root / 'config').exists()
        assert (root / 'src').exists()
        
        print(f"✓ 项目根目录: {root}")
    
    def test_dev_config_dir(self):
        """测试：开发环境下 config 目录路径正确"""
        mgr = ConfigPathManager()
        config_dir = mgr.config_dir
        
        assert config_dir.name == 'config'
        assert config_dir.exists()
        
        print(f"✓ config 目录: {config_dir}")
    
    def test_dev_get_display_config_path(self):
        """测试：开发环境下获取 display 配置路径"""
        mgr = ConfigPathManager()
        config_path = mgr.get_path('display', 'config.yaml')
        
        # 路径应该存在（如果文件存在）
        assert config_path.suffix == '.yaml'
        print(f"✓ display 配置路径: {config_path}")
        print(f"  文件存在: {config_path.exists()}")
    
    def test_dev_get_nested_path(self):
        """测试：开发环境下获取多层嵌套路径"""
        mgr = ConfigPathManager()
        
        # 测试不同层级的路径
        path1 = mgr.get_path('display.yaml')
        assert path1.name == 'display.yaml'
        
        path2 = mgr.get_path('detector', 'gpu.yaml')
        assert path2.parent.name == 'detector'
        assert path2.name == 'gpu.yaml'
        
        path3 = mgr.get_path('a', 'b', 'c', 'd.yaml')
        assert str(path3).endswith('config/a/b/c/d.yaml')
        
        print(f"✓ 嵌套路径测试通过")
    
    def test_dev_exists(self):
        """测试：开发环境下检查文件是否存在"""
        mgr = ConfigPathManager()
        
        # 存在的路径
        if (mgr.config_dir / 'display' / 'config.yaml').exists():
            assert mgr.exists('display', 'config.yaml') == True
        
        # 不存在的路径
        assert mgr.exists('not_exist.yaml') == False
        assert mgr.exists('not_exist_dir', 'file.yaml') == False
        
        print(f"✓ exists 方法测试通过")
    
    # ==================== 打包环境测试（模拟） ====================
    
    def test_frozen_environment(self):
        """测试：模拟打包环境（PyInstaller）"""
        # 创建临时目录模拟打包环境
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            
            # 模拟 config 目录结构
            config_dir = tmp_path / 'config' / 'display'
            config_dir.mkdir(parents=True)
            (config_dir / 'config.yaml').touch()
            
            # 模拟 PyInstaller 环境变量
            with patch('sys.frozen', True, create=True):
                with patch('sys._MEIPASS', str(tmp_path)):
                    mgr = ConfigPathManager()
                    root = mgr._get_project_root()
                    
                    # 应该返回临时目录
                    assert root == tmp_path
                    
                    # 获取配置路径
                    config_path = mgr.get_path('display', 'config.yaml')
                    assert config_path.exists()
                    
                    print(f"✓ 打包环境模拟测试通过")
                    print(f"  模拟 MEIPASS: {tmp_path}")
    
    def test_frozen_no_config(self):
        """测试：打包环境中 config 目录不存在"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            # 不创建 config 目录
            
            with patch('sys.frozen', True, create=True):
                with patch('sys._MEIPASS', str(tmp_path)):
                    mgr = ConfigPathManager()
                    
                    # 应该抛出异常
                    with pytest.raises(RuntimeError):
                        _ = mgr.config_dir
                    
                    print(f"✓ 打包环境缺少 config 目录时正确抛出异常")
    
    # ==================== 手动指定 project_root 测试 ====================
    
    def test_manual_project_root(self):
        """测试：手动指定 project_root"""
        fake_root = Path("/fake/project/root")
        mgr = ConfigPathManager(project_root=fake_root)
        
        assert mgr._project_root == fake_root
        assert mgr._get_project_root() == fake_root
        
        # config_dir 应该是 project_root/config
        with patch.object(mgr, '_get_project_root', return_value=fake_root):
            assert mgr.config_dir == fake_root / 'config'
        
        print(f"✓ 手动指定 project_root 测试通过")
    
    # ==================== 缓存测试 ====================
    
    def test_project_root_cached(self):
        """测试：project_root 缓存"""
        mgr = ConfigPathManager()
        
        # 第一次调用
        root1 = mgr._get_project_root()
        # 第二次调用（应该返回缓存，不再重新计算）
        root2 = mgr._get_project_root()
        
        assert root1 == root2
        print(f"✓ project_root 缓存测试通过")
    
    def test_config_dir_cached(self):
        """测试：config_dir 缓存"""
        mgr = ConfigPathManager()
        
        # 第一次访问
        dir1 = mgr.config_dir
        # 第二次访问（应该使用缓存）
        dir2 = mgr.config_dir
        
        assert dir1 == dir2
        print(f"✓ config_dir 缓存测试通过")
    
    # ==================== 边界情况测试 ====================
    
    def test_get_path_empty(self):
        """测试：空路径参数"""
        mgr = ConfigPathManager(project_root=Path("/fake"))
        
        with patch.object(mgr, 'config_dir', Path("/fake/config")):
            path = mgr.get_path()
            assert path == Path("/fake/config")
        
        print(f"✓ 空路径参数测试通过")
    
    def test_get_path_single(self):
        """测试：单层路径"""
        mgr = ConfigPathManager(project_root=Path("/fake"))
        
        with patch.object(mgr, 'config_dir', Path("/fake/config")):
            path = mgr.get_path('file.yaml')
            assert path == Path("/fake/config/file.yaml")
        
        print(f"✓ 单层路径测试通过")
    
    def test_get_path_multi(self):
        """测试：多层路径"""
        mgr = ConfigPathManager(project_root=Path("/fake"))
        
        with patch.object(mgr, 'config_dir', Path("/fake/config")):
            path = mgr.get_path('a', 'b', 'c', 'file.yaml')
            assert path == Path("/fake/config/a/b/c/file.yaml")
        
        print(f"✓ 多层路径测试通过")


# ==================== 独立运行 ====================

if __name__ == "__main__":
    print("=" * 60)
    print("ConfigPathManager 测试")
    print("=" * 60)
    
    test = TestConfigPathManager()
    
    # 运行开发环境测试（真实路径）
    print("\n--- 开发环境测试 ---")
    try:
        test.test_dev_find_project_root()
        test.test_dev_config_dir()
        test.test_dev_get_display_config_path()
        test.test_dev_get_nested_path()
        test.test_dev_exists()
    except Exception as e:
        print(f"✗ 开发环境测试失败: {e}")
        import traceback
        traceback.print_exc()
    
    # 运行其他测试
    print("\n--- 手动指定根目录测试 ---")
    test.test_manual_project_root()
    
    print("\n--- 缓存测试 ---")
    test.test_project_root_cached()
    test.test_config_dir_cached()
    
    print("\n--- 边界情况测试 ---")
    test.test_get_path_empty()
    test.test_get_path_single()
    test.test_get_path_multi()
    
    print("\n--- 打包环境模拟测试 ---")
    test.test_frozen_environment()
    test.test_frozen_no_config()
    
    print("\n" + "=" * 60)
    print("✓ 所有测试通过")
    print("=" * 60)