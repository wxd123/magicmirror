#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/display.py
"""
硬件检测结果显示模块
"""

from typing import Dict, Any, Optional
from pathlib import Path
from magicm.management.config.configManager import ConfigManager


class HardwareDisplay:
    """硬件检测结果展示类"""   
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None):
        self.width = 50
        self.config_manager = ConfigManager()  # 创建实例
        
        if config is not None:
            self.config = config
        else:
            self.config = self.config_manager.load('display', 'config.yaml')    
    
    
    # ==================== 评级方法 ====================
    
    def get_gpu_rating(self, gpu_name: str) -> str:
        gpu_lower = gpu_name.lower()
        gpu_ratings = self.config['gpu_ratings']
        gpu_rating_words = gpu_ratings['rating']
        ret = ''
        for key in ['nuclear', 'flagship', 'high']:
            if any(kw in gpu_lower for kw in gpu_ratings[key]):
                ret = gpu_rating_words[key]
            else:
                ret = gpu_rating_words['other']
        return '【' + ret +'】'
    
    def get_vram_rating(self, vram_gb: int) -> str:
        ratings = self.config['vram_ratings']
        for rating_config in ratings:
            if vram_gb >= rating_config['min']:
                return rating_config['rating']
        return ratings[-1]['rating']
    
    def get_driver_rating(self, driver_version: str) -> str:
        if not driver_version or driver_version == "未知":
            return "【未检测】"
        
        import re
        match = re.search(r'(\d+)', str(driver_version))
        if not match:
            return "【版本未知】"
        
        major_version = int(match.group(1))
        ratings = self.config['driver_ratings']
        for rating_config in ratings:
            if major_version >= rating_config['min_version']:
                return rating_config['rating']
        return ratings[-1]['rating']
    
    def get_system_rating(self, os_name: str) -> str:
        os_lower = os_name.lower()
        system_ratings = self.config['system_ratings']
        
        for sys_type, sys_config in system_ratings.items():
            if sys_type == 'default':
                continue
            for keyword in sys_config['keywords']:
                if keyword in os_lower:
                    return sys_config['rating']
        
        return system_ratings['default']['rating']
    
    def get_cpu_rating(self, cpu_model: str) -> str:
        cpu_lower = cpu_model.lower()
        cpu_ratings = self.config['cpu_ratings']
        
        for level in ['top', 'high', 'medium', 'entry']:
            for keyword in cpu_ratings[level]['keywords']:
                if keyword in cpu_lower:
                    return cpu_ratings[level]['rating']
        
        return cpu_ratings['default']['rating']
    
    def get_memory_rating(self, memory_gb: int) -> str:
        ratings = self.config['memory_ratings']
        for rating_config in ratings:
            if memory_gb >= rating_config['min']:
                return rating_config['rating']
        return ratings[-1]['rating']
    
    # ==================== 对齐显示方法 ====================
    
    def _get_display_width(self, text: str) -> int:
        """计算字符串显示宽度（中文占2，英文占1）"""
        width = 0
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff' or ch in '【】（）':
                width += 2
            else:
                width += 1
        return width
    
    def _pad_to_width(self, text: str, target_width: int) -> str:
        """填充空格到指定显示宽度"""
        current_width = self._get_display_width(text)
        if current_width >= target_width:
            return text
        return text + ' ' * (target_width - current_width)
    
    def _show_info(self, label: str, value: str, rating: str, indent: int = 4):
        """通用显示方法"""
        spaces = " " * indent
        col1 = f"{spaces}{label}：{value}"
        col1_padded = self._pad_to_width(col1, 35)
        print(f"{col1_padded}{rating}")
    
    def show_banner(self):
        """显示欢迎横幅"""
        print("\n" + "=" * 58)
        print("        你的硬件检测结果")
        print("=" * 58)
        print()
    
    def show_footer(self):
        print("\n" + "=" * 58)
        print()
    
    def display_all(self, system_info: Dict[str, Any], cpu_info: Dict[str, Any], 
                   gpu_info: Dict[str, Any], memory_info: Dict[str, Any]):
        """显示所有硬件信息"""
        self.show_banner()
        
        # 定义显示配置
        displays = [
            ("GPU", gpu_info.get("name", "未知"), 
             self.get_gpu_rating(gpu_info.get("name", "未知"))),
            
            ("显存", f"{gpu_info.get('memory_gb', 0)}GB", 
             self.get_vram_rating(gpu_info.get('memory_gb', 0))),
            
            ("驱动", gpu_info.get("driver_version", "未知"), 
             self.get_driver_rating(gpu_info.get("driver_version", "未知"))),
            
            ("系统环境", system_info.get("pretty_name", system_info.get("name", "未知")), 
             self.get_system_rating(system_info.get("pretty_name", system_info.get("name", "未知")))),
            
            ("CPU", cpu_info.get("simple_model", cpu_info.get("model", "未知")), 
             self.get_cpu_rating(cpu_info.get("simple_model", cpu_info.get("model", "未知")))),
            
            ("内存", f"{memory_info.get('total_gb', 0)}GB", 
             self.get_memory_rating(memory_info.get('total_gb', 0))),
        ]
        
        # 循环显示
        for label, value, rating in displays:
            self._show_info(label, value, rating)
        
        self.show_footer()


# ==================== 便捷函数 ====================

def create_display(config_path: Optional[str] = None) -> HardwareDisplay:
    return HardwareDisplay(config_path=config_path)


def display_hardware_info(system_info: Dict[str, Any], cpu_info: Dict[str, Any],
                         gpu_info: Dict[str, Any], memory_info: Dict[str, Any],
                         config_path: Optional[str] = None):
    display = HardwareDisplay(config_path=config_path)
    display.display_all(system_info, cpu_info, gpu_info, memory_info)


def format_hardware_info(system_info: Dict[str, Any], cpu_info: Dict[str, Any], 
                        gpu_info: Dict[str, Any], memory_info: Dict[str, Any],
                        config_path: Optional[str] = None) -> str:
    display = HardwareDisplay(config_path=config_path)
    
    lines = []
    lines.append("=" * 58)
    lines.append("        你的硬件检测结果")
    lines.append("=" * 58)
    lines.append("")
    
    def add_line(label, value, rating):
        spaces = " " * 4
        col1 = f"{spaces}{label}：{value}"
        col1_padded = display._pad_to_width(col1, 35)
        lines.append(f"{col1_padded}{rating}")
    
    # 定义显示配置
    displays = [
        ("GPU", gpu_info.get("name", "未知"), 
         display.get_gpu_rating(gpu_info.get("name", "未知"))),
        
        ("显存", f"{gpu_info.get('memory_gb', 0)}GB", 
         display.get_vram_rating(gpu_info.get('memory_gb', 0))),
        
        ("驱动", gpu_info.get("driver_version", "未知"), 
         display.get_driver_rating(gpu_info.get("driver_version", "未知"))),
        
        ("系统环境", system_info.get("pretty_name", system_info.get("name", "未知")), 
         display.get_system_rating(system_info.get("pretty_name", system_info.get("name", "未知")))),
        
        ("CPU", cpu_info.get("simple_model", cpu_info.get("model", "未知")), 
         display.get_cpu_rating(cpu_info.get("simple_model", cpu_info.get("model", "未知")))),
        
        ("内存", f"{memory_info.get('total_gb', 0)}GB", 
         display.get_memory_rating(memory_info.get('total_gb', 0))),
    ]
    
    for label, value, rating in displays:
        add_line(label, value, rating)
    
    lines.append("")
    lines.append("=" * 58)
    lines.append("")
    
    return "\n".join(lines)