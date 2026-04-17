# magicm/detector/hardware/cpu/linux_detecter.py

from magicm.utils.util import run_cmd
from .cpu_model import cpu_model as modeler

def detecter():
    """
    Linux系统CPU检测函数。
    
    该函数通过读取系统文件 /proc/cpuinfo 或使用 lscpu 命令来获取
    Linux系统下的CPU型号信息，并使用外部模型简化函数对型号进行精简。
    
    Returns:
        dict: 包含两个键的字典：
            - 'model' (str): CPU的完整原始名称。
            - 'simple_model' (str): 经过简化处理的CPU型号，更适合直接展示。
    
    异常处理:
        优先尝试读取 /proc/cpuinfo，如果失败（如文件不存在或权限问题），
        则自动降级使用 lscpu 命令作为备用方案。
    """
    info = {'model': '未知', 'simple_model': '未知'}
    
    # 方法1: 从 /proc/cpuinfo 读取CPU信息（标准Linux方式）
    # 该文件包含了系统中每个CPU核心的详细信息，其中 'model name' 字段存储CPU型号
    try:
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                # 查找包含 'model name' 的行，这是CPU型号的标准字段
                if 'model name' in line:
                    # 提取冒号后的内容并去除首尾空白字符
                    raw_model = line.split(':')[1].strip()
                    info['model'] = raw_model
                    # 调用外部简化函数，生成更简洁的型号名称
                    info['simple_model'] = modeler(raw_model)
                    break  # 找到第一个CPU核心的型号即可，无需继续读取
    except Exception:
        # 方法2: 备用方案 - 使用 lscpu 命令
        # lscpu 是Linux系统提供的CPU架构信息查看工具，某些精简系统可能不包含/proc/cpuinfo
        try:
            rc, out, _ = run_cmd('lscpu | grep "Model name"')
            if rc == 0 and out:
                # 解析输出格式：通常为 "Model name:          CPU型号"
                raw_model = out.split(':')[1].strip()
                info['model'] = raw_model
                info['simple_model'] = modeler(raw_model)
        except Exception:
            # 如果两种方法都失败，保持默认值 '未知'
            pass
    
    return info