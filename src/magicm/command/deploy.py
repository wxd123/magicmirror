#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# magicm/command/deploy.py

from magicm.deploy.enviroment.env_setup import setup_env
from pathlib import Path

def setup():
    """ 设置虚拟环境信息"""
    setup_env(
        env_name='myapp',
        env_path=Path('/opt/magicm/trellis2'),
        python_version='3.11',
        force=False
    ) 