#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/disp/formatter.py
"""
硬件显示格式化模块
"""

from typing import Dict, Any
from .hardware_rating import HardwareRating


class HardwareFormatter:
    """硬件信息格式化显示类"""
    
    def __init__(self, rating_calculator: HardwareRating, default_width: int = 50):
        """
        初始化格式化器
        
        Args:
            rating_calculator: 评级计算器实例
            default_width: 默认显示宽度
        """
        self.rating = rating_calculator
        self.width = default_width
    
    def _get_display_width(self, text: str) -> int:
        """
        计算字符串显示宽度（中文占2，英文占1）
        
        Args:
            text: 输入字符串
            
        Returns:
            显示宽度
        """
        width = 0
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff' or ch in '【】（）':
                width += 2
            else:
                width += 1
        return width
    
    def _pad_to_width(self, text: str, target_width: int) -> str:
        """
        填充空格到指定显示宽度
        
        Args:
            text: 输入字符串
            target_width: 目标宽度
            
        Returns:
            填充后的字符串
        """
        current_width = self._get_display_width(text)
        if current_width >= target_width:
            return text
        return text + ' ' * (target_width - current_width)
    
    def _show_info(self, label: str, value: str, rating: str, indent: int = 4):
        """
        通用显示方法（控制台输出）
        
        Args:
            label: 标签名
            value: 值
            rating: 评级
            indent: 缩进空格数
        """
        spaces = " " * indent
        col1 = f"{spaces}{label}：{value}"
        col1_padded = self._pad_to_width(col1, self.width)
        print(f"{col1_padded}{rating}")
    
    def show_banner(self):
        """显示欢迎横幅"""
        print("\n" + "=" * 58)
        print("        你的硬件检测结果")
        print("=" * 58)
        print()
    
    def show_footer(self):
        """显示页脚"""
        print("\n" + "=" * 58)
        print()
    
    def display_all(self, system_info: Dict[str, Any]):
        """
        显示所有硬件信息（控制台输出）
        
        Args:
            system_info: 系统信息, {
                'system':   system_info,
                'cpu':      cpu_info,
                'gpu':      gpu_info,
                'mem':      memory_info,
                'env':      env_info
            }            
        """
        self.show_banner()
        
        # 获取所有评级
        ratings = self.rating.get_all_ratings(system_info)
        
        # 定义显示配置
        sys_info = system_info['system']
        gpu_info = system_info['gpu']
        cpu_info = system_info['cpu']
        memory_info = system_info['mem']
        # env_info = system_info['env']

        if 'distribution' in sys_info:
            sys_display_name = sys_info['distribution'].get('pretty_name', '未知')
        displays = [
            ("GPU", gpu_info.get("name", "未知"), ratings['gpu']),
            ("显存", f"{gpu_info.get('memory_gb', 0)}GB", ratings['vram']),
            ("驱动", gpu_info.get("driver_version", "未知"), ratings['driver']),            
            ("CPU", cpu_info.get("simple_model", cpu_info.get("model", "未知")), ratings['cpu']),
            ("内存", f"{memory_info.get('total_gb', 0)}GB", ratings['memory']),
            ("系统环境", sys_info['distribution']['pretty_name'], ratings['system'])
        ]
        
        # 循环显示
        for label, value, rating in displays:
            self._show_info(label, value, rating)
        
        self.show_footer()
    
    def format_as_text(self, system_info: Dict[str, Any], cpu_info: Dict[str, Any],
                      gpu_info: Dict[str, Any], memory_info: Dict[str, Any],
                      width: int = 100) -> str:
        """
        返回格式化的文本（不直接输出）
        
        Args:
            system_info: 系统信息
            cpu_info: CPU信息
            gpu_info: GPU信息
            memory_info: 内存信息
            width: 文本宽度
            
        Returns:
            格式化的文本字符串
        """
        # 获取所有评级
        ratings = self.rating.get_all_ratings(system_info, cpu_info, gpu_info, memory_info)
        
        lines = []
        lines.append("=" * width)
        lines.append("你的硬件检测结果".center(width))
        lines.append("=" * width)
        lines.append("")
        
        def add_line(label: str, value: str, rating: str):
            """添加一行文本"""
            spaces = " " * 4
            col1 = f"{spaces}{label}：{value}"
            # 评级固定占12个字符宽度
            rating_width = 12
            col1_width = width - rating_width - 2  # 减2作为间隔
            col1_padded = col1.ljust(col1_width)
            lines.append(f"{col1_padded}  {rating}")
        
        # 定义显示配置
        displays = [
            ("GPU", gpu_info.get("name", "未知"), ratings['gpu']),
            ("显存", f"{gpu_info.get('memory_gb', 0)}GB", ratings['vram']),
            ("驱动", gpu_info.get("driver_version", "未知"), ratings['driver']),
            ("系统环境", system_info.get("pretty_name", system_info.get("name", "未知")), ratings['system']),
            ("CPU", cpu_info.get("simple_model", cpu_info.get("model", "未知")), ratings['cpu']),
            ("内存", f"{memory_info.get('total_gb', 0)}GB", ratings['memory']),
        ]
        
        for label, value, rating in displays:
            add_line(label, value, rating)
        
        lines.append("")
        lines.append("=" * width)
        lines.append("")
        
        return "\n".join(lines)