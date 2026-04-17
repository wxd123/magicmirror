# `detector`

## Table of Contents

- 🅼 [detector](#detector)
- 🅼 [detector\.hardware](#detector-hardware)
- 🅼 [detector\.hardware\.cpu](#detector-hardware-cpu)
- 🅼 [detector\.hardware\.cpu\.cpu\_detecter](#detector-hardware-cpu-cpu_detecter)
- 🅼 [detector\.hardware\.cpu\.cpu\_model](#detector-hardware-cpu-cpu_model)
- 🅼 [detector\.hardware\.cpu\.linux\_detecter](#detector-hardware-cpu-linux_detecter)
- 🅼 [detector\.hardware\.cpu\.mac\_detecter](#detector-hardware-cpu-mac_detecter)
- 🅼 [detector\.hardware\.cpu\.win\_detecter](#detector-hardware-cpu-win_detecter)
- 🅼 [detector\.hardware\.gpu](#detector-hardware-gpu)
- 🅼 [detector\.hardware\.gpu\.amd](#detector-hardware-gpu-amd)
- 🅼 [detector\.hardware\.gpu\.gpu\_detecter](#detector-hardware-gpu-gpu_detecter)
- 🅼 [detector\.hardware\.gpu\.gpu\_typer](#detector-hardware-gpu-gpu_typer)
- 🅼 [detector\.hardware\.gpu\.nvidia\_detecter](#detector-hardware-gpu-nvidia_detecter)
- 🅼 [detector\.hardware\.gpu\.system](#detector-hardware-gpu-system)
- 🅼 [detector\.hardware\.gpu\.system\.linux\_detecter](#detector-hardware-gpu-system-linux_detecter)
- 🅼 [detector\.hardware\.gpu\.system\.mac\_detecter](#detector-hardware-gpu-system-mac_detecter)
- 🅼 [detector\.hardware\.gpu\.system\.win\_detecter](#detector-hardware-gpu-system-win_detecter)
- 🅼 [detector\.hardware\.gpu\.vendor](#detector-hardware-gpu-vendor)
- 🅼 [detector\.hardware\.gpu\.vendor\.amd](#detector-hardware-gpu-vendor-amd)
- 🅼 [detector\.hardware\.gpu\.vendor\.base](#detector-hardware-gpu-vendor-base)
- 🅼 [detector\.hardware\.gpu\.vendor\.factory](#detector-hardware-gpu-vendor-factory)
- 🅼 [detector\.hardware\.gpu\.vendor\.huawei](#detector-hardware-gpu-vendor-huawei)
- 🅼 [detector\.hardware\.gpu\.vendor\.intel](#detector-hardware-gpu-vendor-intel)
- 🅼 [detector\.hardware\.gpu\.vendor\.nvidia](#detector-hardware-gpu-vendor-nvidia)
- 🅼 [detector\.hardware\.gpu\.vendor\.utils](#detector-hardware-gpu-vendor-utils)
- 🅼 [detector\.hardware\.mem](#detector-hardware-mem)
- 🅼 [detector\.hardware\.mem\.mem\_detecter](#detector-hardware-mem-mem_detecter)
- 🅼 [detector\.software](#detector-software)
- 🅼 [detector\.software\.driver](#detector-software-driver)
- 🅼 [detector\.software\.driver\.cann](#detector-software-driver-cann)
- 🅼 [detector\.software\.driver\.cuda](#detector-software-driver-cuda)
- 🅼 [detector\.software\.driver\.driver\_detecter](#detector-software-driver-driver_detecter)
- 🅼 [detector\.software\.driver\.oneapi](#detector-software-driver-oneapi)
- 🅼 [detector\.software\.driver\.rocm](#detector-software-driver-rocm)
- 🅼 [detector\.software\.system](#detector-software-system)
- 🅼 [detector\.software\.system\.linux\_detecter](#detector-software-system-linux_detecter)
- 🅼 [detector\.software\.system\.sys\_detecter](#detector-software-system-sys_detecter)
- 🅼 [detector\.software\.system\.win\_detecter](#detector-software-system-win_detecter)

<a name="detector"></a>
## 🅼 detector
<a name="detector-hardware"></a>
## 🅼 detector\.hardware
<a name="detector-hardware-cpu"></a>
## 🅼 detector\.hardware\.cpu
<a name="detector-hardware-cpu-cpu_detecter"></a>
## 🅼 detector\.hardware\.cpu\.cpu\_detecter

- **Functions:**
  - 🅵 [cpu\_detected](#detector-hardware-cpu-cpu_detecter-cpu_detected)
  - 🅵 [get\_cpu\_summary](#detector-hardware-cpu-cpu_detecter-get_cpu_summary)

### Functions

<a name="detector-hardware-cpu-cpu_detecter-cpu_detected"></a>
### 🅵 detector\.hardware\.cpu\.cpu\_detecter\.cpu\_detected

```python
def cpu_detected():
```

检测CPU信息 - 增强版
<a name="detector-hardware-cpu-cpu_detecter-get_cpu_summary"></a>
### 🅵 detector\.hardware\.cpu\.cpu\_detecter\.get\_cpu\_summary

```python
def get_cpu_summary():
```

获取CPU摘要信息
<a name="detector-hardware-cpu-cpu_model"></a>
## 🅼 detector\.hardware\.cpu\.cpu\_model

- **Functions:**
  - 🅵 [cpu\_model](#detector-hardware-cpu-cpu_model-cpu_model)

### Functions

<a name="detector-hardware-cpu-cpu_model-cpu_model"></a>
### 🅵 detector\.hardware\.cpu\.cpu\_model\.cpu\_model

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
<a name="detector-hardware-cpu-linux_detecter"></a>
## 🅼 detector\.hardware\.cpu\.linux\_detecter

- **Functions:**
  - 🅵 [detecter](#detector-hardware-cpu-linux_detecter-detecter)

### Functions

<a name="detector-hardware-cpu-linux_detecter-detecter"></a>
### 🅵 detector\.hardware\.cpu\.linux\_detecter\.detecter

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
<a name="detector-hardware-cpu-mac_detecter"></a>
## 🅼 detector\.hardware\.cpu\.mac\_detecter

- **Functions:**
  - 🅵 [detect](#detector-hardware-cpu-mac_detecter-detect)

### Functions

<a name="detector-hardware-cpu-mac_detecter-detect"></a>
### 🅵 detector\.hardware\.cpu\.mac\_detecter\.detect

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
<a name="detector-hardware-cpu-win_detecter"></a>
## 🅼 detector\.hardware\.cpu\.win\_detecter

- **Functions:**
  - 🅵 [detecter](#detector-hardware-cpu-win_detecter-detecter)

### Functions

<a name="detector-hardware-cpu-win_detecter-detecter"></a>
### 🅵 detector\.hardware\.cpu\.win\_detecter\.detecter

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
<a name="detector-hardware-gpu"></a>
## 🅼 detector\.hardware\.gpu
<a name="detector-hardware-gpu-amd"></a>
## 🅼 detector\.hardware\.gpu\.amd
<a name="detector-hardware-gpu-gpu_detecter"></a>
## 🅼 detector\.hardware\.gpu\.gpu\_detecter

- **Functions:**
  - 🅵 [gpu\_detected](#detector-hardware-gpu-gpu_detecter-gpu_detected)
  - 🅵 [get\_gpu\_summary](#detector-hardware-gpu-gpu_detecter-get_gpu_summary)

### Functions

<a name="detector-hardware-gpu-gpu_detecter-gpu_detected"></a>
### 🅵 detector\.hardware\.gpu\.gpu\_detecter\.gpu\_detected

```python
def gpu_detected():
```

检测GPU信息（独立显卡和集成显卡）
<a name="detector-hardware-gpu-gpu_detecter-get_gpu_summary"></a>
### 🅵 detector\.hardware\.gpu\.gpu\_detecter\.get\_gpu\_summary

```python
def get_gpu_summary():
```

获取GPU摘要信息
<a name="detector-hardware-gpu-gpu_typer"></a>
## 🅼 detector\.hardware\.gpu\.gpu\_typer

- **Functions:**
  - 🅵 [determine](#detector-hardware-gpu-gpu_typer-determine)

### Functions

<a name="detector-hardware-gpu-gpu_typer-determine"></a>
### 🅵 detector\.hardware\.gpu\.gpu\_typer\.determine

```python
def determine(name):
```

判断显卡类型（独立还是集成）
<a name="detector-hardware-gpu-nvidia_detecter"></a>
## 🅼 detector\.hardware\.gpu\.nvidia\_detecter

- **Functions:**
  - 🅵 [nvidia\_driver](#detector-hardware-gpu-nvidia_detecter-nvidia_driver)
  - 🅵 [cuda\_version](#detector-hardware-gpu-nvidia_detecter-cuda_version)
  - 🅵 [nvidia\_gpu\_name](#detector-hardware-gpu-nvidia_detecter-nvidia_gpu_name)

### Functions

<a name="detector-hardware-gpu-nvidia_detecter-nvidia_driver"></a>
### 🅵 detector\.hardware\.gpu\.nvidia\_detecter\.nvidia\_driver

```python
def nvidia_driver(output):
```

从nvidia-smi输出中提取驱动版本
<a name="detector-hardware-gpu-nvidia_detecter-cuda_version"></a>
### 🅵 detector\.hardware\.gpu\.nvidia\_detecter\.cuda\_version

```python
def cuda_version(output):
```

从nvidia-smi输出中提取CUDA版本
<a name="detector-hardware-gpu-nvidia_detecter-nvidia_gpu_name"></a>
### 🅵 detector\.hardware\.gpu\.nvidia\_detecter\.nvidia\_gpu\_name

```python
def nvidia_gpu_name(output):
```

从nvidia-smi输出中提取GPU名称
<a name="detector-hardware-gpu-system"></a>
## 🅼 detector\.hardware\.gpu\.system
<a name="detector-hardware-gpu-system-linux_detecter"></a>
## 🅼 detector\.hardware\.gpu\.system\.linux\_detecter

- **Functions:**
  - 🅵 [detect](#detector-hardware-gpu-system-linux_detecter-detect)

### Functions

<a name="detector-hardware-gpu-system-linux_detecter-detect"></a>
### 🅵 detector\.hardware\.gpu\.system\.linux\_detecter\.detect

```python
def detect():
```

Linux系统GPU检测 - 增强版
<a name="detector-hardware-gpu-system-mac_detecter"></a>
## 🅼 detector\.hardware\.gpu\.system\.mac\_detecter

- **Functions:**
  - 🅵 [detect](#detector-hardware-gpu-system-mac_detecter-detect)

### Functions

<a name="detector-hardware-gpu-system-mac_detecter-detect"></a>
### 🅵 detector\.hardware\.gpu\.system\.mac\_detecter\.detect

```python
def detect():
```

macOS系统GPU检测
<a name="detector-hardware-gpu-system-win_detecter"></a>
## 🅼 detector\.hardware\.gpu\.system\.win\_detecter

- **Functions:**
  - 🅵 [detect](#detector-hardware-gpu-system-win_detecter-detect)

### Functions

<a name="detector-hardware-gpu-system-win_detecter-detect"></a>
### 🅵 detector\.hardware\.gpu\.system\.win\_detecter\.detect

```python
def detect():
```

Windows系统GPU检测（独立\+集成）
<a name="detector-hardware-gpu-vendor"></a>
## 🅼 detector\.hardware\.gpu\.vendor
<a name="detector-hardware-gpu-vendor-amd"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.amd

- **Classes:**
  - 🅲 [AMDDetector](#detector-hardware-gpu-vendor-amd-AMDDetector)

### Classes

<a name="detector-hardware-gpu-vendor-amd-AMDDetector"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector

```python
class AMDDetector(BaseGPUDetector):
```

AMD GPU检测器

**Functions:**

<a name="detector-hardware-gpu-vendor-amd-AMDDetector-vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="detector-hardware-gpu-vendor-amd-AMDDetector-detect_from_lspci"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测AMD GPU
<a name="detector-hardware-gpu-vendor-amd-AMDDetector-detect_driver_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测AMD驱动版本
<a name="detector-hardware-gpu-vendor-amd-AMDDetector-detect_rocm_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.detect\_rocm\_version

```python
def detect_rocm_version(self) -> Optional[str]:
```

检测ROCm版本
<a name="detector-hardware-gpu-vendor-amd-AMDDetector-enhance_gpu_info"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.amd\.AMDDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强AMD GPU信息
<a name="detector-hardware-gpu-vendor-base"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.base

- **Classes:**
  - 🅲 [GPUVendor](#detector-hardware-gpu-vendor-base-GPUVendor)
  - 🅲 [GPUType](#detector-hardware-gpu-vendor-base-GPUType)
  - 🅲 [GPUInfo](#detector-hardware-gpu-vendor-base-GPUInfo)
  - 🅲 [DetectionResult](#detector-hardware-gpu-vendor-base-DetectionResult)
  - 🅲 [BaseGPUDetector](#detector-hardware-gpu-vendor-base-BaseGPUDetector)

### Classes

<a name="detector-hardware-gpu-vendor-base-GPUVendor"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.base\.GPUVendor

```python
class GPUVendor(Enum):
```
<a name="detector-hardware-gpu-vendor-base-GPUType"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.base\.GPUType

```python
class GPUType(Enum):
```
<a name="detector-hardware-gpu-vendor-base-GPUInfo"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.base\.GPUInfo

```python
class GPUInfo:
```

GPU信息数据类

**Functions:**

<a name="detector-hardware-gpu-vendor-base-GPUInfo-to_dict"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.GPUInfo\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典
<a name="detector-hardware-gpu-vendor-base-DetectionResult"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.base\.DetectionResult

```python
class DetectionResult:
```

检测结果数据类

**Functions:**

<a name="detector-hardware-gpu-vendor-base-DetectionResult-main_gpu"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.DetectionResult\.main\_gpu

```python
def main_gpu(self) -> Optional[GPUInfo]:
```

获取主GPU（优先离散，其次集成）
<a name="detector-hardware-gpu-vendor-base-DetectionResult-to_dict"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.DetectionResult\.to\_dict

```python
def to_dict(self) -> Dict[str, Any]:
```

转换为字典（兼容原有格式）
<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector

```python
class BaseGPUDetector(ABC):
```

GPU检测器基类

**Functions:**

<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector-vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```

返回检测器支持的厂商
<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector-detect_from_lspci"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

从lspci行检测GPU信息
<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector-detect_driver_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测驱动版本
<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector-enhance_gpu_info"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强GPU信息（填充额外字段）
<a name="detector-hardware-gpu-vendor-base-BaseGPUDetector-supports_vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.base\.BaseGPUDetector\.supports\_vendor

```python
def supports_vendor(self, line: str, name: str) -> bool:
```

判断是否支持该厂商的GPU
<a name="detector-hardware-gpu-vendor-factory"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.factory

- **Classes:**
  - 🅲 [GPUDetectorFactory](#detector-hardware-gpu-vendor-factory-GPUDetectorFactory)

### Classes

<a name="detector-hardware-gpu-vendor-factory-GPUDetectorFactory"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.factory\.GPUDetectorFactory

```python
class GPUDetectorFactory:
```

GPU检测器工厂

**Functions:**

<a name="detector-hardware-gpu-vendor-factory-GPUDetectorFactory-__init__"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.factory\.GPUDetectorFactory\.\_\_init\_\_

```python
def __init__(self):
```
<a name="detector-hardware-gpu-vendor-factory-GPUDetectorFactory-get_detector"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.factory\.GPUDetectorFactory\.get\_detector

```python
def get_detector(self, lspci_line: str, gpu_name: str) -> Optional[BaseGPUDetector]:
```

根据lspci行获取合适的检测器
<a name="detector-hardware-gpu-vendor-factory-GPUDetectorFactory-detect_all"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.factory\.GPUDetectorFactory\.detect\_all

```python
def detect_all(self) -> DetectionResult:
```

检测所有GPU
<a name="detector-hardware-gpu-vendor-huawei"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.huawei

- **Classes:**
  - 🅲 [HuaweiDetector](#detector-hardware-gpu-vendor-huawei-HuaweiDetector)

### Classes

<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector

```python
class HuaweiDetector(BaseGPUDetector):
```

华为昇腾GPU检测器

**Functions:**

<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector-vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_from_lspci"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测华为昇腾GPU
<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_driver_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测昇腾驱动版本
<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector-detect_ascend_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.detect\_ascend\_version

```python
def detect_ascend_version(self) -> Optional[str]:
```

检测CANN版本
<a name="detector-hardware-gpu-vendor-huawei-HuaweiDetector-enhance_gpu_info"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.huawei\.HuaweiDetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强昇腾GPU信息
<a name="detector-hardware-gpu-vendor-intel"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.intel

- **Classes:**
  - 🅲 [IntelDetector](#detector-hardware-gpu-vendor-intel-IntelDetector)

### Classes

<a name="detector-hardware-gpu-vendor-intel-IntelDetector"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.intel\.IntelDetector

```python
class IntelDetector(BaseGPUDetector):
```

Intel GPU检测器

**Functions:**

<a name="detector-hardware-gpu-vendor-intel-IntelDetector-vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="detector-hardware-gpu-vendor-intel-IntelDetector-detect_from_lspci"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测Intel GPU
<a name="detector-hardware-gpu-vendor-intel-IntelDetector-detect_driver_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.intel\.IntelDetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测Intel驱动版本
<a name="detector-hardware-gpu-vendor-nvidia"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.nvidia

- **Classes:**
  - 🅲 [NVIDIADetector](#detector-hardware-gpu-vendor-nvidia-NVIDIADetector)

### Classes

<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector"></a>
### 🅲 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector

```python
class NVIDIADetector(BaseGPUDetector):
```

NVIDIA GPU检测器

**Functions:**

<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-vendor"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.vendor

```python
def vendor(self) -> GPUVendor:
```
<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_from_lspci"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_from\_lspci

```python
def detect_from_lspci(self, lspci_line: str, gpu_name: str) -> Optional[GPUInfo]:
```

检测NVIDIA GPU
<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_driver_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_driver\_version

```python
def detect_driver_version(self, gpu_info: GPUInfo) -> Optional[str]:
```

检测NVIDIA驱动版本
<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_cuda_version"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_cuda\_version

```python
def detect_cuda_version(self) -> Optional[str]:
```

检测CUDA版本
<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-detect_nvlink"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.detect\_nvlink

```python
def detect_nvlink(self) -> Dict[str, Any]:
```

检测NVLink状态
<a name="detector-hardware-gpu-vendor-nvidia-NVIDIADetector-enhance_gpu_info"></a>
#### 🅵 detector\.hardware\.gpu\.vendor\.nvidia\.NVIDIADetector\.enhance\_gpu\_info

```python
def enhance_gpu_info(self, gpu_info: GPUInfo) -> GPUInfo:
```

增强NVIDIA GPU信息
<a name="detector-hardware-gpu-vendor-utils"></a>
## 🅼 detector\.hardware\.gpu\.vendor\.utils

- **Functions:**
  - 🅵 [run\_cmd\_safe](#detector-hardware-gpu-vendor-utils-run_cmd_safe)
  - 🅵 [extract\_gpu\_name](#detector-hardware-gpu-vendor-utils-extract_gpu_name)
  - 🅵 [get\_gpu\_memory](#detector-hardware-gpu-vendor-utils-get_gpu_memory)
  - 🅵 [get\_gpu\_specs](#detector-hardware-gpu-vendor-utils-get_gpu_specs)

### Functions

<a name="detector-hardware-gpu-vendor-utils-run_cmd_safe"></a>
### 🅵 detector\.hardware\.gpu\.vendor\.utils\.run\_cmd\_safe

```python
def run_cmd_safe(cmd: str, timeout: int = 5):
```

安全执行命令
<a name="detector-hardware-gpu-vendor-utils-extract_gpu_name"></a>
### 🅵 detector\.hardware\.gpu\.vendor\.utils\.extract\_gpu\_name

```python
def extract_gpu_name(line: str) -> str:
```

从 lspci 输出中提取干净的 GPU 名称
<a name="detector-hardware-gpu-vendor-utils-get_gpu_memory"></a>
### 🅵 detector\.hardware\.gpu\.vendor\.utils\.get\_gpu\_memory

```python
def get_gpu_memory(gpu_name: str, gpu_raw_line: Optional[str] = None) -> Optional[int]:
```

获取 GPU 显存大小（GB）
<a name="detector-hardware-gpu-vendor-utils-get_gpu_specs"></a>
### 🅵 detector\.hardware\.gpu\.vendor\.utils\.get\_gpu\_specs

```python
def get_gpu_specs(gpu_name: str) -> Optional[Dict[str, Any]]:
```

根据GPU名称获取完整规格
<a name="detector-hardware-mem"></a>
## 🅼 detector\.hardware\.mem
<a name="detector-hardware-mem-mem_detecter"></a>
## 🅼 detector\.hardware\.mem\.mem\_detecter

- **Constants:**
  - 🆅 [MEMORY\_SPECS](#detector-hardware-mem-mem_detecter-MEMORY_SPECS)
- **Functions:**
  - 🅵 [match\_memory\_spec](#detector-hardware-mem-mem_detecter-match_memory_spec)
  - 🅵 [mem\_detected](#detector-hardware-mem-mem_detecter-mem_detected)

### Constants

<a name="detector-hardware-mem-mem_detecter-MEMORY_SPECS"></a>
### 🆅 detector\.hardware\.mem\.mem\_detecter\.MEMORY\_SPECS

```python
MEMORY_SPECS = [2, 4, 6, 8, 12, 16, 20, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
```

### Functions

<a name="detector-hardware-mem-mem_detecter-match_memory_spec"></a>
### 🅵 detector\.hardware\.mem\.mem\_detecter\.match\_memory\_spec

```python
def match_memory_spec(total_bytes):
```

根据实际内存大小，匹配最接近的标准规格

512GB 及以下：向上匹配到标准规格
512GB 以上：返回 512（表示 512GB 或更多）
<a name="detector-hardware-mem-mem_detecter-mem_detected"></a>
### 🅵 detector\.hardware\.mem\.mem\_detecter\.mem\_detected

```python
def mem_detected():
```

检测内存信息 - 使用规格匹配算法
<a name="detector-software"></a>
## 🅼 detector\.software
<a name="detector-software-driver"></a>
## 🅼 detector\.software\.driver
<a name="detector-software-driver-cann"></a>
## 🅼 detector\.software\.driver\.cann
<a name="detector-software-driver-cuda"></a>
## 🅼 detector\.software\.driver\.cuda
<a name="detector-software-driver-driver_detecter"></a>
## 🅼 detector\.software\.driver\.driver\_detecter
<a name="detector-software-driver-oneapi"></a>
## 🅼 detector\.software\.driver\.oneapi
<a name="detector-software-driver-rocm"></a>
## 🅼 detector\.software\.driver\.rocm
<a name="detector-software-system"></a>
## 🅼 detector\.software\.system
<a name="detector-software-system-linux_detecter"></a>
## 🅼 detector\.software\.system\.linux\_detecter

Linux 系统检测模块

- **Functions:**
  - 🅵 [detect](#detector-software-system-linux_detecter-detect)

### Functions

<a name="detector-software-system-linux_detecter-detect"></a>
### 🅵 detector\.software\.system\.linux\_detecter\.detect

```python
def detect():
```

检测 Linux 系统信息
<a name="detector-software-system-sys_detecter"></a>
## 🅼 detector\.software\.system\.sys\_detecter

- **Functions:**
  - 🅵 [detect](#detector-software-system-sys_detecter-detect)

### Functions

<a name="detector-software-system-sys_detecter-detect"></a>
### 🅵 detector\.software\.system\.sys\_detecter\.detect

```python
def detect():
```

检测操作系统信息 - 增强版
<a name="detector-software-system-win_detecter"></a>
## 🅼 detector\.software\.system\.win\_detecter

Windows 系统检测模块

- **Functions:**
  - 🅵 [detect](#detector-software-system-win_detecter-detect)

### Functions

<a name="detector-software-system-win_detecter-detect"></a>
### 🅵 detector\.software\.system\.win\_detecter\.detect

```python
def detect():
```

检测 Windows 系统信息
