# magicm/detector/software/env/env_detecter.py
import sys
import os
from typing import Dict, Any

def detect() -> Dict[str, Any]:
    """统一检测当前环境类型"""
    
    # 检测顺序：mamba -> conda -> uv -> venv
    # 因为 mamba 环境通常也满足 conda 的检测条件，需优先判断
    
    # 检测 mamba
    if _is_mamba_env():
        from . import mamba_detecter
        details = mamba_detecter.detect()
        return {
            "env_type": "mamba",
            "is_virtual_env": True,
            "details": details,
            "python_executable": sys.executable,
            "python_version": sys.version.split()[0]
        }
    
    # 检测 conda
    if _is_conda_env():
        from . import conda_detecter
        details = conda_detecter.detect()
        return {
            "env_type": "conda",
            "is_virtual_env": True,
            "details": details,
            "python_executable": sys.executable,
            "python_version": sys.version.split()[0]
        }
    
    # 检测 uv
    if _is_uv_env():
        from . import uv_detecter
        details = uv_detecter.detect()
        return {
            "env_type": "uv",
            "is_virtual_env": True,
            "details": details,
            "python_executable": sys.executable,
            "python_version": sys.version.split()[0]
        }
    
    # 检测标准 venv / virtualenv
    if hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix:
        return {
            "env_type": "venv" if not hasattr(sys, "real_prefix") else "virtualenv",
            "is_virtual_env": True,
            "details": {
                "base_prefix": sys.base_prefix,
                "real_prefix": getattr(sys, "real_prefix", None)
            },
            "python_executable": sys.executable,
            "python_version": sys.version.split()[0]
        }
    
    # 无虚拟环境
    return {
        "env_type": "none",
        "is_virtual_env": False,
        "details": {},
        "python_executable": sys.executable,
        "python_version": sys.version.split()[0]
    }

def _is_mamba_env() -> bool:
    """检测是否为 mamba 环境"""
    # 检查环境变量或 mamba 特有的路径特征
    if os.environ.get("MAMBA_ROOT_PREFIX"):
        return True
    # 检查 python 路径是否包含 mamba
    if "mamba" in sys.prefix.lower():
        return True
    return False

def _is_conda_env() -> bool:
    """检测是否为 conda 环境（非 mamba）"""
    if not os.environ.get("CONDA_PREFIX"):
        return False
    # 如果已经被识别为 mamba，则返回 False
    if _is_mamba_env():
        return False
    return True

def _is_uv_env() -> bool:
    """检测是否为 uv 环境"""
    # uv 项目通常会设置环境变量或使用 .venv 目录
    if os.environ.get("UV_PROJECT_ENVIRONMENT"):
        return True
    # 检查当前目录或父目录是否存在 pyproject.toml + .venv
    current = os.getcwd()
    while current != os.path.dirname(current):
        if os.path.exists(os.path.join(current, ".venv")):
            return True
        current = os.path.dirname(current)
    return False

def get_env_type() -> str:
    return detect()["env_type"]