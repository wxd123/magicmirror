#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/display.py
"""
硬件检测结果显示模块（主入口）

这是对外的主要接口
"""

from typing import Dict, Any, Optional
from magicm.management.config.configManager import ConfigManager
from .disp.hardware_rating import HardwareRating
from .disp.formatter import HardwareFormatter


class HardwareDisplay:
    """硬件检测结果展示类（门面模式）"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None):
        """
        初始化硬件显示器
        
        Args:
            config: 配置字典（可选）
            config_path: 配置文件路径（可选）
        """
        # 加载配置
        self.config_manager = ConfigManager()
        
        if config is not None:
            self.config = config
        elif config_path is not None:
            self.config = self.config_manager.load('display', config_path)
        else:
            self.config = self.config_manager.load('display', 'config.yaml')
        
        # 初始化评级计算器和格式化器
        self.rating = HardwareRating(self.config)
        self.formatter = HardwareFormatter(self.rating)
        
        # 保持向后兼容的属性
        self.width = 50
    
    # ==================== 主要显示方法 ====================
    
    def display_all(self, system_info: Dict[str, Any]):
        """
        显示所有硬件信息（控制台输出）
        
        Args:
            system_info: 系统信息，新格式：
                {
                    'system': {...},   # 统一接口格式
                    'cpu': {...},
                    'gpu': {...},
                    'mem': {...},
                    'env': {...}
                }
        """
        # 直接透传给 formatter，保持新格式
        self.formatter.display_all(system_info)
    
    def format_text(self, system_info: Dict[str, Any], cpu_info: Dict[str, Any],
                   gpu_info: Dict[str, Any], memory_info: Dict[str, Any],
                   width: int = 100) -> str:
        """
        返回格式化的文本
        
        Args:
            system_info: 系统信息
            cpu_info: CPU信息
            gpu_info: GPU信息
            memory_info: 内存信息
            width: 文本宽度
            
        Returns:
            格式化的文本字符串
        """
        # 统一格式
        wrapped_info = {
            'system': system_info,
            'cpu': cpu_info,
            'gpu': gpu_info,
            'mem': memory_info
        }
        return self.formatter.format_as_text(wrapped_info, width)
    
    # ==================== 评级方法 ====================
    
    def get_gpu_rating(self, gpu_name: str) -> str:
        """获取GPU评级"""
        return self.rating.get_gpu_rating(gpu_name)
    
    def get_vram_rating(self, vram_gb: int) -> str:
        """获取显存评级"""
        return self.rating.get_vram_rating(vram_gb)
    
    def get_driver_rating(self, driver_version: str) -> str:
        """获取驱动评级"""
        return self.rating.get_driver_rating(driver_version)
    
    def get_system_rating(self, os_name: str) -> str:
        """获取系统评级"""
        return self.rating.get_system_rating(os_name)
    
    def get_cpu_rating(self, cpu_model: str) -> str:
        """获取CPU评级"""
        return self.rating.get_cpu_rating(cpu_model)
    
    def get_memory_rating(self, memory_gb: int) -> str:
        """获取内存评级"""
        return self.rating.get_memory_rating(memory_gb)
    
    # ==================== 显示方法 ====================
    
    def show_banner(self):
        """显示欢迎横幅"""
        self.formatter.show_banner()
    
    def show_footer(self):
        """显示页脚"""
        self.formatter.show_footer()
    
    # ==================== 配置重载方法 ====================
    
    def reload_config(self, config_path: Optional[str] = None):
        """
        重新加载配置
        
        Args:
            config_path: 配置文件路径（可选）
        """
        if config_path:
            self.config = self.config_manager.load('display', config_path)
        else:
            self.config = self.config_manager.load('display', 'config.yaml')
        
        # 重新初始化评级计算器
        self.rating = HardwareRating(self.config)
        self.formatter = HardwareFormatter(self.rating, self.width)


# ==================== 便捷函数 ====================

def create_display(config_path: Optional[str] = None) -> HardwareDisplay:
    """创建硬件显示器实例"""
    return HardwareDisplay(config_path=config_path)


def display_hardware_info(system_info: Dict[str, Any], 
                         config_path: Optional[str] = None):
    """
    显示硬件信息（便捷函数）
    
    Args:
        system_info: 系统信息，新格式：
            {
                'system': {...},   # 统一接口格式
                'cpu': {...},
                'gpu': {...},
                'mem': {...},
                'env': {...}
            }
        config_path: 配置文件路径
    """
    display = HardwareDisplay(config_path=config_path)
    display.display_all(system_info)


def format_hardware_info(system_info: Dict[str, Any], cpu_info: Dict[str, Any],
                        gpu_info: Dict[str, Any], memory_info: Dict[str, Any],
                        config_path: Optional[str] = None, width: int = 100) -> str:
    """
    格式化硬件信息为文本（便捷函数）
    
    Args:
        system_info: 系统信息
        cpu_info: CPU信息
        gpu_info: GPU信息
        memory_info: 内存信息
        config_path: 配置文件路径
        width: 文本宽度
        
    Returns:
        格式化的文本字符串
    """
    display = HardwareDisplay(config_path=config_path)
    return display.format_text(system_info, cpu_info, gpu_info, memory_info, width)