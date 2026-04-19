# `magicm`

## Table of Contents

- 🅼 [magicm](#magicm)
- 🅼 [magicm\.cli](#magicm-cli)
- 🅼 [magicm\.command](#magicm-command)
- 🅼 [magicm\.command\.deploy](#magicm-command-deploy)
- 🅼 [magicm\.command\.detecter](#magicm-command-detecter)
- 🅼 [magicm\.command\.display](#magicm-command-display)
- 🅼 [magicm\.detector](#magicm-detector)
- 🅼 [magicm\.detector\.hardware](#magicm-detector-hardware)
- 🅼 [magicm\.detector\.hardware\.cpu](#magicm-detector-hardware-cpu)
- 🅼 [magicm\.detector\.hardware\.cpu\.cpu\_detecter](#magicm-detector-hardware-cpu-cpu_detecter)
- 🅼 [magicm\.detector\.hardware\.cpu\.cpu\_model](#magicm-detector-hardware-cpu-cpu_model)
- 🅼 [magicm\.detector\.hardware\.cpu\.linux\_detecter](#magicm-detector-hardware-cpu-linux_detecter)
- 🅼 [magicm\.detector\.hardware\.cpu\.mac\_detecter](#magicm-detector-hardware-cpu-mac_detecter)
- 🅼 [magicm\.detector\.hardware\.cpu\.win\_detecter](#magicm-detector-hardware-cpu-win_detecter)
- 🅼 [magicm\.detector\.hardware\.gpu](#magicm-detector-hardware-gpu)
- 🅼 [magicm\.detector\.hardware\.gpu\.amd](#magicm-detector-hardware-gpu-amd)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands](#magicm-detector-hardware-gpu-commands)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.amd\_command](#magicm-detector-hardware-gpu-commands-amd_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.apple\_command](#magicm-detector-hardware-gpu-commands-apple_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.huawei\_command](#magicm-detector-hardware-gpu-commands-huawei_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.intel\_command](#magicm-detector-hardware-gpu-commands-intel_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command](#magicm-detector-hardware-gpu-commands-nvidia_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command](#magicm-detector-hardware-gpu-commands-qualcomm_command)
- 🅼 [magicm\.detector\.hardware\.gpu\.core](#magicm-detector-hardware-gpu-core)
- 🅼 [magicm\.detector\.hardware\.gpu\.core\.base](#magicm-detector-hardware-gpu-core-base)
- 🅼 [magicm\.detector\.hardware\.gpu\.core\.command\_executor](#magicm-detector-hardware-gpu-core-command_executor)
- 🅼 [magicm\.detector\.hardware\.gpu\.core\.factory](#magicm-detector-hardware-gpu-core-factory)
- 🅼 [magicm\.detector\.hardware\.gpu\.gpu\_detecter](#magicm-detector-hardware-gpu-gpu_detecter)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor](#magicm-detector-hardware-gpu-vendor)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor\.amd](#magicm-detector-hardware-gpu-vendor-amd)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor\.huawei](#magicm-detector-hardware-gpu-vendor-huawei)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor\.intel](#magicm-detector-hardware-gpu-vendor-intel)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor\.nvidia](#magicm-detector-hardware-gpu-vendor-nvidia)
- 🅼 [magicm\.detector\.hardware\.gpu\.vendor\.utils](#magicm-detector-hardware-gpu-vendor-utils)
- 🅼 [magicm\.detector\.hardware\.mem](#magicm-detector-hardware-mem)
- 🅼 [magicm\.detector\.hardware\.mem\.mem\_detecter](#magicm-detector-hardware-mem-mem_detecter)
- 🅼 [magicm\.detector\.software](#magicm-detector-software)
- 🅼 [magicm\.detector\.software\.driver](#magicm-detector-software-driver)
- 🅼 [magicm\.detector\.software\.driver\.cann](#magicm-detector-software-driver-cann)
- 🅼 [magicm\.detector\.software\.driver\.cuda](#magicm-detector-software-driver-cuda)
- 🅼 [magicm\.detector\.software\.driver\.driver\_detecter](#magicm-detector-software-driver-driver_detecter)
- 🅼 [magicm\.detector\.software\.driver\.oneapi](#magicm-detector-software-driver-oneapi)
- 🅼 [magicm\.detector\.software\.driver\.rocm](#magicm-detector-software-driver-rocm)
- 🅼 [magicm\.detector\.software\.system](#magicm-detector-software-system)
- 🅼 [magicm\.detector\.software\.system\.linux\_detecter](#magicm-detector-software-system-linux_detecter)
- 🅼 [magicm\.detector\.software\.system\.mac\_detecter](#magicm-detector-software-system-mac_detecter)
- 🅼 [magicm\.detector\.software\.system\.sys\_detecter](#magicm-detector-software-system-sys_detecter)
- 🅼 [magicm\.detector\.software\.system\.win\_detecter](#magicm-detector-software-system-win_detecter)
- 🅼 [magicm\.management](#magicm-management)
- 🅼 [magicm\.management\.config](#magicm-management-config)
- 🅼 [magicm\.management\.config\.configLoader](#magicm-management-config-configLoader)
- 🅼 [magicm\.management\.config\.configManager](#magicm-management-config-configManager)
- 🅼 [magicm\.management\.config\.configPathManager](#magicm-management-config-configPathManager)
- 🅼 [magicm\.management\.config\.configReader](#magicm-management-config-configReader)
- 🅼 [magicm\.management\.config\.configWriter](#magicm-management-config-configWriter)
- 🅼 [magicm\.utils](#magicm-utils)
- 🅼 [magicm\.utils\.util](#magicm-utils-util)

<a name="magicm"></a>
## 🅼 magicm
<a name="magicm-cli"></a>
## 🅼 magicm\.cli

magicm CLI 硬件检测工具

- **Functions:**
  - 🅵 [main](#magicm-cli-main)

### Functions

<a name="magicm-cli-main"></a>
### 🅵 magicm\.cli\.main

```python
def main():
```

主函数：顺序调用各检测模块，然后交给 display 显示
<a name="magicm-command"></a>
## 🅼 magicm\.command
<a name="magicm-command-deploy"></a>
## 🅼 magicm\.command\.deploy
<a name="magicm-command-detecter"></a>
## 🅼 magicm\.command\.detecter

magicm CLI 硬件检测工具

- **Functions:**
  - 🅵 [get\_system\_info](#magicm-command-detecter-get_system_info)
  - 🅵 [get\_cpu\_info](#magicm-command-detecter-get_cpu_info)
  - 🅵 [get\_gpu\_info](#magicm-command-detecter-get_gpu_info)
  - 🅵 [get\_memory\_info](#magicm-command-detecter-get_memory_info)
  - 🅵 [detect](#magicm-command-detecter-detect)

### Functions

<a name="magicm-command-detecter-get_system_info"></a>
### 🅵 magicm\.command\.detecter\.get\_system\_info

```python
def get_system_info():
```

获取系统信息
<a name="magicm-command-detecter-get_cpu_info"></a>
### 🅵 magicm\.command\.detecter\.get\_cpu\_info

```python
def get_cpu_info():
```

获取CPU信息
<a name="magicm-command-detecter-get_gpu_info"></a>
### 🅵 magicm\.command\.detecter\.get\_gpu\_info

```python
def get_gpu_info():
```

获取GPU信息
<a name="magicm-command-detecter-get_memory_info"></a>
### 🅵 magicm\.command\.detecter\.get\_memory\_info

```python
def get_memory_info():
```

获取内存信息
<a name="magicm-command-detecter-detect"></a>
### 🅵 magicm\.command\.detecter\.detect

```python
def detect():
```

主函数：顺序调用各检测模块，然后交给 display 显示
<a name="magicm-command-display"></a>
## 🅼 magicm\.command\.display

硬件检测结果显示模块（主入口）

这是对外的主要接口，保持向后兼容

- **Functions:**
  - 🅵 [create\_display](#magicm-command-display-create_display)
  - 🅵 [display\_hardware\_info](#magicm-command-display-display_hardware_info)
  - 🅵 [format\_hardware\_info](#magicm-command-display-format_hardware_info)
- **Classes:**
  - 🅲 [HardwareDisplay](#magicm-command-display-HardwareDisplay)

### Functions

<a name="magicm-command-display-create_display"></a>
### 🅵 magicm\.command\.display\.create\_display

```python
def create_display(config_path: Optional[str] = None) -> HardwareDisplay:
```

创建硬件显示器实例

**Parameters:**

- **config_path**: 配置文件路径

**Returns:**

- HardwareDisplay实例
<a name="magicm-command-display-display_hardware_info"></a>
### 🅵 magicm\.command\.display\.display\_hardware\_info

```python
def display_hardware_info(system_info: Dict[str, Any], config_path: Optional[str] = None):
```

显示硬件信息（便捷函数）

Args:
    system\_info: \{
        'system':   ,
        'cpu':      ,
        'gpu':      ,
        'mem':      
    \},        
    config\_path: 配置文件路径
<a name="magicm-command-display-format_hardware_info"></a>
### 🅵 magicm\.command\.display\.format\_hardware\_info

```python
def format_hardware_info(system_info: Dict[str, Any], cpu_info: Dict[str, Any], gpu_info: Dict[str, Any], memory_info: Dict[str, Any], config_path: Optional[str] = None, width: int = 100) -> str:
```

格式化硬件信息为文本（便捷函数）

**Parameters:**

- **system_info**: 系统信息
- **cpu_info**: CPU信息
- **gpu_info**: GPU信息
- **memory_info**: 内存信息
- **config_path**: 配置文件路径
- **width**: 文本宽度

**Returns:**

- 格式化的文本字符串

### Classes

<a name="magicm-command-display-HardwareDisplay"></a>
### 🅲 magicm\.command\.display\.HardwareDisplay

```python
class HardwareDisplay:
```

硬件检测结果展示类（门面模式）

**Functions:**

<a name="magicm-command-display-HardwareDisplay-__init__"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.\_\_init\_\_

```python
def __init__(self, config: Optional[Dict[str, Any]] = None, config_path: Optional[str] = None):
```

初始化硬件显示器

**Parameters:**

- **config**: 配置字典（可选）
- **config_path**: 配置文件路径（可选）
<a name="magicm-command-display-HardwareDisplay-display_all"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.display\_all

```python
def display_all(self, system_info: Dict[str, Any]):
```

显示所有硬件信息（控制台输出）

Args:
    system\_info: 系统信息, \{
        'system':   system\_info,
        'cpu':      cpu\_info,
        'gpu':      gpu\_info,
        'mem':      memory\_info
    \}
<a name="magicm-command-display-HardwareDisplay-format_text"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.format\_text

```python
def format_text(self, system_info: Dict[str, Any], cpu_info: Dict[str, Any], gpu_info: Dict[str, Any], memory_info: Dict[str, Any], width: int = 100) -> str:
```

返回格式化的文本

**Parameters:**

- **system_info**: 系统信息
- **cpu_info**: CPU信息
- **gpu_info**: GPU信息
- **memory_info**: 内存信息
- **width**: 文本宽度

**Returns:**

- 格式化的文本字符串
<a name="magicm-command-display-HardwareDisplay-get_gpu_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_gpu\_rating

```python
def get_gpu_rating(self, gpu_name: str) -> str:
```

获取GPU评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-get_vram_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_vram\_rating

```python
def get_vram_rating(self, vram_gb: int) -> str:
```

获取显存评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-get_driver_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_driver\_rating

```python
def get_driver_rating(self, driver_version: str) -> str:
```

获取驱动评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-get_system_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_system\_rating

```python
def get_system_rating(self, os_name: str) -> str:
```

获取系统评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-get_cpu_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_cpu\_rating

```python
def get_cpu_rating(self, cpu_model: str) -> str:
```

获取CPU评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-get_memory_rating"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.get\_memory\_rating

```python
def get_memory_rating(self, memory_gb: int) -> str:
```

获取内存评级（向后兼容）
<a name="magicm-command-display-HardwareDisplay-show_banner"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.show\_banner

```python
def show_banner(self):
```

显示欢迎横幅（向后兼容）
<a name="magicm-command-display-HardwareDisplay-show_footer"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.show\_footer

```python
def show_footer(self):
```

显示页脚（向后兼容）
<a name="magicm-command-display-HardwareDisplay-reload_config"></a>
#### 🅵 magicm\.command\.display\.HardwareDisplay\.reload\_config

```python
def reload_config(self, config_path: Optional[str] = None):
```

重新加载配置

**Parameters:**

- **config_path**: 配置文件路径（可选）
<a name="magicm-detector"></a>
## 🅼 magicm\.detector
<a name="magicm-detector-hardware"></a>
## 🅼 magicm\.detector\.hardware
<a name="magicm-detector-hardware-cpu"></a>
## 🅼 magicm\.detector\.hardware\.cpu
<a name="magicm-detector-hardware-cpu-cpu_detecter"></a>
## 🅼 magicm\.detector\.hardware\.cpu\.cpu\_detecter

- **Functions:**
  - 🅵 [cpu\_detected](#magicm-detector-hardware-cpu-cpu_detecter-cpu_detected)
  - 🅵 [get\_cpu\_summary](#magicm-detector-hardware-cpu-cpu_detecter-get_cpu_summary)

### Functions

<a name="magicm-detector-hardware-cpu-cpu_detecter-cpu_detected"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.cpu\_detecter\.cpu\_detected

```python
def cpu_detected():
```

检测CPU信息 - 增强版
<a name="magicm-detector-hardware-cpu-cpu_detecter-get_cpu_summary"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.cpu\_detecter\.get\_cpu\_summary

```python
def get_cpu_summary():
```

获取CPU摘要信息
<a name="magicm-detector-hardware-cpu-cpu_model"></a>
## 🅼 magicm\.detector\.hardware\.cpu\.cpu\_model

- **Functions:**
  - 🅵 [cpu\_model](#magicm-detector-hardware-cpu-cpu_model-cpu_model)

### Functions

<a name="magicm-detector-hardware-cpu-cpu_model-cpu_model"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.cpu\_model\.cpu\_model

```python
def cpu_model(model):
```

通用的CPU型号简化函数。

该函数通过正则表达式匹配常见的CPU型号模式，从完整的CPU品牌字符串中
提取出核心型号信息，使显示更加简洁清晰。

**Parameters:**

- **model** (`str`): CPU的完整原始名称字符串。
例如: "AMD Ryzen 7 8845HS w/ Radeon 780M Graphics"
"Intel\(R\) Core\(TM\) i7-12700K CPU @ 3\.60GHz"

**Returns:**

- `str`: 简化后的CPU型号。
- AMD Ryzen示例: "Ryzen 7 8845HS"
- Intel Core示例: "i7-12700K"
- 输入为空时: "未知"
- 无法匹配时: 返回原始输入值
<a name="magicm-detector-hardware-cpu-linux_detecter"></a>
## 🅼 magicm\.detector\.hardware\.cpu\.linux\_detecter

- **Functions:**
  - 🅵 [detecter](#magicm-detector-hardware-cpu-linux_detecter-detecter)

### Functions

<a name="magicm-detector-hardware-cpu-linux_detecter-detecter"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.linux\_detecter\.detecter

```python
def detecter():
```

Linux系统CPU检测函数。

该函数通过读取系统文件 /proc/cpuinfo 或使用 lscpu 命令来获取
Linux系统下的CPU型号信息，并使用外部模型简化函数对型号进行精简。

**Returns:**

- `dict`: 包含两个键的字典：
- 'model' \(str\): CPU的完整原始名称。
- 'simple\_model' \(str\): 经过简化处理的CPU型号，更适合直接展示。
<a name="magicm-detector-hardware-cpu-mac_detecter"></a>
## 🅼 magicm\.detector\.hardware\.cpu\.mac\_detecter

- **Functions:**
  - 🅵 [detect](#magicm-detector-hardware-cpu-mac_detecter-detect)

### Functions

<a name="magicm-detector-hardware-cpu-mac_detecter-detect"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.mac\_detecter\.detect

```python
def detect():
```

macOS系统CPU检测函数。

该函数通过 sysctl 命令获取 macOS 系统下的 CPU 品牌字符串信息，
并使用外部模型简化函数对型号进行精简处理。

**Returns:**

- `dict`: 包含两个键的字典：
- 'model' \(str\): CPU的完整原始品牌字符串。
- 'simple\_model' \(str\): 经过简化处理的CPU型号，更适合直接展示。
<a name="magicm-detector-hardware-cpu-win_detecter"></a>
## 🅼 magicm\.detector\.hardware\.cpu\.win\_detecter

- **Functions:**
  - 🅵 [detecter](#magicm-detector-hardware-cpu-win_detecter-detecter)

### Functions

<a name="magicm-detector-hardware-cpu-win_detecter-detecter"></a>
### 🅵 magicm\.detector\.hardware\.cpu\.win\_detecter\.detecter

```python
def detecter():
```

Windows系统CPU检测函数。

该函数通过多种方式（WMI、PowerShell、注册表）获取Windows系统下的CPU型号信息，
并针对AMD处理器显示不完整的问题进行了专门处理。

**Returns:**

- `dict`: 包含两个键的字典：
- 'model' \(str\): CPU的完整原始名称。
- 'simple\_model' \(str\): 经过简化处理的CPU型号，更适合直接展示。
<a name="magicm-detector-hardware-gpu"></a>
## 🅼 magicm\.detector\.hardware\.gpu
<a name="magicm-detector-hardware-gpu-amd"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.amd
<a name="magicm-detector-hardware-gpu-commands"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands

- **[Exports](#magicm-detector-hardware-gpu-commands-exports)**

<a name="magicm-detector-hardware-gpu-commands-exports"></a>
### Exports

- 🅼 [`NVIDIACommand`](#magicm-detector-hardware-gpu-commands-NVIDIACommand)
- 🅼 [`AMDCommand`](#magicm-detector-hardware-gpu-commands-AMDCommand)
- 🅼 [`IntelCommand`](#magicm-detector-hardware-gpu-commands-IntelCommand)
- 🅼 [`HuaweiCommand`](#magicm-detector-hardware-gpu-commands-HuaweiCommand)
<a name="magicm-detector-hardware-gpu-commands-amd_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.amd\_command

- **Classes:**
  - 🅲 [AMDCommand](#magicm-detector-hardware-gpu-commands-amd_command-AMDCommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-amd_command-AMDCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.amd\_command\.AMDCommand

```python
class AMDCommand(GPUDetectionCommand):
```

AMD GPU检测命令

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-amd_command-AMDCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.amd\_command\.AMDCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-amd_command-AMDCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.amd\_command\.AMDCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-amd_command-AMDCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.amd\_command\.AMDCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行AMD GPU检测
<a name="magicm-detector-hardware-gpu-commands-apple_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.apple\_command

- **Classes:**
  - 🅲 [AppleCommand](#magicm-detector-hardware-gpu-commands-apple_command-AppleCommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-apple_command-AppleCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.apple\_command\.AppleCommand

```python
class AppleCommand(GPUDetectionCommand):
```

Apple Silicon GPU检测命令 - 新增厂商示例

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-apple_command-AppleCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.apple\_command\.AppleCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-apple_command-AppleCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.apple\_command\.AppleCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-apple_command-AppleCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.apple\_command\.AppleCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Apple Silicon GPU检测
<a name="magicm-detector-hardware-gpu-commands-huawei_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.huawei\_command

- **Classes:**
  - 🅲 [HuaweiCommand](#magicm-detector-hardware-gpu-commands-huawei_command-HuaweiCommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-huawei_command-HuaweiCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand

```python
class HuaweiCommand(GPUDetectionCommand):
```

华为昇腾GPU检测命令

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-huawei_command-HuaweiCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-huawei_command-HuaweiCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-huawei_command-HuaweiCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行华为昇腾GPU检测
<a name="magicm-detector-hardware-gpu-commands-intel_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.intel\_command

- **Classes:**
  - 🅲 [IntelCommand](#magicm-detector-hardware-gpu-commands-intel_command-IntelCommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-intel_command-IntelCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.intel\_command\.IntelCommand

```python
class IntelCommand(GPUDetectionCommand):
```

Intel GPU检测命令

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-intel_command-IntelCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.intel\_command\.IntelCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-intel_command-IntelCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.intel\_command\.IntelCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-intel_command-IntelCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.intel\_command\.IntelCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Intel GPU检测
<a name="magicm-detector-hardware-gpu-commands-nvidia_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command

- **Classes:**
  - 🅲 [NVIDIACommand](#magicm-detector-hardware-gpu-commands-nvidia_command-NVIDIACommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-nvidia_command-NVIDIACommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand

```python
class NVIDIACommand(GPUDetectionCommand):
```

NVIDIA GPU检测命令

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-nvidia_command-NVIDIACommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-nvidia_command-NVIDIACommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-nvidia_command-NVIDIACommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行NVIDIA GPU检测
<a name="magicm-detector-hardware-gpu-commands-qualcomm_command"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command

- **Classes:**
  - 🅲 [QualcommCommand](#magicm-detector-hardware-gpu-commands-qualcomm_command-QualcommCommand)

### Classes

<a name="magicm-detector-hardware-gpu-commands-qualcomm_command-QualcommCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand

```python
class QualcommCommand(GPUDetectionCommand):
```

高通Adreno GPU检测命令 - 新增厂商示例

**Functions:**

<a name="magicm-detector-hardware-gpu-commands-qualcomm_command-QualcommCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-commands-qualcomm_command-QualcommCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="magicm-detector-hardware-gpu-commands-qualcomm_command-QualcommCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行高通Adreno GPU检测
<a name="magicm-detector-hardware-gpu-core"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.core
<a name="magicm-detector-hardware-gpu-core-base"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.core\.base

- **Classes:**
  - 🅲 [SystemType](#magicm-detector-hardware-gpu-core-base-SystemType)
  - 🅲 [GPUVendor](#magicm-detector-hardware-gpu-core-base-GPUVendor)
  - 🅲 [GPUType](#magicm-detector-hardware-gpu-core-base-GPUType)
  - 🅲 [GPUInfo](#magicm-detector-hardware-gpu-core-base-GPUInfo)
  - 🅲 [DetectionResult](#magicm-detector-hardware-gpu-core-base-DetectionResult)
  - 🅲 [GPUDetectionCommand](#magicm-detector-hardware-gpu-core-base-GPUDetectionCommand)
  - 🅲 [PlatformAdapter](#magicm-detector-hardware-gpu-core-base-PlatformAdapter)

### Classes

<a name="magicm-detector-hardware-gpu-core-base-SystemType"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.SystemType

```python
class SystemType(Enum):
```

系统类型 - 扩展少
<a name="magicm-detector-hardware-gpu-core-base-GPUVendor"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.GPUVendor

```python
class GPUVendor(Enum):
```

GPU厂商 - 扩展多
<a name="magicm-detector-hardware-gpu-core-base-GPUType"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.GPUType

```python
class GPUType(Enum):
```

GPU类型
<a name="magicm-detector-hardware-gpu-core-base-GPUInfo"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.GPUInfo

```python
class GPUInfo:
```

GPU信息数据类 - 兼容原有API

**Functions:**

<a name="magicm-detector-hardware-gpu-core-base-GPUInfo-to_dict"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.GPUInfo\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="magicm-detector-hardware-gpu-core-base-DetectionResult"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.DetectionResult

```python
class DetectionResult:
```

检测结果数据类 - 兼容原有API

**Functions:**

<a name="magicm-detector-hardware-gpu-core-base-DetectionResult-main_gpu"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.DetectionResult\.main\_gpu

```python
def main_gpu(self) -> Optional[GPUInfo]:
```

获取主GPU（优先离散，其次集成）
<a name="magicm-detector-hardware-gpu-core-base-DetectionResult-to_dict"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.DetectionResult\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="magicm-detector-hardware-gpu-core-base-GPUDetectionCommand"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.GPUDetectionCommand

```python
class GPUDetectionCommand(ABC):
```

GPU检测命令接口

**Functions:**

<a name="magicm-detector-hardware-gpu-core-base-GPUDetectionCommand-execute"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.GPUDetectionCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行检测命令
<a name="magicm-detector-hardware-gpu-core-base-GPUDetectionCommand-get_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.GPUDetectionCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```

返回厂商类型
<a name="magicm-detector-hardware-gpu-core-base-GPUDetectionCommand-get_priority"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.GPUDetectionCommand\.get\_priority

```python
def get_priority(self) -> int:
```

优先级（数值越小越先执行）
<a name="magicm-detector-hardware-gpu-core-base-PlatformAdapter"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.base\.PlatformAdapter

```python
class PlatformAdapter(ABC):
```

平台适配器接口

**Functions:**

<a name="magicm-detector-hardware-gpu-core-base-PlatformAdapter-get_system_type"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.PlatformAdapter\.get\_system\_type

```python
def get_system_type(self) -> SystemType:
```

获取系统类型
<a name="magicm-detector-hardware-gpu-core-base-PlatformAdapter-run_command"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.PlatformAdapter\.run\_command

```python
def run_command(self, cmd: str) -> tuple:
```

执行命令
<a name="magicm-detector-hardware-gpu-core-base-PlatformAdapter-get_gpu_list"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.base\.PlatformAdapter\.get\_gpu\_list

```python
def get_gpu_list(self) -> List[Dict[str, Any]]:
```

获取GPU原始列表
<a name="magicm-detector-hardware-gpu-core-command_executor"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.core\.command\_executor

- **Classes:**
  - 🅲 [CommandRegistry](#magicm-detector-hardware-gpu-core-command_executor-CommandRegistry)
  - 🅲 [GPUCommandExecutor](#magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor)

### Classes

<a name="magicm-detector-hardware-gpu-core-command_executor-CommandRegistry"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.CommandRegistry

```python
class CommandRegistry:
```

命令注册器

**Functions:**

<a name="magicm-detector-hardware-gpu-core-command_executor-CommandRegistry-register"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.CommandRegistry\.register

```python
def register(cls, command: GPUDetectionCommand):
```

注册命令
<a name="magicm-detector-hardware-gpu-core-command_executor-CommandRegistry-get"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.CommandRegistry\.get

```python
def get(cls, vendor: GPUVendor) -> Optional[GPUDetectionCommand]:
```

获取命令
<a name="magicm-detector-hardware-gpu-core-command_executor-CommandRegistry-get_all"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.CommandRegistry\.get\_all

```python
def get_all(cls) -> List[GPUDetectionCommand]:
```

获取所有命令（按优先级排序）
<a name="magicm-detector-hardware-gpu-core-command_executor-CommandRegistry-clear"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.CommandRegistry\.clear

```python
def clear(cls):
```

清空所有命令
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor

```python
class GPUCommandExecutor:
```

GPU命令执行器 - 核心业务逻辑

**Functions:**

<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-__init__"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.\_\_init\_\_

```python
def __init__(self, system: str = None):
```

初始化执行器

**Parameters:**

- **system**: 系统类型 \(linux/windows/macos\)，None表示自动检测
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-detect_all"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU - 返回DetectionResult
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-detect_by_vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_by\_vendor

```python
def detect_by_vendor(self, vendor: GPUVendor) -> List[GPUInfo]:
```

检测特定厂商的GPU
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-add_command"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.add\_command

```python
def add_command(self, command: GPUDetectionCommand):
```

动态添加命令（用于扩展）
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-remove_command"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.remove\_command

```python
def remove_command(self, vendor: GPUVendor):
```

移除命令
<a name="magicm-detector-hardware-gpu-core-command_executor-GPUCommandExecutor-get_registered_vendors"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.get\_registered\_vendors

```python
def get_registered_vendors(self) -> List[GPUVendor]:
```

获取已注册的厂商列表
<a name="magicm-detector-hardware-gpu-core-factory"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.core\.factory

- **Classes:**
  - 🅲 [GPUDetectorFactory](#magicm-detector-hardware-gpu-core-factory-GPUDetectorFactory)

### Classes

<a name="magicm-detector-hardware-gpu-core-factory-GPUDetectorFactory"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.core\.factory\.GPUDetectorFactory

```python
class GPUDetectorFactory:
```

GPU检测器工厂

**Functions:**

<a name="magicm-detector-hardware-gpu-core-factory-GPUDetectorFactory-__init__"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.factory\.GPUDetectorFactory\.\_\_init\_\_

```python
def __init__(self):
```
<a name="magicm-detector-hardware-gpu-core-factory-GPUDetectorFactory-get_detector"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.factory\.GPUDetectorFactory\.get\_detector

```python
def get_detector(self, lspci_line: str, gpu_name: str) -> Optional[BaseGPUDetector]:
```

根据lspci行获取合适的检测器
<a name="magicm-detector-hardware-gpu-core-factory-GPUDetectorFactory-detect_all"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.core\.factory\.GPUDetectorFactory\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU
<a name="magicm-detector-hardware-gpu-gpu_detecter"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.gpu\_detecter

- **Functions:**
  - 🅵 [gpu\_detected](#magicm-detector-hardware-gpu-gpu_detecter-gpu_detected)
  - 🅵 [get\_gpu\_summary](#magicm-detector-hardware-gpu-gpu_detecter-get_gpu_summary)

### Functions

<a name="magicm-detector-hardware-gpu-gpu_detecter-gpu_detected"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.gpu\_detecter\.gpu\_detected

```python
def gpu_detected() -> Dict[str, Any]:
```

检测GPU信息（独立显卡和集成显卡）

这是API文档中定义的接口，保持向后兼容

**Returns:**

- `Dict`: GPU检测结果字典
<a name="magicm-detector-hardware-gpu-gpu_detecter-get_gpu_summary"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.gpu\_detecter\.get\_gpu\_summary

```python
def get_gpu_summary() -> Dict[str, Any]:
```

获取GPU摘要信息

这是API文档中定义的接口

**Returns:**

- `Dict`: GPU摘要信息
<a name="magicm-detector-hardware-gpu-vendor"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor
<a name="magicm-detector-hardware-gpu-vendor-amd"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor\.amd

- **Classes:**
  - 🅲 [AMDDetector](#magicm-detector-hardware-gpu-vendor-amd-AMDDetector)

### Classes

<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector

```python
class AMDDetector(BaseGPUDetector):
```

AMD GPU检测器

**Functions:**

<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector-vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector-detect_from_lspci"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测AMD GPU
<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector-detect_driver_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测AMD驱动版本
<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector-detect_rocm_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_rocm\_version

```python
def detect_rocm_version(self) -> Optional[str]:
```

检测ROCm版本
<a name="magicm-detector-hardware-gpu-vendor-amd-AMDDetector-enhance_gpu_info"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强AMD GPU信息
<a name="magicm-detector-hardware-gpu-vendor-huawei"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor\.huawei

- **Classes:**
  - 🅲 [HuaweiDetector](#magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector)

### Classes

<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector

```python
class HuaweiDetector(BaseGPUDetector):
```

华为昇腾GPU检测器

**Functions:**

<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector-vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_from_lspci"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测华为昇腾GPU
<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_driver_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测昇腾驱动版本
<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_ascend_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_ascend\_version

```python
def detect_ascend_version(self) -> Optional[str]:
```

检测CANN版本
<a name="magicm-detector-hardware-gpu-vendor-huawei-HuaweiDetector-enhance_gpu_info"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强昇腾GPU信息
<a name="magicm-detector-hardware-gpu-vendor-intel"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor\.intel

- **Classes:**
  - 🅲 [IntelDetector](#magicm-detector-hardware-gpu-vendor-intel-IntelDetector)

### Classes

<a name="magicm-detector-hardware-gpu-vendor-intel-IntelDetector"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.vendor\.intel\.IntelDetector

```python
class IntelDetector(BaseGPUDetector):
```

Intel GPU检测器

**Functions:**

<a name="magicm-detector-hardware-gpu-vendor-intel-IntelDetector-vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-vendor-intel-IntelDetector-detect_from_lspci"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测Intel GPU
<a name="magicm-detector-hardware-gpu-vendor-intel-IntelDetector-detect_driver_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测Intel驱动版本
<a name="magicm-detector-hardware-gpu-vendor-nvidia"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor\.nvidia

- **Classes:**
  - 🅲 [NVIDIADetector](#magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector)

### Classes

<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector"></a>
### 🅲 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector

```python
class NVIDIADetector(BaseGPUDetector):
```

NVIDIA GPU检测器

**Functions:**

<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-vendor"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_from_lspci"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测NVIDIA GPU
<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_driver_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测NVIDIA驱动版本
<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_cuda_version"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_cuda\_version

```python
def detect_cuda_version(self) -> Optional[str]:
```

检测CUDA版本
<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_nvlink"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_nvlink

```python
def detect_nvlink(self) -> Dict[str, Any]:
```

检测NVLink状态
<a name="magicm-detector-hardware-gpu-vendor-nvidia-NVIDIADetector-enhance_gpu_info"></a>
#### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强NVIDIA GPU信息
<a name="magicm-detector-hardware-gpu-vendor-utils"></a>
## 🅼 magicm\.detector\.hardware\.gpu\.vendor\.utils

- **Functions:**
  - 🅵 [run\_cmd\_safe](#magicm-detector-hardware-gpu-vendor-utils-run_cmd_safe)
  - 🅵 [extract\_gpu\_name](#magicm-detector-hardware-gpu-vendor-utils-extract_gpu_name)
  - 🅵 [get\_gpu\_memory](#magicm-detector-hardware-gpu-vendor-utils-get_gpu_memory)
  - 🅵 [get\_gpu\_specs](#magicm-detector-hardware-gpu-vendor-utils-get_gpu_specs)

### Functions

<a name="magicm-detector-hardware-gpu-vendor-utils-run_cmd_safe"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.utils\.run\_cmd\_safe

```python
def run_cmd_safe(cmd: str, timeout: int = 5):
```

安全执行命令
<a name="magicm-detector-hardware-gpu-vendor-utils-extract_gpu_name"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.utils\.extract\_gpu\_name

```python
def extract_gpu_name(line: str) -> str:
```

从 lspci 输出中提取干净的 GPU 名称
<a name="magicm-detector-hardware-gpu-vendor-utils-get_gpu_memory"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.utils\.get\_gpu\_memory

```python
def get_gpu_memory(gpu_name: str, gpu_raw_line: Optional[str] = None) -> Optional[int]:
```

获取 GPU 显存大小（GB）
<a name="magicm-detector-hardware-gpu-vendor-utils-get_gpu_specs"></a>
### 🅵 magicm\.detector\.hardware\.gpu\.vendor\.utils\.get\_gpu\_specs

```python
def get_gpu_specs(gpu_name: str) -> Optional[Dict[str, Any]]:
```

根据GPU名称获取完整规格
<a name="magicm-detector-hardware-mem"></a>
## 🅼 magicm\.detector\.hardware\.mem
<a name="magicm-detector-hardware-mem-mem_detecter"></a>
## 🅼 magicm\.detector\.hardware\.mem\.mem\_detecter

- **Constants:**
  - 🆅 [MEMORY\_SPECS](#magicm-detector-hardware-mem-mem_detecter-MEMORY_SPECS)
- **Functions:**
  - 🅵 [match\_memory\_spec](#magicm-detector-hardware-mem-mem_detecter-match_memory_spec)
  - 🅵 [mem\_detected](#magicm-detector-hardware-mem-mem_detecter-mem_detected)

### Constants

<a name="magicm-detector-hardware-mem-mem_detecter-MEMORY_SPECS"></a>
### 🆅 magicm\.detector\.hardware\.mem\.mem\_detecter\.MEMORY\_SPECS

```python
MEMORY_SPECS = [2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
```

### Functions

<a name="magicm-detector-hardware-mem-mem_detecter-match_memory_spec"></a>
### 🅵 magicm\.detector\.hardware\.mem\.mem\_detecter\.match\_memory\_spec

```python
def match_memory_spec(total_bytes):
```

根据实际内存大小，匹配最接近的标准规格

512GB 及以下：向上匹配到标准规格
512GB 以上：返回 512（表示 512GB 或更多）
<a name="magicm-detector-hardware-mem-mem_detecter-mem_detected"></a>
### 🅵 magicm\.detector\.hardware\.mem\.mem\_detecter\.mem\_detected

```python
def mem_detected():
```

检测内存信息 - 使用规格匹配算法
<a name="magicm-detector-software"></a>
## 🅼 magicm\.detector\.software
<a name="magicm-detector-software-driver"></a>
## 🅼 magicm\.detector\.software\.driver
<a name="magicm-detector-software-driver-cann"></a>
## 🅼 magicm\.detector\.software\.driver\.cann
<a name="magicm-detector-software-driver-cuda"></a>
## 🅼 magicm\.detector\.software\.driver\.cuda
<a name="magicm-detector-software-driver-driver_detecter"></a>
## 🅼 magicm\.detector\.software\.driver\.driver\_detecter
<a name="magicm-detector-software-driver-oneapi"></a>
## 🅼 magicm\.detector\.software\.driver\.oneapi
<a name="magicm-detector-software-driver-rocm"></a>
## 🅼 magicm\.detector\.software\.driver\.rocm
<a name="magicm-detector-software-system"></a>
## 🅼 magicm\.detector\.software\.system
<a name="magicm-detector-software-system-linux_detecter"></a>
## 🅼 magicm\.detector\.software\.system\.linux\_detecter

Linux 系统检测模块

- **Functions:**
  - 🅵 [detect](#magicm-detector-software-system-linux_detecter-detect)

### Functions

<a name="magicm-detector-software-system-linux_detecter-detect"></a>
### 🅵 magicm\.detector\.software\.system\.linux\_detecter\.detect

```python
def detect():
```

检测 Linux 系统
<a name="magicm-detector-software-system-mac_detecter"></a>
## 🅼 magicm\.detector\.software\.system\.mac\_detecter

- **Functions:**
  - 🅵 [detect](#magicm-detector-software-system-mac_detecter-detect)

### Functions

<a name="magicm-detector-software-system-mac_detecter-detect"></a>
### 🅵 magicm\.detector\.software\.system\.mac\_detecter\.detect

```python
def detect():
```

检测 macOS 系统
<a name="magicm-detector-software-system-sys_detecter"></a>
## 🅼 magicm\.detector\.software\.system\.sys\_detecter

- **Functions:**
  - 🅵 [detect](#magicm-detector-software-system-sys_detecter-detect)

### Functions

<a name="magicm-detector-software-system-sys_detecter-detect"></a>
### 🅵 magicm\.detector\.software\.system\.sys\_detecter\.detect

```python
def detect():
```

检测操作系统信息 - 增强版
<a name="magicm-detector-software-system-win_detecter"></a>
## 🅼 magicm\.detector\.software\.system\.win\_detecter

Windows 系统检测模块

- **Functions:**
  - 🅵 [detect](#magicm-detector-software-system-win_detecter-detect)

### Functions

<a name="magicm-detector-software-system-win_detecter-detect"></a>
### 🅵 magicm\.detector\.software\.system\.win\_detecter\.detect

```python
def detect():
```
<a name="magicm-management"></a>
## 🅼 magicm\.management
<a name="magicm-management-config"></a>
## 🅼 magicm\.management\.config
<a name="magicm-management-config-configLoader"></a>
## 🅼 magicm\.management\.config\.configLoader

YAML 配置加载器 - 配置文件的加载和合并模块

该模块提供 YAML 配置文件的加载功能，支持项目配置和用户配置的自动合并。
支持开发环境和打包环境，自动处理不同环境下的路径问题。

核心功能：
- 加载项目配置文件
- 加载并合并用户配置（用户配置覆盖项目配置）
- 支持嵌套路径的配置路径获取
- 支持打包环境的路径适配

使用示例:
    from magicm\.management\.config import ConfigLoader
    
    \# 方式1：直接加载指定路径的配置
    loader = ConfigLoader\(\)
    config = loader\.load\('display', 'config\.yaml'\)
    
    \# 方式2：使用模块名加载（支持用户配置合并）
    loader = ConfigLoader\('display', 'config\.yaml'\)
    config = loader\.load\_merged\(\)  \# 自动合并用户配置

- **Classes:**
  - 🅲 [ConfigLoader](#magicm-management-config-configLoader-ConfigLoader)

### Classes

<a name="magicm-management-config-configLoader-ConfigLoader"></a>
### 🅲 magicm\.management\.config\.configLoader\.ConfigLoader

```python
class ConfigLoader:
```

YAML 配置加载器 - 支持嵌套路径和配置合并

该类负责从文件系统加载 YAML 配置文件，支持：
1\. 直接加载指定路径的配置文件
2\. 按模块名加载（自动定位项目配置和用户配置）
3\. 项目配置与用户配置的深度合并
4\. 开发环境和打包环境的路径自动适配

配置优先级（从低到高）：
- 项目配置：项目源码中的默认配置（只读）
- 用户配置：用户目录中的自定义配置（可写，覆盖项目配置）

**Attributes:**

- **module_name** (`str`): 模块名称，如 'display'
- **config_filename** (`str`): 配置文件名，如 'config\.yaml'
- **_project_root** (`Optional[Path]`): 项目根目录缓存
- **_using_user_config** (`bool`): 当前是否使用用户配置
- **_current_config_path** (`Optional[Path]`): 当前加载的配置文件路径

**Functions:**

<a name="magicm-management-config-configLoader-ConfigLoader-__init__"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.\_\_init\_\_

```python
def __init__(self):
```

初始化配置加载器
<a name="magicm-management-config-configLoader-ConfigLoader-get_config_path"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.get\_config\_path

```python
def get_config_path(self, *paths: str) -> Path:
```

获取配置文件路径（通用方法）

根据传入的路径组件，构建 config 目录下的完整文件路径。
该方法不检查文件是否存在，只负责路径构建。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: get\_config\_path\('display', 'config\.yaml'\)
例如: get\_config\_path\('detector', 'gpu', 'nvidia\.yaml'\)

**Returns:**

- `Path`: 配置文件完整路径
<a name="magicm-management-config-configLoader-ConfigLoader-get_project_config_path"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.get\_project\_config\_path

```python
def get_project_config_path(self) -> Optional[Path]:
```

获取项目配置文件路径

根据初始化时设置的 module\_name 和 config\_filename，返回项目配置文件的完整路径。
项目配置文件位于项目源码的 config 目录下，是只读的默认配置。

**Returns:**

- `Optional[Path]`: 项目配置文件路径，如果未设置 module\_name 或 config\_filename 则返回 None
<a name="magicm-management-config-configLoader-ConfigLoader-get_user_config_path"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.get\_user\_config\_path

```python
def get_user_config_path(self) -> Optional[Path]:
```

获取用户配置文件路径

用户配置文件存储在用户配置目录中，用于覆盖项目配置。
不同操作系统的用户配置目录：
- Linux: ~/\.config/magicm/
- macOS: ~/Library/Application Support/magicm/
- Windows: C:\\Users\\\<User\>\\AppData\\Local\\magicm\\

**Returns:**

- `Optional[Path]`: 用户配置文件路径，如果未设置 module\_name 或 config\_filename 则返回 None
<a name="magicm-management-config-configLoader-ConfigLoader-get_current_config_path"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.get\_current\_config\_path

```python
def get_current_config_path(self) -> Optional[Path]:
```

获取当前使用的配置文件路径

返回最近一次 load\_merged\(\) 实际加载的配置文件路径。
可能是项目配置文件，也可能是用户配置文件（如果存在）。

**Returns:**

- `Optional[Path]`: 当前使用的配置文件路径，未加载时返回 None
<a name="magicm-management-config-configLoader-ConfigLoader-is_using_user_config"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.is\_using\_user\_config

```python
def is_using_user_config(self) -> bool:
```

是否正在使用用户配置

检查最近一次 load\_merged\(\) 是否使用了用户配置覆盖项目配置。

**Returns:**

- `bool`: 使用用户配置返回 True，否则返回 False
<a name="magicm-management-config-configLoader-ConfigLoader-load"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.load

```python
def load(self, *paths: str) -> Dict[str, Any]:
```

加载 YAML 配置文件（直接加载，不合并）

直接从指定路径加载配置文件，不进行用户配置合并。
适用于不需要用户自定义配置的场景。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: load\('display', 'config\.yaml'\)
例如: load\('detector', 'gpu', 'nvidia\.yaml'\)

**Returns:**

- `Dict[str, Any]`: 解析后的配置字典，文件为空时返回空字典

**Raises:**

- **FileNotFoundError**: 配置文件不存在时抛出
<a name="magicm-management-config-configLoader-ConfigLoader-load_all_from_directory"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.load\_all\_from\_directory

```python
def load_all_from_directory(self, *paths: str) -> Dict[str, Dict[str, Any]]:
```

加载指定目录下的所有 YAML 配置文件

从指定目录加载所有 \.yaml 和 \.yml 文件，返回以文件名（不含扩展名）为键的配置字典。

**Parameters:**

- ***paths**: config 目录下的路径\(相对于config\)

**Returns:**

- `Dict[str, Dict[str, Any]]`: 配置字典，格式为 \{文件名: 配置内容\}

**Raises:**

- **FileNotFoundError**: 目录不存在时抛出
<a name="magicm-management-config-configLoader-ConfigLoader-load_merged"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.load\_merged

```python
def load_merged(self) -> Dict[str, Any]:
```

加载合并后的配置（项目配置 \+ 用户配置）

加载项目配置，如果用户配置存在，则用用户配置覆盖项目配置。
用户配置的优先级高于项目配置，可以实现配置的自定义。

配置合并规则：
- 简单类型：用户配置直接覆盖项目配置
- 字典类型：递归合并，用户配置的键值对覆盖项目配置的同名键
- 列表类型：用户配置完全替换项目配置（不合并列表元素）

**Returns:**

- `Dict[str, Any]`: 合并后的配置字典

**Raises:**

- **ValueError**: 未设置 module\_name 或 config\_filename 时抛出
- **FileNotFoundError**: 项目配置文件不存在时抛出
<a name="magicm-management-config-configLoader-ConfigLoader-exists"></a>
#### 🅵 magicm\.management\.config\.configLoader\.ConfigLoader\.exists

```python
def exists(self, *paths: str) -> bool:
```

检查配置文件是否存在

判断指定路径的配置文件是否存在于文件系统中。

**Parameters:**

- ***paths**: config 目录下的路径组件

**Returns:**

- `bool`: 配置文件存在返回 True，否则返回 False
<a name="magicm-management-config-configManager"></a>
## 🅼 magicm\.management\.config\.configManager

配置管理器 - 纯代理模块

该模块提供统一的配置管理入口，通过代理模式将具体功能委托给专门的组件：
- ConfigPathManager: 路径管理
- ConfigLoader: 配置加载
- ConfigReader: 配置读取
- ConfigWriter: 配置写入

使用示例:
    from magicm\.management\.config import ConfigManager
    
    cm = ConfigManager\(\)
    
    \# 获取配置文件路径
    path = cm\.get\_config\_path\('display', 'config\.yaml'\)
    
    \# 加载配置
    config = cm\.load\('display', 'config\.yaml'\)
    
    \# 读取嵌套配置
    value = cm\.get\(config, 'gpu\_ratings\.nuclear', default=\[\]\)
    
    \# 修改配置
    cm\.set\(config, 'timeout', 30\)
    cm\.save\(config, path\)

- **Classes:**
  - 🅲 [ConfigManager](#magicm-management-config-configManager-ConfigManager)

### Classes

<a name="magicm-management-config-configManager-ConfigManager"></a>
### 🅲 magicm\.management\.config\.configManager\.ConfigManager

```python
class ConfigManager:
```

配置管理器 - 纯代理类

该类不包含任何业务逻辑，仅作为统一门面，将所有方法调用委托给专门的组件。
这样设计的好处是：
1\. 统一入口：调用方只需知道 ConfigManager
2\. 职责单一：每个组件只负责自己的功能
3\. 易于扩展：添加新功能只需添加新的代理方法

组件职责：
- ConfigPathManager: 项目 config 目录下的路径管理
- ConfigLoader: YAML 配置文件加载
- ConfigReader: 配置项读取（支持嵌套键）
- ConfigWriter: 配置项写入和保存

**Functions:**

<a name="magicm-management-config-configManager-ConfigManager-__init__"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.\_\_init\_\_

```python
def __init__(self):
```

初始化配置管理器

创建四个专门组件的实例，用于处理不同的配置管理任务。
<a name="magicm-management-config-configManager-ConfigManager-get_config_path"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.get\_config\_path

```python
def get_config_path(self, *paths: str) -> Path:
```

获取配置文件路径

代理 ConfigPathManager\.get\_path\(\) 方法。
根据传入的路径组件，构建 config 目录下的完整文件路径。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: get\_config\_path\('display', 'config\.yaml'\)
例如: get\_config\_path\('detector', 'gpu', 'nvidia\.yaml'\)

**Returns:**

- `Path`: 完整的配置文件路径
<a name="magicm-management-config-configManager-ConfigManager-config_exists"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.config\_exists

```python
def config_exists(self, *paths: str) -> bool:
```

检查配置文件是否存在

代理 ConfigPathManager\.exists\(\) 方法。

**Parameters:**

- ***paths**: config 目录下的路径组件

**Returns:**

- `bool`: 配置文件存在返回 True，否则返回 False
<a name="magicm-management-config-configManager-ConfigManager-load"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.load

```python
def load(self, *paths: str) -> Dict[str, Any]:
```

加载 YAML 配置文件

代理 ConfigLoader\.load\(\) 方法。
从项目 config 目录下加载指定的 YAML 配置文件。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: load\('display', 'config\.yaml'\)
例如: load\('detector', 'gpu', 'nvidia\.yaml'\)

**Returns:**

- `Dict[str, Any]`: 解析后的配置字典，文件为空时返回空字典

**Raises:**

- **FileNotFoundError**: 配置文件不存在时抛出
<a name="magicm-management-config-configManager-ConfigManager-load_all_from_directory"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.load\_all\_from\_directory

```python
def load_all_from_directory(self, *paths: str) -> Dict[str, Dict[str, Any]]:
```

加载指定目录下的所有 YAML 配置文件

从指定目录加载所有 \.yaml 和 \.yml 文件，返回以文件名（不含扩展名）为键的配置字典。

**Parameters:**

- ***paths**: config 目录下的路径\(相对于config\)

**Returns:**

- `Dict[str, Dict[str, Any]]`: 配置字典，格式为 \{文件名: 配置内容\}

**Raises:**

- **FileNotFoundError**: 目录不存在时抛出
<a name="magicm-management-config-configManager-ConfigManager-load_merged"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.load\_merged

```python
def load_merged(self) -> Dict[str, Any]:
```

加载合并后的配置（项目配置 \+ 用户配置）

代理 ConfigLoader\.load\_merged\(\) 方法。
先加载项目配置，再用用户配置覆盖，实现配置的自定义。

注意：此方法使用 ConfigManager 初始化时指定的模块名和配置文件名，
因此调用前需要先创建 ConfigManager 实例时传入相应参数。

**Returns:**

- `Dict[str, Any]`: 合并后的配置字典
<a name="magicm-management-config-configManager-ConfigManager-get"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.get

```python
def get(self, config: dict, key: str, default: Any = None) -> Any:
```

从配置字典中获取指定键的值

代理 ConfigReader\.get\(\) 方法。
支持点号分隔的嵌套键，如 'gpu\_ratings\.nuclear'。

**Parameters:**

- **config**: 配置字典
- **key**: 配置键名，支持点号分隔的嵌套路径
- **default**: 键不存在时返回的默认值

**Returns:**

- `Any`: 配置值，键不存在时返回 default
<a name="magicm-management-config-configManager-ConfigManager-get_path"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.get\_path

```python
def get_path(self, config: dict, path: str, default: Any = None) -> Any:
```

从配置字典中获取指定路径的值（别名方法）

代理 ConfigReader\.get\_path\(\) 方法。
与 get\(\) 方法功能相同，提供更语义化的方法名。

**Parameters:**

- **config**: 配置字典
- **path**: 点号分隔的嵌套路径
- **default**: 路径不存在时返回的默认值

**Returns:**

- `Any`: 配置值
<a name="magicm-management-config-configManager-ConfigManager-set"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.set

```python
def set(self, config: dict, key: str, value: Any) -> None:
```

设置配置字典中指定键的值

代理 ConfigWriter\.set\(\) 方法。
直接修改传入的配置字典，不自动保存到文件。

**Parameters:**

- **config**: 配置字典（会被直接修改）
- **key**: 配置键名
- **value**: 要设置的值
<a name="magicm-management-config-configManager-ConfigManager-set_path"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.set\_path

```python
def set_path(self, config: dict, path: str, value: Any) -> None:
```

设置配置字典中指定路径的值

代理 ConfigWriter\.set\_path\(\) 方法。
支持点号分隔的嵌套路径，自动创建不存在的中间键。

**Parameters:**

- **config**: 配置字典（会被直接修改）
- **path**: 点号分隔的嵌套路径，如 'a\.b\.c'
- **value**: 要设置的值
<a name="magicm-management-config-configManager-ConfigManager-save"></a>
#### 🅵 magicm\.management\.config\.configManager\.ConfigManager\.save

```python
def save(self, config: dict, path: str) -> bool:
```

保存配置字典到 YAML 文件

代理 ConfigWriter\.save\(\) 方法。
将配置字典以 YAML 格式写入指定文件。

**Parameters:**

- **config**: 配置字典
- **path**: 目标文件路径

**Returns:**

- `bool`: 保存成功返回 True，失败返回 False
<a name="magicm-management-config-configPathManager"></a>
## 🅼 magicm\.management\.config\.configPathManager

配置路径管理器 - 项目配置目录路径管理模块

该模块提供项目 config 目录的路径管理功能，自动适配开发环境和打包环境。
支持开发环境（源码运行）和 PyInstaller 打包环境（onefile 模式）。

核心功能：
- 自动查找项目根目录
- 管理 config 目录下的文件路径
- 支持开发环境和打包环境的无缝切换

使用示例:
    from magicm\.management\.config import ConfigPathManager
    
    path\_mgr = ConfigPathManager\(\)
    
    \# 获取配置文件路径
    config\_path = path\_mgr\.get\_path\('display', 'config\.yaml'\)
    
    \# 检查配置文件是否存在
    if path\_mgr\.exists\('display', 'config\.yaml'\):
        with open\(config\_path, 'r'\) as f:
            config = yaml\.safe\_load\(f\)

- **Classes:**
  - 🅲 [ConfigPathManager](#magicm-management-config-configPathManager-ConfigPathManager)

### Classes

<a name="magicm-management-config-configPathManager-ConfigPathManager"></a>
### 🅲 magicm\.management\.config\.configPathManager\.ConfigPathManager

```python
class ConfigPathManager:
```

稳定的配置路径管理器，支持开发环境和 PyInstaller 打包环境

该类的核心职责：
1\. 自动识别当前运行环境（开发环境 vs 打包环境）
2\. 返回正确的项目 config 目录路径
3\. 提供便捷的路径构建和检查方法

环境识别逻辑：
- 打包环境：通过 sys\.frozen 和 sys\.\_MEIPASS 识别，配置位于临时解压目录
- 开发环境：向上查找同时包含 config 和 src 目录的父目录作为项目根目录

使用场景：
- 开发时：从项目源码的 config 目录读取配置
- 打包后：从 PyInstaller 解压的临时目录读取配置
- 测试时：可手动指定 project\_root 用于单元测试

**Attributes:**

- **_project_root** (`Optional[Path]`): 项目根目录缓存
- **_config_dir** (`Optional[Path]`): config 目录缓存

**Functions:**

<a name="magicm-management-config-configPathManager-ConfigPathManager-__init__"></a>
#### 🅵 magicm\.management\.config\.configPathManager\.ConfigPathManager\.\_\_init\_\_

```python
def __init__(self, project_root: Optional[Path] = None):
```

初始化配置路径管理器

**Parameters:**

- **project_root**: 可选的项目根目录路径。
如果提供，将直接使用该路径作为项目根目录，
跳过自动查找逻辑。主要用于单元测试。
<a name="magicm-management-config-configPathManager-ConfigPathManager-config_dir"></a>
#### 🅵 magicm\.management\.config\.configPathManager\.ConfigPathManager\.config\_dir

```python
def config_dir(self) -> Path:
```

获取 config 目录路径

该属性使用延迟加载和缓存机制，首次访问时计算并缓存结果。

**Returns:**

- `Path`: config 目录的绝对路径

**Raises:**

- **RuntimeError**: config 目录不存在时抛出
<a name="magicm-management-config-configPathManager-ConfigPathManager-get_path"></a>
#### 🅵 magicm\.management\.config\.configPathManager\.ConfigPathManager\.get\_path

```python
def get_path(self, *paths: str) -> Path:
```

获取 config 目录下的文件路径

将传入的路径组件与 config 目录拼接，返回完整的文件路径。
该方法不检查文件是否存在，只负责路径构建。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: get\_path\('display', 'config\.yaml'\)
例如: get\_path\('detector', 'gpu', 'nvidia\.yaml'\)
例如: get\_path\('settings\.json'\)

**Returns:**

- `Path`: config 目录下的完整文件路径
<a name="magicm-management-config-configPathManager-ConfigPathManager-exists"></a>
#### 🅵 magicm\.management\.config\.configPathManager\.ConfigPathManager\.exists

```python
def exists(self, *paths: str) -> bool:
```

检查 config 目录下的文件是否存在

该方法在 get\_path\(\) 的基础上增加了存在性检查。
不会抛出异常，仅返回布尔值。

**Parameters:**

- ***paths**: config 目录下的路径组件
例如: exists\('display', 'config\.yaml'\)
例如: exists\('detector', 'gpu', 'nvidia\.yaml'\)

**Returns:**

- `bool`: 文件存在返回 True，否则返回 False
<a name="magicm-management-config-configReader"></a>
## 🅼 magicm\.management\.config\.configReader

配置读取器 - 只读配置访问模块

该模块提供只读的配置访问功能，支持从项目配置和用户配置合并后的结果中读取配置。
配置读取器支持延迟加载，在首次使用时才加载配置。

核心功能：
- 横向获取：直接通过键名获取配置值
- 纵向获取：通过点号分隔的路径获取嵌套配置值
- 批量获取：同时获取多个配置项
- 配置重载：重新从文件加载配置
- 来源追踪：获取当前配置的来源信息

使用示例:
    from magicm\.management\.config import ConfigReader
    
    \# 无参构造，调用时传入模块名
    reader = ConfigReader\(\)
    
    \# 横向获取
    timeout = reader\.get\('display', 'timeout', default=30\)
    
    \# 纵向获取嵌套配置
    nuclear = reader\.get\_path\('display', 'gpu\_ratings\.nuclear', default=\[\]\)
    
    \# 批量获取
    ratings = reader\.get\_multi\('display', \['gpu\_ratings\.nuclear', 'gpu\_ratings\.flagship'\]\)
    
    \# 查看配置来源
    source = reader\.get\_config\_source\('display'\)
    print\(f"当前使用: \{source\['current\_config'\]\}"\)

- **Classes:**
  - 🅲 [ConfigReader](#magicm-management-config-configReader-ConfigReader)

### Classes

<a name="magicm-management-config-configReader-ConfigReader"></a>
### 🅲 magicm\.management\.config\.configReader\.ConfigReader

```python
class ConfigReader:
```

配置读取器 - 只读配置访问

该类提供只读的配置访问接口，支持延迟加载配置。
配置在首次访问时从文件加载并合并（项目配置 \+ 用户配置），
后续读取操作直接使用缓存，性能高效。

特点：
- 只读：不提供任何写入或修改配置的方法
- 延迟加载：首次使用时才加载配置
- 自动合并：自动合并项目配置和用户配置
- 支持嵌套：通过点号分隔的路径访问嵌套配置
- 来源追踪：可以查询配置来自项目文件还是用户文件

**Attributes:**

- **_loaders** (`Dict[str, ConfigLoader]`): 各模块的配置加载器缓存
- **_configs** (`Dict[str, Dict[str, Any]]`): 各模块的配置字典缓存

**Functions:**

<a name="magicm-management-config-configReader-ConfigReader-__init__"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.\_\_init\_\_

```python
def __init__(self):
```

初始化配置读取器

无参构造，配置在首次使用时才加载。
<a name="magicm-management-config-configReader-ConfigReader-get"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.get

```python
def get(self, module_name: str, key: str, default: Any = None, config_filename: str = 'config.yaml') -> Any:
```

横向获取配置项

直接从配置字典的顶层获取指定键的值。
适用于获取非嵌套的顶级配置项。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **key**: 配置键名（顶层键）
- **default**: 键不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Any`: 配置值，键不存在时返回 default
<a name="magicm-management-config-configReader-ConfigReader-get_path"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.get\_path

```python
def get_path(self, module_name: str, path: str, default: Any = None, config_filename: str = 'config.yaml') -> Any:
```

纵向获取配置项（点分隔路径）

通过点号分隔的路径字符串访问嵌套配置。
例如 'gpu\_ratings\.nuclear' 会访问 config\['gpu\_ratings'\]\['nuclear'\]。

路径解析规则：
- 每个路径段作为字典的键
- 如果中间任一键不存在或对应的值不是字典，返回 default
- 支持任意深度的嵌套

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **path**: 点号分隔的嵌套路径，如 'gpu\_ratings\.nuclear'
- **default**: 路径不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Any`: 路径对应的配置值，路径不存在时返回 default
<a name="magicm-management-config-configReader-ConfigReader-get_multi"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.get\_multi

```python
def get_multi(self, module_name: str, keys: list, default: Any = None, config_filename: str = 'config.yaml') -> Dict[str, Any]:
```

批量获取多个配置项

同时获取多个配置项，返回包含键值对的字典。
自动识别键名是否包含点号，分别调用 get\(\) 或 get\_path\(\)。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **keys**: 配置键名列表，支持点号分隔的路径
- **default**: 键不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Dict[str, Any]`: 键名到配置值的映射字典
<a name="magicm-management-config-configReader-ConfigReader-reload"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.reload

```python
def reload(self, module_name: str, config_filename: str = 'config.yaml'):
```

重新加载配置

从文件系统重新加载配置（项目配置 \+ 用户配置合并），
更新内存中的配置数据。适用于配置文件在运行时被外部修改的场景。

注意：重新加载会丢失所有未保存的内存修改（如果存在）。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configReader-ConfigReader-reload_all"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.reload\_all

```python
def reload_all(self):
```

重新加载所有已加载的配置

清空所有缓存，下次访问时会重新从文件加载。
<a name="magicm-management-config-configReader-ConfigReader-get_config_source"></a>
#### 🅵 magicm\.management\.config\.configReader\.ConfigReader\.get\_config\_source

```python
def get_config_source(self, module_name: str, config_filename: str = 'config.yaml') -> Dict[str, str]:
```

获取配置来源信息

返回当前配置的来源详情，包括项目配置文件路径、用户配置文件路径、
当前使用的配置文件路径以及是否使用了用户配置。

此方法可用于调试和诊断配置加载问题。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Dict[str, str]`: 包含以下键的字典：
- 'project\_config': 项目配置文件路径
- 'user\_config': 用户配置文件路径
- 'current\_config': 当前使用的配置文件路径
- 'using\_user\_config': 是否使用了用户配置（字符串 'True'/'False'）
<a name="magicm-management-config-configWriter"></a>
## 🅼 magicm\.management\.config\.configWriter

配置写入器 - 配置修改和保存模块

该模块提供配置的读写功能，支持修改配置并将修改保存到用户配置文件中。
配置写入器支持延迟加载，在首次使用时才加载配置。

核心功能：
- 读取配置：支持读取配置项
- 修改配置：支持横向设置、纵向设置（嵌套路径）、批量更新
- 保存配置：将修改保存到用户配置文件
- 配置管理：支持重载配置、切换配置来源

使用示例:
    from magicm\.management\.config import ConfigWriter
    
    \# 无参构造，调用时传入模块名
    writer = ConfigWriter\(\)
    
    \# 修改配置
    writer\.set\('display', 'timeout', 30\)
    writer\.set\_path\('display', 'gpu\_ratings\.nuclear', \['RTX 5090', 'RX 8900'\]\)
    
    \# 批量更新
    writer\.update\('display', \{
        'version': '2\.0',
        'author': 'magicm'
    \}\)
    
    \# 保存到用户配置
    writer\.save\('display'\)
    
    \# 重新加载（从文件重新读取）
    writer\.reload\('display'\)

- **Classes:**
  - 🅲 [ConfigWriter](#magicm-management-config-configWriter-ConfigWriter)

### Classes

<a name="magicm-management-config-configWriter-ConfigWriter"></a>
### 🅲 magicm\.management\.config\.configWriter\.ConfigWriter

```python
class ConfigWriter:
```

配置写入器 - 可读写的配置管理类

该类提供完整的配置读写功能，所有修改默认保存在用户配置目录中，
不会影响项目默认配置。支持横向和纵向（嵌套）的配置操作。
支持延迟加载，在首次使用时才加载配置。

配置存储策略：
- 项目配置：存储在项目源码 config 目录，只读，作为默认配置
- 用户配置：存储在用户配置目录（如 ~/\.config/magicm/），可写，
  用户修改会保存到这里，优先级高于项目配置

特点：
- 延迟加载：首次使用时才加载配置
- 写入能力：支持修改和添加配置项
- 嵌套操作：支持点号分隔的路径访问嵌套配置
- 安全保存：修改保存到用户配置，不影响项目配置

**Attributes:**

- **_loaders** (`Dict[str, ConfigLoader]`): 各模块的配置加载器缓存
- **_configs** (`Dict[str, Dict[str, Any]]`): 各模块的配置字典缓存

**Functions:**

<a name="magicm-management-config-configWriter-ConfigWriter-__init__"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.\_\_init\_\_

```python
def __init__(self):
```

初始化配置写入器

无参构造，配置在首次使用时才加载。
<a name="magicm-management-config-configWriter-ConfigWriter-get"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.get

```python
def get(self, module_name: str, key: str, default: Any = None, config_filename: str = 'config.yaml') -> Any:
```

横向获取配置项

直接从配置字典的顶层获取指定键的值。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **key**: 配置键名（顶层键）
- **default**: 键不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Any`: 配置值，键不存在时返回 default
<a name="magicm-management-config-configWriter-ConfigWriter-get_path"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.get\_path

```python
def get_path(self, module_name: str, path: str, default: Any = None, config_filename: str = 'config.yaml') -> Any:
```

纵向获取配置项（点分隔路径）

通过点号分隔的路径字符串访问嵌套配置。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **path**: 点号分隔的嵌套路径，如 'gpu\_ratings\.nuclear'
- **default**: 路径不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Any`: 路径对应的配置值，路径不存在时返回 default
<a name="magicm-management-config-configWriter-ConfigWriter-get_multi"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.get\_multi

```python
def get_multi(self, module_name: str, keys: list, default: Any = None, config_filename: str = 'config.yaml') -> Dict[str, Any]:
```

批量获取多个配置项

同时获取多个配置项，返回包含键值对的字典。
自动识别键名是否包含点号，分别调用 get\(\) 或 get\_path\(\)。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **keys**: 配置键名列表，支持点号分隔的路径
- **default**: 键不存在时返回的默认值
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Dict[str, Any]`: 键名到配置值的映射字典
<a name="magicm-management-config-configWriter-ConfigWriter-set"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.set

```python
def set(self, module_name: str, key: str, value: Any, config_filename: str = 'config.yaml'):
```

横向设置配置项

直接设置配置字典顶层的键值对。
修改后需要调用 save\(\) 方法才能持久化到文件。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **key**: 配置键名（顶层键）
- **value**: 要设置的值
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-set_path"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.set\_path

```python
def set_path(self, module_name: str, path: str, value: Any, config_filename: str = 'config.yaml'):
```

纵向设置嵌套配置项

通过点号分隔的路径设置嵌套配置的值。
如果路径中的中间键不存在，会自动创建。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **path**: 点号分隔的嵌套路径，如 'gpu\_ratings\.nuclear'
- **value**: 要设置的值
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-update"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.update

```python
def update(self, module_name: str, updates: Dict[str, Any], config_filename: str = 'config.yaml'):
```

批量更新配置

使用字典批量更新多个顶层配置项。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **updates**: 包含键值对的字典，键为顶层配置键名
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-update_path"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.update\_path

```python
def update_path(self, module_name: str, updates: Dict[str, Any], config_filename: str = 'config.yaml'):
```

批量更新嵌套配置

使用字典批量更新多个嵌套配置项，键名支持点号分隔的路径。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **updates**: 包含路径-值对的字典
键为点号分隔的路径，值为要设置的内容
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-save"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.save

```python
def save(self, module_name: str, config_filename: str = 'config.yaml') -> bool:
```

保存配置到用户文件

将当前配置保存到用户配置目录，不会影响项目默认配置。
用户配置优先级高于项目配置，下次加载时会自动合并。

用户配置文件位置：
- Linux: ~/\.config/magicm/\{module\_name\}/config\.yaml
- macOS: ~/Library/Application Support/magicm/\{module\_name\}/config\.yaml
- Windows: C:\\Users\\\<User\>\\AppData\\Local\\magicm\\\{module\_name\}\\config\.yaml

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `bool`: 保存成功返回 True，失败返回 False
<a name="magicm-management-config-configWriter-ConfigWriter-save_as_project"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.save\_as\_project

```python
def save_as_project(self, module_name: str, config_filename: str = 'config.yaml') -> bool:
```

保存配置到项目文件（需要权限）

将当前配置保存到项目源码的 config 目录，覆盖项目默认配置。
通常需要管理员权限，且不建议在生产环境使用。

警告：
- 需要项目目录的写入权限
- 会影响所有用户的默认配置
- 建议仅在开发或调试时使用

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `bool`: 保存成功返回 True，失败返回 False
<a name="magicm-management-config-configWriter-ConfigWriter-reload"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.reload

```python
def reload(self, module_name: str, config_filename: str = 'config.yaml'):
```

重新加载配置

从文件系统重新加载配置（项目配置 \+ 用户配置合并），
更新内存中的配置数据。会丢失未保存的修改。

使用场景：
- 外部程序修改了配置文件
- 需要恢复到文件中的配置状态
- 切换配置来源后

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-reload_all"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.reload\_all

```python
def reload_all(self):
```

重新加载所有已加载的配置

清空所有缓存，下次访问时会重新从文件加载。
<a name="magicm-management-config-configWriter-ConfigWriter-switch_to_user_config"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.switch\_to\_user\_config

```python
def switch_to_user_config(self, module_name: str, config_filename: str = 'config.yaml'):
```

切换到用户配置

重新加载配置，确保优先使用用户配置。
如果用户配置存在，会覆盖项目配置中的相同项。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-switch_to_project_config"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.switch\_to\_project\_config

```python
def switch_to_project_config(self, module_name: str, config_filename: str = 'config.yaml'):
```

切换到项目配置

重新加载配置，只使用项目配置，忽略用户配置。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'
<a name="magicm-management-config-configWriter-ConfigWriter-get_config_source"></a>
#### 🅵 magicm\.management\.config\.configWriter\.ConfigWriter\.get\_config\_source

```python
def get_config_source(self, module_name: str, config_filename: str = 'config.yaml') -> Dict[str, str]:
```

获取配置来源信息

返回当前配置的来源详情，包括项目配置文件路径、用户配置文件路径、
当前使用的配置文件路径以及是否使用了用户配置。

此方法可用于调试和诊断配置加载问题。

**Parameters:**

- **module_name**: 模块名称，如 'display', 'detector'
- **config_filename**: 配置文件名，默认为 'config\.yaml'

**Returns:**

- `Dict[str, str]`: 包含以下键的字典：
- 'project\_config': 项目配置文件路径
- 'user\_config': 用户配置文件路径
- 'current\_config': 当前使用的配置文件路径
- 'using\_user\_config': 是否使用了用户配置（字符串 'True'/'False'）
<a name="magicm-utils"></a>
## 🅼 magicm\.utils
<a name="magicm-utils-util"></a>
## 🅼 magicm\.utils\.util

通用命令执行模块

提供系统命令执行的通用功能，包括超时控制和错误处理。
可用于各种需要调用外部命令的场景。

- **Functions:**
  - 🅵 [run\_cmd](#magicm-utils-util-run_cmd)
  - 🅵 [log\_result](#magicm-utils-util-log_result)
  - 🅵 [is\_windows](#magicm-utils-util-is_windows)
  - 🅵 [is\_linux](#magicm-utils-util-is_linux)
  - 🅵 [is\_macos](#magicm-utils-util-is_macos)

### Functions

<a name="magicm-utils-util-run_cmd"></a>
### 🅵 magicm\.utils\.util\.run\_cmd

```python
def run_cmd(cmd, timeout = 120):
```

运行系统命令并返回执行结果

该函数通过 subprocess 模块执行指定的 shell 命令，支持超时控制，
并自动捕获标准输出和标准错误输出。命令执行过程中发生的异常会被
捕获并转换为返回码 -1。

**Parameters:**

- **cmd** (`str`): 要执行的 shell 命令字符串
- **timeout** (`int`): 命令执行的超时时间（秒）。默认为 120 秒。

**Returns:**

- `tuple`: \(returncode, stdout, stderr\)
- returncode \(int\): 命令的返回码。成功执行通常返回 0，
  超时或异常时返回 -1
- stdout \(str\): 命令的标准输出内容，已去除首尾空白字符。
  若无输出则为空字符串
- stderr \(str\): 命令的标准错误输出内容，已去除首尾空白字符。
  若无输出或发生异常则为空字符串或异常信息
<a name="magicm-utils-util-log_result"></a>
### 🅵 magicm\.utils\.util\.log\_result

```python
def log_result(returncode, stdout, stderr, cmd_name = ''):
```

格式化输出命令执行结果（示例辅助函数）

**Parameters:**

- **returncode** (`int`): 命令返回码
- **stdout** (`str`): 标准输出
- **stderr** (`str`): 标准错误
- **cmd_name** (`str`): 命令名称（用于日志标识）

**Returns:**

- `str`: 格式化后的日志信息
<a name="magicm-utils-util-is_windows"></a>
### 🅵 magicm\.utils\.util\.is\_windows

```python
def is_windows():
```

判断当前操作系统是否为 Windows

**Returns:**

- `bool`: 如果是 Windows 系统返回 True，否则返回 False
<a name="magicm-utils-util-is_linux"></a>
### 🅵 magicm\.utils\.util\.is\_linux

```python
def is_linux():
```

判断当前操作系统是否为 Linux

**Returns:**

- `bool`: 如果是 Linux 系统返回 True，否则返回 False
<a name="magicm-utils-util-is_macos"></a>
### 🅵 magicm\.utils\.util\.is\_macos

```python
def is_macos():
```

判断当前操作系统是否为 macOS

**Returns:**

- `bool`: 如果是 macOS 系统返回 True，否则返回 False
