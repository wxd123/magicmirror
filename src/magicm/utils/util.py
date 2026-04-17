"""
通用命令执行模块

提供系统命令执行的通用功能，包括超时控制和错误处理。
可用于各种需要调用外部命令的场景。
"""

import subprocess


def run_cmd(cmd, timeout=120):
    """
    运行系统命令并返回执行结果
    
    该函数通过 subprocess 模块执行指定的 shell 命令，支持超时控制，
    并自动捕获标准输出和标准错误输出。命令执行过程中发生的异常会被
    捕获并转换为返回码 -1。
    
    Args:
        cmd (str): 要执行的 shell 命令字符串
        timeout (int, optional): 命令执行的超时时间（秒）。默认为 120 秒。
    
    Returns:
        tuple: (returncode, stdout, stderr)
            - returncode (int): 命令的返回码。成功执行通常返回 0，
              超时或异常时返回 -1
            - stdout (str): 命令的标准输出内容，已去除首尾空白字符。
              若无输出则为空字符串
            - stderr (str): 命令的标准错误输出内容，已去除首尾空白字符。
              若无输出或发生异常则为空字符串或异常信息
    
    Examples:
        >>> # 执行简单命令
        >>> code, output, error = run_cmd("echo 'hello'")
        >>> print(output)
        'hello'
        
        >>> # 执行超时命令
        >>> code, output, error = run_cmd("sleep 10", timeout=1)
        >>> print(code)
        -1
        >>> print(error)
        '命令执行超时'
        
        >>> # 执行错误命令
        >>> code, output, error = run_cmd("invalid_command")
        >>> print(code)
        -1
    
    Notes:
        - 命令通过 shell=True 执行，支持管道、重定向等 shell 特性
        - 超时后会抛出 TimeoutExpired 异常，被捕获后返回 -1
        - 其他异常（如命令不存在）也会被捕获并返回 -1
        - stdout 和 stderr 会自动去除首尾空白字符，如需保留请直接修改代码
    """
    try:
        # 执行 shell 命令，捕获输出和错误信息
        result = subprocess.run(
            cmd,                       # 要执行的命令
            shell=True,                # 使用 shell 执行（支持管道等特性）
            capture_output=True,       # 捕获标准输出和标准错误
            text=True,                 # 以文本模式返回输出（而非字节）
            timeout=timeout            # 设置超时时间
        )
        # 返回执行结果：返回码、去除首尾空白的标准输出、去除首尾空白的标准错误
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    
    except subprocess.TimeoutExpired:
        # 命令执行超过指定时间
        return -1, "", "命令执行超时"
    
    except Exception as e:
        # 其他异常（如命令不存在、权限不足等）
        return -1, "", str(e)


# ========== 可扩展的通用函数 ==========

def log_result(returncode, stdout, stderr, cmd_name=""):
    """
    格式化输出命令执行结果（示例辅助函数）
    
    Args:
        returncode (int): 命令返回码
        stdout (str): 标准输出
        stderr (str): 标准错误
        cmd_name (str): 命令名称（用于日志标识）
    
    Returns:
        str: 格式化后的日志信息
    """
    log_lines = [
        f"[{'成功' if returncode == 0 else '失败'}] 命令: {cmd_name or '未命名'}",
        f"返回码: {returncode}"
    ]
    
    if stdout:
        log_lines.append(f"标准输出: {stdout}")
    if stderr:
        log_lines.append(f"标准错误: {stderr}")
    
    return "\n".join(log_lines)


def is_windows():
    """
    判断当前操作系统是否为 Windows
    
    Returns:
        bool: 如果是 Windows 系统返回 True，否则返回 False
    """
    import platform
    return platform.system().lower() == "windows"


def is_linux():
    """
    判断当前操作系统是否为 Linux
    
    Returns:
        bool: 如果是 Linux 系统返回 True，否则返回 False
    """
    import platform
    return platform.system().lower() == "linux"


def is_macos():
    """
    判断当前操作系统是否为 macOS
    
    Returns:
        bool: 如果是 macOS 系统返回 True，否则返回 False
    """
    import platform
    return platform.system().lower() == "darwin"