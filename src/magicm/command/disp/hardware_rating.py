#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/disp/hardware_rating.py
"""
硬件评级计算模块
"""

from typing import Dict, Any
import re


class HardwareRating:
    """硬件评级计算类"""
    
    def __init__(self, config: Dict[str, Any]):
        """
        初始化评级计算器
        
        Args:
            config: 配置字典，包含评级规则
        """
        self.config = config
    
    def get_gpu_rating(self, gpu_name: str) -> str:
        """
        获取GPU评级
        
        Args:
            gpu_name: GPU名称
            
        Returns:
            评级字符串（带【】括号）
        """
        if not gpu_name or gpu_name == "未知":
            return "【未知】"
        
        gpu_lower = gpu_name.lower()
        gpu_ratings = self.config.get('gpu_ratings', {})
        gpu_rating_words = gpu_ratings.get('rating', {})
        
        # 按优先级检查：核弹级 > 旗舰级 > 高性能级
        ret = gpu_rating_words.get('other', '普通')
        for key in ['nuclear', 'flagship', 'high']:
            if any(kw in gpu_lower for kw in gpu_ratings.get(key, [])):
                ret = gpu_rating_words.get(key, '未知')
                break
        
        return '【' + ret + '】'
    
    def get_vram_rating(self, vram_gb: int) -> str:
        """
        获取显存评级
        
        Args:
            vram_gb: 显存大小（GB）
            
        Returns:
            评级字符串
        """
        if vram_gb <= 0:
            return "【无显存】"
        
        ratings = self.config.get('vram_ratings', [])
        for rating_config in ratings:
            if vram_gb >= rating_config.get('min', 0):
                return rating_config.get('rating', '【未知】')
        
        return ratings[-1].get('rating', '【未知】') if ratings else "【未知】"
    
    def get_driver_rating(self, driver_version: str) -> str:
        """
        获取驱动评级
        
        Args:
            driver_version: 驱动版本号
            
        Returns:
            评级字符串
        """
        if not driver_version or driver_version == "未知":
            return "【未检测】"
        
        # 提取主版本号
        match = re.search(r'(\d+)', str(driver_version))
        if not match:
            return "【版本未知】"
        
        major_version = int(match.group(1))
        ratings = self.config.get('driver_ratings', [])
        
        for rating_config in ratings:
            if major_version >= rating_config.get('min_version', 0):
                return rating_config.get('rating', '【未知】')
        
        return ratings[-1].get('rating', '【未知】') if ratings else "【未知】"
    
    def get_system_rating(self, os_name: str) -> str:
        """
        获取操作系统评级
        
        Args:
            os_name: 操作系统名称
            
        Returns:
            评级字符串
        """
        if not os_name or os_name == "未知":
            return "【未知】"
        
        os_lower = os_name.lower()
        system_ratings = self.config.get('system_ratings', {})
        
        for sys_type, sys_config in system_ratings.items():
            if sys_type == 'default':
                continue
            for keyword in sys_config.get('keywords', []):
                if keyword in os_lower:
                    return sys_config.get('rating', '【未知】')
        
        return system_ratings.get('default', {}).get('rating', '【未知】')
    
    def get_cpu_rating(self, cpu_model: str) -> str:
        """
        获取CPU评级
        
        Args:
            cpu_model: CPU型号
            
        Returns:
            评级字符串
        """
        if not cpu_model or cpu_model == "未知":
            return "【未知】"
        
        cpu_lower = cpu_model.lower()
        cpu_ratings = self.config.get('cpu_ratings', {})
        
        for level in ['top', 'high', 'medium', 'entry']:
            for keyword in cpu_ratings.get(level, {}).get('keywords', []):
                if keyword in cpu_lower:
                    return cpu_ratings[level].get('rating', '【未知】')
        
        return cpu_ratings.get('default', {}).get('rating', '【标准CPU】')
    
    def get_memory_rating(self, memory_gb: int) -> str:
        """
        获取内存评级
        
        Args:
            memory_gb: 内存大小（GB）
            
        Returns:
            评级字符串
        """
        if memory_gb <= 0:
            return "【无内存】"
        
        ratings = self.config.get('memory_ratings', [])
        for rating_config in ratings:
            if memory_gb >= rating_config.get('min', 0):
                return rating_config.get('rating', '【未知】')
        
        return ratings[-1].get('rating', '【未知】') if ratings else "【未知】"
    
    def get_all_ratings(self, system_info: Dict[str, Any]) -> Dict[str, str]:
        """
        一次性获取所有评级
        
        Args:
            system_info: 系统信息,return {
                'system':   system_info,
                'cpu':      cpu_info,
                'gpu':      gpu_info,
                'mem':      memory_info
            }        
            
        Returns:
            包含所有评级的字典
        """
        gpu_info = system_info['gpu']
        cpu_info = system_info['cpu']
        memory_info = system_info['mem']
        sys_info = system_info['system']
        return {
            'gpu': self.get_gpu_rating(gpu_info.get('name', '未知')),
            'vram': self.get_vram_rating(gpu_info.get('memory_gb', 0)),
            'driver': self.get_driver_rating(gpu_info.get('driver_version', '未知')),
            'system': self.get_system_rating(sys_info['distribution']['name']),
            'cpu': self.get_cpu_rating(cpu_info.get('simple_model', cpu_info.get('model', '未知'))),
            'memory': self.get_memory_rating(memory_info.get('total_gb', 0))
        }