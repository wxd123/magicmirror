# MagicMirror

[![PyPI version](https://badge.fury.io/py/magicm.svg)](https://badge.fury.io/py/magicm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> 一键部署大模型的工具包 —— 支持 API 服务和 ComfyUI 节点两种部署方式

## 项目状态

**开发中** - 首个正式版本将于 2026 年 5 月发布

## 功能规划

- **API 服务部署**：一行命令将大模型封装为 REST API 服务
- **ComfyUI 集成**：一键安装 ComfyUI 自定义节点，在 ComfyUI 中直接调用
- **模型格式转换**：支持 PyTorch、ONNX、TensorRT 等多种格式
- **多平台发布**：支持发布到 Hugging Face、ModelScope 等平台

## 安装

```bash
pip install magicm
```
## 快速开始（待正式版本发布后补充）

```python
from magicm import deploy
```
## 一键部署
```
deploy("your-model-path")
````
## 代码规范
本项目遵循以下基本原则：

1. 单文件不超过 200 行：超过时请拆分为多个模块
2. 单函数不超过 200 行：超过时请拆分为多个小函数
3. 注释尽量完整：关键逻辑、复杂算法、非显而易见的代码必须有注释说明
4. 如有特殊场景确实需要突破（如纯数据定义文件），可在 PR 中说明。

这些规则旨在保证代码的可读性和可维护性，便于合作，请尽量遵守。

## 针对 AI 辅助工具的提示
本项目使用 AI 辅助开发，请在生成代码时尽量遵守上述代码规范。

## 许可证
MIT License

## 作者
wxd123 - GitHub
