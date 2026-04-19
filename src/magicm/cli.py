#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
magicm CLI 硬件检测工具
"""

import sys
import os

# 添加项目路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from magicm.command.detecter import detect as hardware_detecter
from magicm.command.display import display_hardware_info
from magicm.command.deploy import setup as env_setup



def main():
    """主函数：顺序调用各检测模块，然后交给 display 显示"""
    # print("\n🔍 正在检测硬件信息...\n")
    
    # 1. 硬件检测
    system_info = hardware_detecter()
    
    # 1.1.  显示硬件检测结果
    # print("\n  [5/5] 生成检测报告...")
    display_hardware_info(system_info)
    
    # 2. 安装虚拟环境
    env_setup()
    return 0

    

if __name__ == "__main__":
    sys.exit(main())