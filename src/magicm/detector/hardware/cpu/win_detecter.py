# magicm/detector/hardware/cpu/win_detecter.py

import re
from magicm.utils.util import run_cmd

def detecter():
    """
    Windows系统CPU检测函数。
    
    该函数通过多种方式（WMI、PowerShell、注册表）获取Windows系统下的CPU型号信息，
    并针对AMD处理器显示不完整的问题进行了专门处理。
    
    Returns:
        dict: 包含两个键的字典：
            - 'model' (str): CPU的完整原始名称。
            - 'simple_model' (str): 经过简化处理的CPU型号，更适合直接展示。
    
    异常处理:
        所有内部方法调用均被捕获异常，任一方法失败会继续尝试下一个备用方案，
        确保函数在各种异常情况下仍能返回一个有效的结果（或默认值）。
    """
    info = {'model': '未知', 'simple_model': '未知'}
    
    # 方法1: 使用wmic cpu get name (最准确)
    # 该方法直接获取CPU的Name属性，通常包含最完整的型号字符串
    try:
        rc, out, _ = run_cmd('wmic cpu get name /format:csv')
        if rc == 0:
            lines = out.strip().split('\n')
            for line in lines:
                # 过滤空行、包含'Node'的表头行，并确保CSV格式正确
                if line.strip() and 'Node' not in line and ',' in line:
                    # CSV格式: Node,Name
                    parts = line.split(',')
                    if len(parts) >= 2:
                        raw_model = parts[1].strip()
                        # 确保获取到的是有效的CPU型号字符串，而非列标题'Name'
                        if raw_model and not raw_model.startswith('Name'):
                            info['model'] = raw_model
                            info['simple_model'] = _simplify_cpu_model_windows(raw_model)
                            print(f"找到CPU型号: {raw_model}")  # 调试输出
                            return info
    except Exception as e:
        print(f"wmic name方法失败: {e}")
    
    # 方法2: 使用wmic cpu get caption
    # Caption属性是Name的备选，有时提供更友好的描述
    try:
        rc, out, _ = run_cmd('wmic cpu get caption /format:csv')
        if rc == 0:
            lines = out.strip().split('\n')
            for line in lines:
                if line.strip() and 'Node' not in line and ',' in line:
                    parts = line.split(',')
                    if len(parts) >= 2:
                        raw_model = parts[1].strip()
                        if raw_model and not raw_model.startswith('Caption'):
                            info['model'] = raw_model
                            info['simple_model'] = _simplify_cpu_model_windows(raw_model)
                            return info
    except Exception as e:
        print(f"wmic caption方法失败: {e}")
    
    # 方法3: 使用PowerShell获取更详细的信息
    # PowerShell可以调用Get-WmiObject获取更全面的处理器对象属性
    try:
        ps_cmd = 'powershell -command "Get-WmiObject -Class Win32_Processor | Select-Object Name, Caption, Description | ConvertTo-Csv -NoTypeInformation"'
        rc, out, _ = run_cmd(ps_cmd)
        if rc == 0:
            lines = out.strip().split('\n')
            for line in lines:
                # 解析CSV行，忽略标题行（包含'Name'）
                if line.strip() and ',' in line and 'Name' not in line:
                    # 移除引号并按逗号分隔
                    parts = line.strip('"').split('","')
                    if len(parts) >= 1 and parts[0].strip():
                        raw_model = parts[0].strip()
                        info['model'] = raw_model
                        info['simple_model'] = _simplify_cpu_model_windows(raw_model)
                        return info
    except Exception as e:
        print(f"PowerShell方法失败: {e}")
    
    # 方法4: 使用注册表读取
    # 直接从注册表项 HARDWARE\DESCRIPTION\System\CentralProcessor\0 中获取 ProcessorNameString 值
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                            r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
        value, _ = winreg.QueryValueEx(key, "ProcessorNameString")
        if value:
            info['model'] = value
            info['simple_model'] = _simplify_cpu_model_windows(value)
            return info
    except Exception:
        # 注册表读取失败时静默忽略，继续返回默认值
        pass
    
    # 所有方法均失败，返回包含默认值的字典
    return info

def _simplify_cpu_model_windows(model):
    """
    专门处理Windows下的CPU型号简化。
    
    该函数针对常见的AMD Ryzen和Intel Core处理器型号进行字符串精简，
    移除冗余的图形核心描述（如 "w/ Radeon 780M Graphics"），提取核心型号。
    
    Args:
        model (str): CPU的完整原始名称字符串。
    
    Returns:
        str: 简化后的CPU型号字符串，如果输入为空则返回'未知'。
             - AMD Ryzen示例: "Ryzen 7 8845HS"
             - Intel Core示例: "i7-12700K" 或 "Core i7"
             - 其他情况: 截取原始字符串的前40个字符或前3个单词。
    """
    if not model:
        return '未知'
    
    # AMD Ryzen 7 8845HS 处理
    # 匹配格式: AMD Ryzen 7 8845HS w/ Radeon 780M Graphics
    # 捕获组1: 系列数字 (如7)，捕获组2: 具体型号 (如8845HS)
    ryzen_match = re.search(r'AMD\s+Ryzen\s+(\d+)\s+(\d{4}[A-Z]*)', model, re.IGNORECASE)
    if ryzen_match:
        series = ryzen_match.group(1)  # 例如: 7
        model_num = ryzen_match.group(2)  # 例如: 8845HS
        return f"Ryzen {series} {model_num}"
    
    # 匹配更简单的格式: Ryzen 7 8845HS (不包含AMD前缀)
    ryzen_simple = re.search(r'Ryzen\s+\d+\s+\d{4}[A-Z]*', model, re.IGNORECASE)
    if ryzen_simple:
        return ryzen_simple.group(0)
    
    # 仅匹配Ryzen系列，不匹配具体型号: Ryzen 7
    ryzen_series = re.search(r'Ryzen\s+(\d+)', model, re.IGNORECASE)
    if ryzen_series:
        return f"Ryzen {ryzen_series.group(1)}"
    
    # Intel CPU处理: 匹配 i7-12700K 或 i9-13900H 等格式
    intel_match = re.search(r'i\d-\d{4,5}[A-Z]*', model, re.IGNORECASE)
    if intel_match:
        return intel_match.group(0)
    
    # Intel Core i系列: 匹配 "Core i5", "Core i7" 等
    intel_core = re.search(r'Core.*?i[3579]', model, re.IGNORECASE)
    if intel_core:
        return intel_core.group(0)
    
    # 如果上述所有模式均未匹配到，则进行通用截断处理
    # 策略1: 如果型号长度超过40字符，尝试返回前3个单词
    if len(model) > 40:
        parts = model.split()
        if len(parts) >= 3:
            return ' '.join(parts[:3])
    
    # 默认返回原始模型（或截断后的原始模型）
    return model