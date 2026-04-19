# `enviroment`

## Table of Contents

- 🅼 [enviroment](#enviroment)
- 🅼 [enviroment\.env\_manage](#enviroment-env_manage)
- 🅼 [enviroment\.env\_setup](#enviroment-env_setup)
- 🅼 [enviroment\.uv\_installer](#enviroment-uv_installer)

<a name="enviroment"></a>
## 🅼 enviroment
<a name="enviroment-env_manage"></a>
## 🅼 enviroment\.env\_manage

虚拟环境管理器 - 创建和删除 \(Linux版\)

- **Classes:**
  - 🅲 [VirtualEnvManager](#enviroment-env_manage-VirtualEnvManager)

### Classes

<a name="enviroment-env_manage-VirtualEnvManager"></a>
### 🅲 enviroment\.env\_manage\.VirtualEnvManager

```python
class VirtualEnvManager:
```

虚拟环境管理器 - Linux版

**Functions:**

<a name="enviroment-env_manage-VirtualEnvManager-__init__"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.\_\_init\_\_

```python
def __init__(self, env_name: str, env_path: str, python_version: str = '3.11'):
```

初始化环境管理器

**Parameters:**

- **env_name**: 环境名称
- **env_path**: 环境路径
- **python_version**: Python版本
<a name="enviroment-env_manage-VirtualEnvManager-exists"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.exists

```python
def exists(self) -> bool:
```

检查环境是否已存在
<a name="enviroment-env_manage-VirtualEnvManager-delete"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.delete

```python
def delete(self, force: bool = False) -> bool:
```

删除已存在的环境

**Parameters:**

- **force**: 是否强制删除（不询问）

**Returns:**

- 是否执行删除
<a name="enviroment-env_manage-VirtualEnvManager-create"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.create

```python
def create(self) -> bool:
```

创建虚拟环境

**Returns:**

- 是否创建成功
<a name="enviroment-env_manage-VirtualEnvManager-get_python_path"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.get\_python\_path

```python
def get_python_path(self) -> Optional[Path]:
```

获取环境中的 python 路径
<a name="enviroment-env_manage-VirtualEnvManager-get_pip_path"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.get\_pip\_path

```python
def get_pip_path(self) -> Optional[Path]:
```

获取环境中的 pip 路径
<a name="enviroment-env_manage-VirtualEnvManager-run_python"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.run\_python

```python
def run_python(self, script_args: list) -> subprocess.CompletedProcess:
```

在环境中运行 Python 脚本
<a name="enviroment-env_manage-VirtualEnvManager-install_package"></a>
#### 🅵 enviroment\.env\_manage\.VirtualEnvManager\.install\_package

```python
def install_package(self, package: str) -> bool:
```

在环境中安装包
<a name="enviroment-env_setup"></a>
## 🅼 enviroment\.env\_setup

虚拟环境创建模块 - 提供在 /opt/magicm/ 下创建虚拟环境的功能

- **Functions:**
  - 🅵 [create\_virtual\_env](#enviroment-env_setup-create_virtual_env)
  - 🅵 [get\_env\_path](#enviroment-env_setup-get_env_path)
  - 🅵 [env\_exists](#enviroment-env_setup-env_exists)

### Functions

<a name="enviroment-env_setup-create_virtual_env"></a>
### 🅵 enviroment\.env\_setup\.create\_virtual\_env

```python
def create_virtual_env(env_name: str, python_version: str = '3.11', force: bool = False) -> bool:
```

创建虚拟环境

**Parameters:**

- **env_name**: 环境名称
- **python_version**: Python版本
- **force**: 是否强制删除已存在的环境

**Returns:**

- 是否创建成功
<a name="enviroment-env_setup-get_env_path"></a>
### 🅵 enviroment\.env\_setup\.get\_env\_path

```python
def get_env_path(env_name: str) -> Path:
```

获取环境路径
<a name="enviroment-env_setup-env_exists"></a>
### 🅵 enviroment\.env\_setup\.env\_exists

```python
def env_exists(env_name: str) -> bool:
```

检查环境是否存在
<a name="enviroment-uv_installer"></a>
## 🅼 enviroment\.uv\_installer

UV 安装器 - 检测、下载、安装 uv \(Linux版\)

- **Classes:**
  - 🅲 [UVInstaller](#enviroment-uv_installer-UVInstaller)

### Classes

<a name="enviroment-uv_installer-UVInstaller"></a>
### 🅲 enviroment\.uv\_installer\.UVInstaller

```python
class UVInstaller:
```

UV 安装器 - Linux版

**Functions:**

<a name="enviroment-uv_installer-UVInstaller-is_installed"></a>
#### 🅵 enviroment\.uv\_installer\.UVInstaller\.is\_installed

```python
def is_installed() -> bool:
```

检查 uv 是否已安装
<a name="enviroment-uv_installer-UVInstaller-get_version"></a>
#### 🅵 enviroment\.uv\_installer\.UVInstaller\.get\_version

```python
def get_version() -> Optional[str]:
```

获取 uv 版本
<a name="enviroment-uv_installer-UVInstaller-get_install_path"></a>
#### 🅵 enviroment\.uv\_installer\.UVInstaller\.get\_install\_path

```python
def get_install_path() -> Path:
```

获取 uv 安装路径
<a name="enviroment-uv_installer-UVInstaller-install"></a>
#### 🅵 enviroment\.uv\_installer\.UVInstaller\.install

```python
def install(cls, install_path: Optional[Path] = None) -> bool:
```

下载并安装 uv
<a name="enviroment-uv_installer-UVInstaller-ensure_installed"></a>
#### 🅵 enviroment\.uv\_installer\.UVInstaller\.ensure\_installed

```python
def ensure_installed(cls) -> bool:
```

确保 uv 已安装，未安装则自动安装
