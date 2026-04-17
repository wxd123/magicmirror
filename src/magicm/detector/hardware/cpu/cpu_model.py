# magicm/detector/hardware/cpu/cpu_model.py

import re

def cpu_model(model):
    """
    通用的CPU型号简化函数。
    
    该函数通过正则表达式匹配常见的CPU型号模式，从完整的CPU品牌字符串中
    提取出核心型号信息，使显示更加简洁清晰。
    
    Args:
        model (str): CPU的完整原始名称字符串。
                    例如: "AMD Ryzen 7 8845HS w/ Radeon 780M Graphics"
                          "Intel(R) Core(TM) i7-12700K CPU @ 3.60GHz"
    
    Returns:
        str: 简化后的CPU型号。
             - AMD Ryzen示例: "Ryzen 7 8845HS"
             - Intel Core示例: "i7-12700K"
             - 输入为空时: "未知"
             - 无法匹配时: 返回原始输入值
    
    注意:
        该函数当前仅支持AMD Ryzen和Intel Core系列CPU的简化，
        对于其他品牌（如Apple Silicon、VIA等）暂不处理，直接返回原始值。
        未来可根据需要扩展支持更多CPU品牌。
    """
    # 处理空输入的情况
    if not model:
        return '未知'
    
    # AMD Ryzen 系列 CPU 型号匹配
    # 匹配模式: Ryzen + 空格 + 系列数字 + 空格 + 4位数字型号 + 可选字母后缀
    # 示例匹配:
    #   - "Ryzen 7 8845HS" -> 匹配成功
    #   - "Ryzen 5 5600X" -> 匹配成功
    #   - "Ryzen 9 7950X3D" -> 匹配成功
    # 正则说明:
    #   - Ryzen\s+: 匹配 "Ryzen" 后跟一个或多个空白字符
    #   - \d+: 匹配一个或多个数字（系列号：3/5/7/9）
    #   - \s+: 匹配一个或多个空白字符
    #   - \d{4,5}: 匹配4位或5位数字（型号代码）
    #   - [A-Z]*: 匹配零个或多个大写字母后缀（如 H、HS、X、X3D 等）
    #   - re.IGNORECASE: 忽略大小写，兼容 "RYZEN"、"ryzen" 等写法
    ryzen_match = re.search(r'Ryzen\s+\d+\s+\d{4}[A-Z]*', model, re.IGNORECASE)
    if ryzen_match:
        return ryzen_match.group(0)
    
    # Intel Core 系列 CPU 型号匹配
    # 匹配模式: i + 数字 + - + 4-5位数字 + 可选字母后缀
    # 示例匹配:
    #   - "i7-12700K" -> 匹配成功
    #   - "i5-12400F" -> 匹配成功
    #   - "i9-13900HX" -> 匹配成功
    #   - "i3-10100" -> 匹配成功
    # 正则说明:
    #   - i\d: 匹配 "i" 后跟一个数字（3/5/7/9）
    #   - -: 匹配连字符
    #   - \d{4,5}: 匹配4位或5位数字（处理器编号）
    #   - [A-Z]*: 匹配零个或多个大写字母后缀（如 K、F、H、HX 等）
    #   - re.IGNORECASE: 忽略大小写，兼容 "I7-12700K" 等写法
    intel_match = re.search(r'i\d-\d{4,5}[A-Z]*', model, re.IGNORECASE)
    if intel_match:
        return intel_match.group(0)
    
    # 如果没有匹配到任何已知的CPU型号模式，则返回原始输入
    # 这样可以确保函数始终返回一个有效的字符串值
    return model