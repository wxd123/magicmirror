# `hardware`

## Table of Contents

- 🅼 [hardware](#hardware)
- 🅼 [hardware\.cpu](#hardware-cpu)
- 🅼 [hardware\.cpu\.cpu\_detecter](#hardware-cpu-cpu_detecter)
- 🅼 [hardware\.cpu\.cpu\_model](#hardware-cpu-cpu_model)
- 🅼 [hardware\.cpu\.linux\_detecter](#hardware-cpu-linux_detecter)
- 🅼 [hardware\.cpu\.mac\_detecter](#hardware-cpu-mac_detecter)
- 🅼 [hardware\.cpu\.win\_detecter](#hardware-cpu-win_detecter)
- 🅼 [hardware\.gpu](#hardware-gpu)
- 🅼 [hardware\.gpu\.amd](#hardware-gpu-amd)
- 🅼 [hardware\.gpu\.commands](#hardware-gpu-commands)
- 🅼 [hardware\.gpu\.commands\.amd\_command](#hardware-gpu-commands-amd_command)
- 🅼 [hardware\.gpu\.commands\.apple\_command](#hardware-gpu-commands-apple_command)
- 🅼 [hardware\.gpu\.commands\.huawei\_command](#hardware-gpu-commands-huawei_command)
- 🅼 [hardware\.gpu\.commands\.intel\_command](#hardware-gpu-commands-intel_command)
- 🅼 [hardware\.gpu\.commands\.nvidia\_command](#hardware-gpu-commands-nvidia_command)
- 🅼 [hardware\.gpu\.commands\.qualcomm\_command](#hardware-gpu-commands-qualcomm_command)
- 🅼 [hardware\.gpu\.core](#hardware-gpu-core)
- 🅼 [hardware\.gpu\.core\.base](#hardware-gpu-core-base)
- 🅼 [hardware\.gpu\.core\.command\_executor](#hardware-gpu-core-command_executor)
- 🅼 [hardware\.gpu\.core\.factory](#hardware-gpu-core-factory)
- 🅼 [hardware\.gpu\.gpu\_detecter](#hardware-gpu-gpu_detecter)
- 🅼 [hardware\.gpu\.vendor](#hardware-gpu-vendor)
- 🅼 [hardware\.gpu\.vendor\.amd](#hardware-gpu-vendor-amd)
- 🅼 [hardware\.gpu\.vendor\.huawei](#hardware-gpu-vendor-huawei)
- 🅼 [hardware\.gpu\.vendor\.intel](#hardware-gpu-vendor-intel)
- 🅼 [hardware\.gpu\.vendor\.nvidia](#hardware-gpu-vendor-nvidia)
- 🅼 [hardware\.gpu\.vendor\.utils](#hardware-gpu-vendor-utils)
- 🅼 [hardware\.mem](#hardware-mem)
- 🅼 [hardware\.mem\.mem\_detecter](#hardware-mem-mem_detecter)

<a name="hardware"></a>
## 🅼 hardware
<a name="hardware-cpu"></a>
## 🅼 hardware\.cpu
<a name="hardware-cpu-cpu_detecter"></a>
## 🅼 hardware\.cpu\.cpu\_detecter

- **Functions:**
  - 🅵 [cpu\_detected](#hardware-cpu-cpu_detecter-cpu_detected)
  - 🅵 [get\_cpu\_summary](#hardware-cpu-cpu_detecter-get_cpu_summary)

### Functions

<a name="hardware-cpu-cpu_detecter-cpu_detected"></a>
### 🅵 hardware\.cpu\.cpu\_detecter\.cpu\_detected

```python
def cpu_detected():
```

检测CPU信息 - 增强版
<a name="hardware-cpu-cpu_detecter-get_cpu_summary"></a>
### 🅵 hardware\.cpu\.cpu\_detecter\.get\_cpu\_summary

```python
def get_cpu_summary():
```

获取CPU摘要信息
<a name="hardware-cpu-cpu_model"></a>
## 🅼 hardware\.cpu\.cpu\_model

- **Functions:**
  - 🅵 [cpu\_model](#hardware-cpu-cpu_model-cpu_model)

### Functions

<a name="hardware-cpu-cpu_model-cpu_model"></a>
### 🅵 hardware\.cpu\.cpu\_model\.cpu\_model

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
<a name="hardware-cpu-linux_detecter"></a>
## 🅼 hardware\.cpu\.linux\_detecter

- **Functions:**
  - 🅵 [detecter](#hardware-cpu-linux_detecter-detecter)

### Functions

<a name="hardware-cpu-linux_detecter-detecter"></a>
### 🅵 hardware\.cpu\.linux\_detecter\.detecter

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
<a name="hardware-cpu-mac_detecter"></a>
## 🅼 hardware\.cpu\.mac\_detecter

- **Functions:**
  - 🅵 [detect](#hardware-cpu-mac_detecter-detect)

### Functions

<a name="hardware-cpu-mac_detecter-detect"></a>
### 🅵 hardware\.cpu\.mac\_detecter\.detect

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
<a name="hardware-cpu-win_detecter"></a>
## 🅼 hardware\.cpu\.win\_detecter

- **Functions:**
  - 🅵 [detecter](#hardware-cpu-win_detecter-detecter)

### Functions

<a name="hardware-cpu-win_detecter-detecter"></a>
### 🅵 hardware\.cpu\.win\_detecter\.detecter

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
<a name="hardware-gpu"></a>
## 🅼 hardware\.gpu
<a name="hardware-gpu-amd"></a>
## 🅼 hardware\.gpu\.amd
<a name="hardware-gpu-commands"></a>
## 🅼 hardware\.gpu\.commands

- **[Exports](#hardware-gpu-commands-exports)**

<a name="hardware-gpu-commands-exports"></a>
### Exports

- 🅼 [`NVIDIACommand`](#hardware-gpu-commands-NVIDIACommand)
- 🅼 [`AMDCommand`](#hardware-gpu-commands-AMDCommand)
- 🅼 [`IntelCommand`](#hardware-gpu-commands-IntelCommand)
- 🅼 [`HuaweiCommand`](#hardware-gpu-commands-HuaweiCommand)
<a name="hardware-gpu-commands-amd_command"></a>
## 🅼 hardware\.gpu\.commands\.amd\_command

- **Classes:**
  - 🅲 [AMDCommand](#hardware-gpu-commands-amd_command-AMDCommand)

### Classes

<a name="hardware-gpu-commands-amd_command-AMDCommand"></a>
### 🅲 hardware\.gpu\.commands\.amd\_command\.AMDCommand

```python
class AMDCommand(GPUDetectionCommand):
```

AMD GPU检测命令

**Functions:**

<a name="hardware-gpu-commands-amd_command-AMDCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.amd\_command\.AMDCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-amd_command-AMDCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.amd\_command\.AMDCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-amd_command-AMDCommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.amd\_command\.AMDCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行AMD GPU检测
<a name="hardware-gpu-commands-apple_command"></a>
## 🅼 hardware\.gpu\.commands\.apple\_command

- **Classes:**
  - 🅲 [AppleCommand](#hardware-gpu-commands-apple_command-AppleCommand)

### Classes

<a name="hardware-gpu-commands-apple_command-AppleCommand"></a>
### 🅲 hardware\.gpu\.commands\.apple\_command\.AppleCommand

```python
class AppleCommand(GPUDetectionCommand):
```

Apple Silicon GPU检测命令 - 新增厂商示例

**Functions:**

<a name="hardware-gpu-commands-apple_command-AppleCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.apple\_command\.AppleCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-apple_command-AppleCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.apple\_command\.AppleCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-apple_command-AppleCommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.apple\_command\.AppleCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Apple Silicon GPU检测
<a name="hardware-gpu-commands-huawei_command"></a>
## 🅼 hardware\.gpu\.commands\.huawei\_command

- **Classes:**
  - 🅲 [HuaweiCommand](#hardware-gpu-commands-huawei_command-HuaweiCommand)

### Classes

<a name="hardware-gpu-commands-huawei_command-HuaweiCommand"></a>
### 🅲 hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand

```python
class HuaweiCommand(GPUDetectionCommand):
```

华为昇腾GPU检测命令

**Functions:**

<a name="hardware-gpu-commands-huawei_command-HuaweiCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-huawei_command-HuaweiCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-huawei_command-HuaweiCommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.huawei\_command\.HuaweiCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行华为昇腾GPU检测
<a name="hardware-gpu-commands-intel_command"></a>
## 🅼 hardware\.gpu\.commands\.intel\_command

- **Classes:**
  - 🅲 [IntelCommand](#hardware-gpu-commands-intel_command-IntelCommand)

### Classes

<a name="hardware-gpu-commands-intel_command-IntelCommand"></a>
### 🅲 hardware\.gpu\.commands\.intel\_command\.IntelCommand

```python
class IntelCommand(GPUDetectionCommand):
```

Intel GPU检测命令

**Functions:**

<a name="hardware-gpu-commands-intel_command-IntelCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.intel\_command\.IntelCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-intel_command-IntelCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.intel\_command\.IntelCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-intel_command-IntelCommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.intel\_command\.IntelCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行Intel GPU检测
<a name="hardware-gpu-commands-nvidia_command"></a>
## 🅼 hardware\.gpu\.commands\.nvidia\_command

- **Classes:**
  - 🅲 [NVIDIACommand](#hardware-gpu-commands-nvidia_command-NVIDIACommand)

### Classes

<a name="hardware-gpu-commands-nvidia_command-NVIDIACommand"></a>
### 🅲 hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand

```python
class NVIDIACommand(GPUDetectionCommand):
```

NVIDIA GPU检测命令

**Functions:**

<a name="hardware-gpu-commands-nvidia_command-NVIDIACommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-nvidia_command-NVIDIACommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-nvidia_command-NVIDIACommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.nvidia\_command\.NVIDIACommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行NVIDIA GPU检测
<a name="hardware-gpu-commands-qualcomm_command"></a>
## 🅼 hardware\.gpu\.commands\.qualcomm\_command

- **Classes:**
  - 🅲 [QualcommCommand](#hardware-gpu-commands-qualcomm_command-QualcommCommand)

### Classes

<a name="hardware-gpu-commands-qualcomm_command-QualcommCommand"></a>
### 🅲 hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand

```python
class QualcommCommand(GPUDetectionCommand):
```

高通Adreno GPU检测命令 - 新增厂商示例

**Functions:**

<a name="hardware-gpu-commands-qualcomm_command-QualcommCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-commands-qualcomm_command-QualcommCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.get\_priority

```python
def get_priority(self) -> int:
```
<a name="hardware-gpu-commands-qualcomm_command-QualcommCommand-execute"></a>
#### 🅵 hardware\.gpu\.commands\.qualcomm\_command\.QualcommCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行高通Adreno GPU检测
<a name="hardware-gpu-core"></a>
## 🅼 hardware\.gpu\.core
<a name="hardware-gpu-core-base"></a>
## 🅼 hardware\.gpu\.core\.base

- **Classes:**
  - 🅲 [SystemType](#hardware-gpu-core-base-SystemType)
  - 🅲 [GPUVendor](#hardware-gpu-core-base-GPUVendor)
  - 🅲 [GPUType](#hardware-gpu-core-base-GPUType)
  - 🅲 [GPUInfo](#hardware-gpu-core-base-GPUInfo)
  - 🅲 [DetectionResult](#hardware-gpu-core-base-DetectionResult)
  - 🅲 [GPUDetectionCommand](#hardware-gpu-core-base-GPUDetectionCommand)
  - 🅲 [PlatformAdapter](#hardware-gpu-core-base-PlatformAdapter)

### Classes

<a name="hardware-gpu-core-base-SystemType"></a>
### 🅲 hardware\.gpu\.core\.base\.SystemType

```python
class SystemType(Enum):
```

系统类型 - 扩展少
<a name="hardware-gpu-core-base-GPUVendor"></a>
### 🅲 hardware\.gpu\.core\.base\.GPUVendor

```python
class GPUVendor(Enum):
```

GPU厂商 - 扩展多
<a name="hardware-gpu-core-base-GPUType"></a>
### 🅲 hardware\.gpu\.core\.base\.GPUType

```python
class GPUType(Enum):
```

GPU类型
<a name="hardware-gpu-core-base-GPUInfo"></a>
### 🅲 hardware\.gpu\.core\.base\.GPUInfo

```python
class GPUInfo:
```

GPU信息数据类 - 兼容原有API

**Functions:**

<a name="hardware-gpu-core-base-GPUInfo-to_dict"></a>
#### 🅵 hardware\.gpu\.core\.base\.GPUInfo\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="hardware-gpu-core-base-DetectionResult"></a>
### 🅲 hardware\.gpu\.core\.base\.DetectionResult

```python
class DetectionResult:
```

检测结果数据类 - 兼容原有API

**Functions:**

<a name="hardware-gpu-core-base-DetectionResult-main_gpu"></a>
#### 🅵 hardware\.gpu\.core\.base\.DetectionResult\.main\_gpu

```python
def main_gpu(self) -> Optional[GPUInfo]:
```

获取主GPU（优先离散，其次集成）
<a name="hardware-gpu-core-base-DetectionResult-to_dict"></a>
#### 🅵 hardware\.gpu\.core\.base\.DetectionResult\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典 - 兼容原有格式
<a name="hardware-gpu-core-base-GPUDetectionCommand"></a>
### 🅲 hardware\.gpu\.core\.base\.GPUDetectionCommand

```python
class GPUDetectionCommand(ABC):
```

GPU检测命令接口

**Functions:**

<a name="hardware-gpu-core-base-GPUDetectionCommand-execute"></a>
#### 🅵 hardware\.gpu\.core\.base\.GPUDetectionCommand\.execute

```python
def execute(self, context: Dict[str, Any]) -> List[GPUInfo]:
```

执行检测命令
<a name="hardware-gpu-core-base-GPUDetectionCommand-get_vendor"></a>
#### 🅵 hardware\.gpu\.core\.base\.GPUDetectionCommand\.get\_vendor

```python
def get_vendor(self) -> GPUVendor:
```

返回厂商类型
<a name="hardware-gpu-core-base-GPUDetectionCommand-get_priority"></a>
#### 🅵 hardware\.gpu\.core\.base\.GPUDetectionCommand\.get\_priority

```python
def get_priority(self) -> int:
```

优先级（数值越小越先执行）
<a name="hardware-gpu-core-base-PlatformAdapter"></a>
### 🅲 hardware\.gpu\.core\.base\.PlatformAdapter

```python
class PlatformAdapter(ABC):
```

平台适配器接口

**Functions:**

<a name="hardware-gpu-core-base-PlatformAdapter-get_system_type"></a>
#### 🅵 hardware\.gpu\.core\.base\.PlatformAdapter\.get\_system\_type

```python
def get_system_type(self) -> SystemType:
```

获取系统类型
<a name="hardware-gpu-core-base-PlatformAdapter-run_command"></a>
#### 🅵 hardware\.gpu\.core\.base\.PlatformAdapter\.run\_command

```python
def run_command(self, cmd: str) -> tuple:
```

执行命令
<a name="hardware-gpu-core-base-PlatformAdapter-get_gpu_list"></a>
#### 🅵 hardware\.gpu\.core\.base\.PlatformAdapter\.get\_gpu\_list

```python
def get_gpu_list(self) -> List[Dict[str, Any]]:
```

获取GPU原始列表
<a name="hardware-gpu-core-command_executor"></a>
## 🅼 hardware\.gpu\.core\.command\_executor

- **Classes:**
  - 🅲 [CommandRegistry](#hardware-gpu-core-command_executor-CommandRegistry)
  - 🅲 [GPUCommandExecutor](#hardware-gpu-core-command_executor-GPUCommandExecutor)

### Classes

<a name="hardware-gpu-core-command_executor-CommandRegistry"></a>
### 🅲 hardware\.gpu\.core\.command\_executor\.CommandRegistry

```python
class CommandRegistry:
```

命令注册器

**Functions:**

<a name="hardware-gpu-core-command_executor-CommandRegistry-register"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.CommandRegistry\.register

```python
def register(cls, command: GPUDetectionCommand):
```

注册命令
<a name="hardware-gpu-core-command_executor-CommandRegistry-get"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.CommandRegistry\.get

```python
def get(cls, vendor: GPUVendor) -> Optional[GPUDetectionCommand]:
```

获取命令
<a name="hardware-gpu-core-command_executor-CommandRegistry-get_all"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.CommandRegistry\.get\_all

```python
def get_all(cls) -> List[GPUDetectionCommand]:
```

获取所有命令（按优先级排序）
<a name="hardware-gpu-core-command_executor-CommandRegistry-clear"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.CommandRegistry\.clear

```python
def clear(cls):
```

清空所有命令
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor"></a>
### 🅲 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor

```python
class GPUCommandExecutor:
```

GPU命令执行器 - 核心业务逻辑

**Functions:**

<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-__init__"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.\_\_init\_\_

```python
def __init__(self, system: str = None):
```

初始化执行器

**Parameters:**

- **system**: 系统类型 \(linux/windows/macos\)，None表示自动检测
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-detect_all"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU - 返回DetectionResult
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-detect_by_vendor"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.detect\_by\_vendor

```python
def detect_by_vendor(self, vendor: GPUVendor) -> List[GPUInfo]:
```

检测特定厂商的GPU
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-add_command"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.add\_command

```python
def add_command(self, command: GPUDetectionCommand):
```

动态添加命令（用于扩展）
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-remove_command"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.remove\_command

```python
def remove_command(self, vendor: GPUVendor):
```

移除命令
<a name="hardware-gpu-core-command_executor-GPUCommandExecutor-get_registered_vendors"></a>
#### 🅵 hardware\.gpu\.core\.command\_executor\.GPUCommandExecutor\.get\_registered\_vendors

```python
def get_registered_vendors(self) -> List[GPUVendor]:
```

获取已注册的厂商列表
<a name="hardware-gpu-core-factory"></a>
## 🅼 hardware\.gpu\.core\.factory

- **Classes:**
  - 🅲 [GPUDetectorFactory](#hardware-gpu-core-factory-GPUDetectorFactory)

### Classes

<a name="hardware-gpu-core-factory-GPUDetectorFactory"></a>
### 🅲 hardware\.gpu\.core\.factory\.GPUDetectorFactory

```python
class GPUDetectorFactory:
```

GPU检测器工厂

**Functions:**

<a name="hardware-gpu-core-factory-GPUDetectorFactory-__init__"></a>
#### 🅵 hardware\.gpu\.core\.factory\.GPUDetectorFactory\.\_\_init\_\_

```python
def __init__(self):
```
<a name="hardware-gpu-core-factory-GPUDetectorFactory-get_detector"></a>
#### 🅵 hardware\.gpu\.core\.factory\.GPUDetectorFactory\.get\_detector

```python
def get_detector(self, lspci_line: str, gpu_name: str) -> Optional[BaseGPUDetector]:
```

根据lspci行获取合适的检测器
<a name="hardware-gpu-core-factory-GPUDetectorFactory-detect_all"></a>
#### 🅵 hardware\.gpu\.core\.factory\.GPUDetectorFactory\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU
<a name="hardware-gpu-gpu_detecter"></a>
## 🅼 hardware\.gpu\.gpu\_detecter

- **Functions:**
  - 🅵 [gpu\_detected](#hardware-gpu-gpu_detecter-gpu_detected)
  - 🅵 [get\_gpu\_summary](#hardware-gpu-gpu_detecter-get_gpu_summary)

### Functions

<a name="hardware-gpu-gpu_detecter-gpu_detected"></a>
### 🅵 hardware\.gpu\.gpu\_detecter\.gpu\_detected

```python
def gpu_detected() -> Dict[str, Any]:
```

检测GPU信息（独立显卡和集成显卡）

这是API文档中定义的接口，保持向后兼容

**Returns:**

- `Dict`: GPU检测结果字典
<a name="hardware-gpu-gpu_detecter-get_gpu_summary"></a>
### 🅵 hardware\.gpu\.gpu\_detecter\.get\_gpu\_summary

```python
def get_gpu_summary() -> Dict[str, Any]:
```

获取GPU摘要信息

这是API文档中定义的接口

**Returns:**

- `Dict`: GPU摘要信息
<a name="hardware-gpu-vendor"></a>
## 🅼 hardware\.gpu\.vendor
<a name="hardware-gpu-vendor-amd"></a>
## 🅼 hardware\.gpu\.vendor\.amd

- **Classes:**
  - 🅲 [AMDDetector](#hardware-gpu-vendor-amd-AMDDetector)

### Classes

<a name="hardware-gpu-vendor-amd-AMDDetector"></a>
### 🅲 hardware\.gpu\.vendor\.amd\.AMDDetector

```python
class AMDDetector(BaseGPUDetector):
```

AMD GPU检测器

**Functions:**

<a name="hardware-gpu-vendor-amd-AMDDetector-vendor"></a>
#### 🅵 hardware\.gpu\.vendor\.amd\.AMDDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-vendor-amd-AMDDetector-detect_from_lspci"></a>
#### 🅵 hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测AMD GPU
<a name="hardware-gpu-vendor-amd-AMDDetector-detect_driver_version"></a>
#### 🅵 hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测AMD驱动版本
<a name="hardware-gpu-vendor-amd-AMDDetector-detect_rocm_version"></a>
#### 🅵 hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_rocm\_version

```python
def detect_rocm_version(self) -> Optional[str]:
```

检测ROCm版本
<a name="hardware-gpu-vendor-amd-AMDDetector-enhance_gpu_info"></a>
#### 🅵 hardware\.gpu\.vendor\.amd\.AMDDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强AMD GPU信息
<a name="hardware-gpu-vendor-huawei"></a>
## 🅼 hardware\.gpu\.vendor\.huawei

- **Classes:**
  - 🅲 [HuaweiDetector](#hardware-gpu-vendor-huawei-HuaweiDetector)

### Classes

<a name="hardware-gpu-vendor-huawei-HuaweiDetector"></a>
### 🅲 hardware\.gpu\.vendor\.huawei\.HuaweiDetector

```python
class HuaweiDetector(BaseGPUDetector):
```

华为昇腾GPU检测器

**Functions:**

<a name="hardware-gpu-vendor-huawei-HuaweiDetector-vendor"></a>
#### 🅵 hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-vendor-huawei-HuaweiDetector-detect_from_lspci"></a>
#### 🅵 hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测华为昇腾GPU
<a name="hardware-gpu-vendor-huawei-HuaweiDetector-detect_driver_version"></a>
#### 🅵 hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测昇腾驱动版本
<a name="hardware-gpu-vendor-huawei-HuaweiDetector-detect_ascend_version"></a>
#### 🅵 hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_ascend\_version

```python
def detect_ascend_version(self) -> Optional[str]:
```

检测CANN版本
<a name="hardware-gpu-vendor-huawei-HuaweiDetector-enhance_gpu_info"></a>
#### 🅵 hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强昇腾GPU信息
<a name="hardware-gpu-vendor-intel"></a>
## 🅼 hardware\.gpu\.vendor\.intel

- **Classes:**
  - 🅲 [IntelDetector](#hardware-gpu-vendor-intel-IntelDetector)

### Classes

<a name="hardware-gpu-vendor-intel-IntelDetector"></a>
### 🅲 hardware\.gpu\.vendor\.intel\.IntelDetector

```python
class IntelDetector(BaseGPUDetector):
```

Intel GPU检测器

**Functions:**

<a name="hardware-gpu-vendor-intel-IntelDetector-vendor"></a>
#### 🅵 hardware\.gpu\.vendor\.intel\.IntelDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-vendor-intel-IntelDetector-detect_from_lspci"></a>
#### 🅵 hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测Intel GPU
<a name="hardware-gpu-vendor-intel-IntelDetector-detect_driver_version"></a>
#### 🅵 hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测Intel驱动版本
<a name="hardware-gpu-vendor-nvidia"></a>
## 🅼 hardware\.gpu\.vendor\.nvidia

- **Classes:**
  - 🅲 [NVIDIADetector](#hardware-gpu-vendor-nvidia-NVIDIADetector)

### Classes

<a name="hardware-gpu-vendor-nvidia-NVIDIADetector"></a>
### 🅲 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector

```python
class NVIDIADetector(BaseGPUDetector):
```

NVIDIA GPU检测器

**Functions:**

<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-vendor"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-detect_from_lspci"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测NVIDIA GPU
<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-detect_driver_version"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测NVIDIA驱动版本
<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-detect_cuda_version"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_cuda\_version

```python
def detect_cuda_version(self) -> Optional[str]:
```

检测CUDA版本
<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-detect_nvlink"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_nvlink

```python
def detect_nvlink(self) -> Dict[str, Any]:
```

检测NVLink状态
<a name="hardware-gpu-vendor-nvidia-NVIDIADetector-enhance_gpu_info"></a>
#### 🅵 hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强NVIDIA GPU信息
<a name="hardware-gpu-vendor-utils"></a>
## 🅼 hardware\.gpu\.vendor\.utils

- **Functions:**
  - 🅵 [run\_cmd\_safe](#hardware-gpu-vendor-utils-run_cmd_safe)
  - 🅵 [extract\_gpu\_name](#hardware-gpu-vendor-utils-extract_gpu_name)
  - 🅵 [get\_gpu\_memory](#hardware-gpu-vendor-utils-get_gpu_memory)
  - 🅵 [get\_gpu\_specs](#hardware-gpu-vendor-utils-get_gpu_specs)

### Functions

<a name="hardware-gpu-vendor-utils-run_cmd_safe"></a>
### 🅵 hardware\.gpu\.vendor\.utils\.run\_cmd\_safe

```python
def run_cmd_safe(cmd: str, timeout: int = 5):
```

安全执行命令
<a name="hardware-gpu-vendor-utils-extract_gpu_name"></a>
### 🅵 hardware\.gpu\.vendor\.utils\.extract\_gpu\_name

```python
def extract_gpu_name(line: str) -> str:
```

从 lspci 输出中提取干净的 GPU 名称
<a name="hardware-gpu-vendor-utils-get_gpu_memory"></a>
### 🅵 hardware\.gpu\.vendor\.utils\.get\_gpu\_memory

```python
def get_gpu_memory(gpu_name: str, gpu_raw_line: Optional[str] = None) -> Optional[int]:
```

获取 GPU 显存大小（GB）
<a name="hardware-gpu-vendor-utils-get_gpu_specs"></a>
### 🅵 hardware\.gpu\.vendor\.utils\.get\_gpu\_specs

```python
def get_gpu_specs(gpu_name: str) -> Optional[Dict[str, Any]]:
```

根据GPU名称获取完整规格
<a name="hardware-mem"></a>
## 🅼 hardware\.mem
<a name="hardware-mem-mem_detecter"></a>
## 🅼 hardware\.mem\.mem\_detecter

- **Constants:**
  - 🆅 [MEMORY\_SPECS](#hardware-mem-mem_detecter-MEMORY_SPECS)
- **Functions:**
  - 🅵 [match\_memory\_spec](#hardware-mem-mem_detecter-match_memory_spec)
  - 🅵 [mem\_detected](#hardware-mem-mem_detecter-mem_detected)

### Constants

<a name="hardware-mem-mem_detecter-MEMORY_SPECS"></a>
### 🆅 hardware\.mem\.mem\_detecter\.MEMORY\_SPECS

```python
MEMORY_SPECS = [2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
```

### Functions

<a name="hardware-mem-mem_detecter-match_memory_spec"></a>
### 🅵 hardware\.mem\.mem\_detecter\.match\_memory\_spec

```python
def match_memory_spec(total_bytes):
```

根据实际内存大小，匹配最接近的标准规格

512GB 及以下：向上匹配到标准规格
512GB 以上：返回 512（表示 512GB 或更多）
<a name="hardware-mem-mem_detecter-mem_detected"></a>
### 🅵 hardware\.mem\.mem\_detecter\.mem\_detected

```python
def mem_detected():
```

检测内存信息 - 使用规格匹配算法
