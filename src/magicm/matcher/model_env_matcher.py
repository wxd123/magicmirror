"""
模型环境匹配模块 - 精确版本匹配
"""

import os
import sys
import subprocess
import importlib.metadata
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path
import yaml
import psutil


@dataclass
class MatchResult:
    """匹配结果数据类"""
    success: bool
    model_name: str
    gpu_name: str
    gpu_class: str
    messages: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    detected_config: Dict[str, Any] = field(default_factory=dict)
    required_config: Dict[str, Any] = field(default_factory=dict)


class SystemDetector:
    """系统检测器"""
    
    @staticmethod
    def detect_python_version() -> str:
        """检测Python版本"""
        return f"{sys.version_info.major}.{sys.version_info.minor}"
    
    @staticmethod
    def detect_cuda_version() -> Optional[str]:
        """检测CUDA版本"""
        try:
            result = subprocess.run(['nvcc', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'release' in line:
                        version = line.split('release')[-1].strip().split(',')[0]
                        return version
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        return None
    
   
    
    @staticmethod
    def detect_system_ram_gb() -> float:
        """检测系统内存大小(GB)"""
        return psutil.virtual_memory().total / (1024**3)
    
    @staticmethod
    def detect_build_tool_version(tool_name: str) -> Optional[str]:
        """检测构建工具版本"""
        tool_commands = {
            'cmake': ['cmake', '--version'],
            'ninja': ['ninja', '--version'],
            'cuda-toolkit': ['nvcc', '--version']
        }
        
        if tool_name not in tool_commands:
            return None
        
        try:
            result = subprocess.run(tool_commands[tool_name],
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                output = result.stdout.strip()
                if tool_name == 'cuda-toolkit':
                    for line in output.split('\n'):
                        if 'release' in line:
                            return line.split('release')[-1].strip().split(',')[0]
                elif tool_name == 'cmake':
                    parts = output.split()
                    if len(parts) >= 3:
                        return parts[2]
                elif tool_name == 'ninja':
                    return output.split()[0]
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return None
        return None
    
    @staticmethod
    def detect_package_version(package_name: str) -> Optional[str]:
        """检测Python包版本"""
        try:
            return importlib.metadata.version(package_name)
        except importlib.metadata.PackageNotFoundError:
            return None


class ModelEnvironmentMatcher:
    """模型环境匹配器"""
    
    def __init__(self, config_path: str = "configs/trellis2_config.yaml"):
        self.config_path = Path(config_path)
        self.detector = SystemDetector()
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """加载配置文件"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    def match_model_environment(self, model_name: str) -> MatchResult:
        """匹配模型环境"""
        result = MatchResult(
            success=False,
            model_name=model_name,
            gpu_name="",
            gpu_class=""
        )
        
        # 检查模型配置是否存在
        if model_name not in self.config.get('model_configs', {}):
            result.errors.append(f"Model '{model_name}' not found in config")
            result.messages.append(f"Available models: {list(self.config['model_configs'].keys())}")
            return result
        
        model_config = self.config['model_configs'][model_name]
        result.required_config = model_config
        
        # 检测系统信息
        detected_info = {
            'python_version': self.detector.detect_python_version(),
            'cuda_version': self.detector.detect_cuda_version(),
            'system_ram_gb': self.detector.detect_system_ram_gb(),
            'gpus': self.detector.detect_gpu_info(),
            'packages': {},
            'build_tools': {}
        }
        
        # 检测所有包版本
        for gpu_class, gpu_config in model_config.get('gpu_configs', {}).items():
            for dep_name in gpu_config.get('dependencies', {}):
                if dep_name not in detected_info['packages']:
                    detected_info['packages'][dep_name] = self.detector.detect_package_version(dep_name)
            
            for tool_name in gpu_config.get('build_tools', {}):
                if tool_name not in detected_info['build_tools']:
                    detected_info['build_tools'][tool_name] = self.detector.detect_build_tool_version(tool_name)
        
        result.detected_config = detected_info
        
        # 检查系统内存
        if detected_info['system_ram_gb'] < model_config.get('min_system_ram_gb', 0):
            result.errors.append(
                f"Insufficient system RAM: {detected_info['system_ram_gb']:.1f}GB < "
                f"{model_config['min_system_ram_gb']}GB"
            )
            result.recommendations.append(f"Upgrade RAM to at least {model_config['min_system_ram_gb']}GB")
        
        # 检查GPU
        if not detected_info['gpus']:
            result.errors.append("No CUDA-capable GPU detected")
            result.recommendations.append("Install NVIDIA GPU with CUDA support")
            return result
        
        # 匹配GPU配置
        matched_gpu_config = None
        matched_gpu_class = None
        matched_gpu_name = None
        
        for gpu_info in detected_info['gpus']:
            gpu_name = gpu_info['name']
            for gpu_class, gpu_config in model_config.get('gpu_configs', {}).items():
                if gpu_class.lower() in gpu_name.lower():
                    # 检查显存
                    if gpu_info['total_vram_gb'] >= gpu_config.get('min_vram_gb', 0):
                        matched_gpu_config = gpu_config
                        matched_gpu_class = gpu_class
                        matched_gpu_name = gpu_name
                        result.messages.append(f"GPU matched: {gpu_name} -> {gpu_class}")
                        break
                    else:
                        result.warnings.append(
                            f"GPU {gpu_name} has insufficient VRAM: "
                            f"{gpu_info['total_vram_gb']:.1f}GB < {gpu_config['min_vram_gb']}GB"
                        )
            if matched_gpu_config:
                break
        
        if not matched_gpu_config:
            result.errors.append(
                f"No compatible GPU found. Supported: {list(model_config['gpu_configs'].keys())}"
            )
            result.recommendations.append(
                f"Please use one of: {', '.join(model_config['gpu_configs'].keys())}"
            )
            return result
        
        result.gpu_name = matched_gpu_name
        result.gpu_class = matched_gpu_class
        
        # 精确匹配各项配置
        # 1. 检查Python版本
        required_python = matched_gpu_config['python_version']
        if detected_info['python_version'] != required_python:
            result.errors.append(
                f"Python version mismatch: {detected_info['python_version']} != {required_python}"
            )
            result.recommendations.append(f"Use Python {required_python}")
        
        # 2. 检查CUDA版本
        required_cuda = matched_gpu_config['build_tools'].get('cuda-toolkit')
        if required_cuda and detected_info['cuda_version'] != required_cuda:
            result.errors.append(
                f"CUDA version mismatch: {detected_info['cuda_version']} != {required_cuda}"
            )
            result.recommendations.append(f"Install CUDA Toolkit {required_cuda}")
        
        # 3. 检查构建工具版本
        for tool_name, required_version in matched_gpu_config['build_tools'].items():
            if tool_name == 'cuda-toolkit':
                continue  # 已检查
            detected_version = detected_info['build_tools'].get(tool_name)
            if detected_version != required_version:
                result.errors.append(
                    f"{tool_name} version mismatch: {detected_version} != {required_version}"
                )
                result.recommendations.append(f"Install {tool_name} {required_version}")
        
        # 4. 检查Python包版本
        for package_name, required_version in matched_gpu_config['dependencies'].items():
            detected_version = detected_info['packages'].get(package_name)
            if detected_version != required_version:
                result.errors.append(
                    f"{package_name} version mismatch: {detected_version} != {required_version}"
                )
                result.recommendations.append(f"Install {package_name}=={required_version}")
        
        # 判断是否成功
        result.success = len(result.errors) == 0
        
        if result.success:
            result.messages.append("All environment checks passed!")
            result.messages.append(f"GPU Class: {matched_gpu_class}")
            result.messages.append(f"Python: {required_python}")
            result.messages.append(f"CUDA: {required_cuda}")
            
            # 添加性能建议
            if 'environment_variables' in matched_gpu_config:
                result.recommendations.append("Recommended environment variables:")
                for key, value in matched_gpu_config['environment_variables'].items():
                    result.recommendations.append(f"  export {key}={value}")
        
        return result
    
    def get_environment_setup_commands(self, result: MatchResult) -> List[str]:
        """获取环境设置命令"""
        commands = []
        
        if not result.success:
            return commands
        
        if result.matched_config:
            # Conda环境创建命令
            python_version = result.matched_config.get('python_version')
            if python_version:
                commands.append(f"conda create -n {result.model_name}_env python={python_version}")
                commands.append(f"conda activate {result.model_name}_env")
            
            # 包安装命令
            for package, version in result.matched_config.get('dependencies', {}).items():
                commands.append(f"pip install {package}=={version}")
            
            # 环境变量设置
            for key, value in result.matched_config.get('environment_variables', {}).items():
                commands.append(f"export {key}={value}")
        
        return commands


# 使用示例
if __name__ == "__main__":
    matcher = ModelEnvironmentMatcher("configs/trellis2_config.yaml")
    
    # 匹配trellis2模型
    result = matcher.match_model_environment("trellis2")
    
    print(f"\n{'='*60}")
    print(f"Model: {result.model_name}")
    print(f"Success: {result.success}")
    print(f"GPU: {result.gpu_name} ({result.gpu_class})")
    print(f"\nMessages:")
    for msg in result.messages:
        print(f"  ✓ {msg}")
    print(f"\nErrors:")
    for err in result.errors:
        print(f"  ✗ {err}")
    print(f"\nWarnings:")
    for warn in result.warnings:
        print(f"  ⚠ {warn}")
    print(f"\nRecommendations:")
    for rec in result.recommendations:
        print(f"  → {rec}")
    
    if result.success:
        print(f"\nEnvironment Setup Commands:")
        for cmd in matcher.get_environment_setup_commands(result):
            print(f"  $ {cmd}")
    print(f"{'='*60}")