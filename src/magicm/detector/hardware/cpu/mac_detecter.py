# magicm/detector/hardware/cpu/mac_detecter.py

from magicm.utils.util import run_cmd
from .cpu_model import cpu_model as modeler

def detect():
    """
    macOS系统CPU检测函数。
    
    该函数通过 sysctl 命令获取 macOS 系统下的 CPU 品牌字符串信息，
    并使用外部模型简化函数对型号进行精简处理。
    
    Returns:
        dict: 包含两个键的字典：
            - 'model' (str): CPU的完整原始品牌字符串。
            - 'simple_model' (str): 经过简化处理的CPU型号，更适合直接展示。
    
    注意:
        macOS 使用 machdep.cpu.brand_string 参数存储 CPU 的完整品牌信息，
        该信息与 Linux 的 /proc/cpuinfo 中的 model name 类似。
    
    异常处理:
        如果 sysctl 命令执行失败或返回空结果，函数将返回包含默认值 '未知' 的字典。
    """
    info = {'model': '未知', 'simple_model': '未知'}
    
    # 使用 sysctl 命令获取 CPU 品牌字符串
    # sysctl -n 参数表示只输出值，不输出键名
    # machdep.cpu.brand_string 是 macOS 内核参数，存储 CPU 的完整品牌信息
    # 示例输出: "Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz" 或 "Apple M1 Pro"
    rc, out, _ = run_cmd('sysctl -n machdep.cpu.brand_string')
    
    # 检查命令执行成功且有输出内容
    if rc == 0 and out:
        # 去除输出字符串首尾的空白字符（换行符、空格等）
        raw_model = out.strip()
        info['model'] = raw_model
        # 调用外部简化函数，生成更简洁的型号名称
        # 例如: "Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz" -> "i7-8750H"
        #       "Apple M1 Pro" -> "M1 Pro"
        info['simple_model'] = modeler(raw_model)
    
    return info