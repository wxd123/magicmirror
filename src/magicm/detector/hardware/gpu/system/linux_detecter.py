# magicm/detector/hardware/gpu/system/linux_detecter.py

import re
import math
from magicm.utils.util import run_cmd

def _extract_gpu_name(line):
    """从 lspci 输出中提取干净的 GPU 名称"""
    # 移除前面的 PCI 地址和设备类型
    # 示例: "01:00.0 VGA compatible controller: NVIDIA Corporation GA102 [GeForce RTX 3080] (rev a1)"
    # 提取: "NVIDIA GeForce RTX 3080"
    
    # 方法1: 提取 [xxx] 中的内容
    bracket_match = re.search(r'\[([^\]]+)\]', line)
    if bracket_match:
        return bracket_match.group(1).strip()
    
    # 方法2: 提取 "controller: " 之后的内容
    if 'controller:' in line:
        parts = line.split('controller:', 1)
        if len(parts) > 1:
            name = parts[1].strip()
            # 移除括号内容
            name = re.sub(r'\([^)]*\)', '', name).strip()
            return name
    
    # 方法3: 提取 "3D controller:" 之后的内容
    if '3D controller:' in line:
        parts = line.split('3D controller:', 1)
        if len(parts) > 1:
            name = parts[1].strip()
            name = re.sub(r'\([^)]*\)', '', name).strip()
            return name
    
    # 方法4: 清理原始行
    # 移除 PCI 地址
    cleaned = re.sub(r'^[0-9a-f]{2}:[0-9a-f]{2}\.[0-9a-f]\s+', '', line)
    # 移除设备类型
    cleaned = re.sub(r'(VGA compatible controller|3D controller|Display controller):\s*', '', cleaned)
    # 移除括号内容
    cleaned = re.sub(r'\([^)]*\)', '', cleaned)
    
    return cleaned.strip()


def _get_gpu_memory(gpu_name, gpu_raw_line=None):
    """获取 GPU 显存大小（GB）"""
    
    # 方法1: 尝试使用 nvidia-smi（适用于所有 NVIDIA GPU）
    try:
        # 先检查 nvidia-smi 是否可用
        rc_check, _, _ = run_cmd('which nvidia-smi 2>/dev/null')
        if rc_check == 0:
            # 尝试获取显存大小
            rc, out, err = run_cmd('nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits 2>/dev/null')
            if rc == 0 and out and out.strip():
                memory_mb_str = out.strip().split('\n')[0].strip()
                if memory_mb_str:
                    memory_mb = int(memory_mb_str)
                    memory_gb = math.ceil(memory_mb / 1024)
                    return memory_gb
    except Exception as e:
        pass
    
    # 方法2: 从原始 lspci 行中判断是否是 NVIDIA
    if gpu_raw_line and ('nvidia' in gpu_raw_line.lower()):
        # 这是 NVIDIA GPU，但 nvidia-smi 可能失败了
        # 可以尝试其他方法或返回默认值
        pass
    
    # 方法3: 从 glxinfo 获取（开源驱动）
    try:
        rc, out, _ = run_cmd('glxinfo 2>/dev/null | grep "Video memory"')
        if rc == 0 and out:
            match = re.search(r'(\d+)\s*MB', out)
            if match:
                memory_mb = int(match.group(1))
                return memory_mb // 1024
    except:
        pass
    
    # 方法4: 从 /sys/class/drm/ 获取（AMD GPU）
    try:
        import glob
        for card in glob.glob('/sys/class/drm/card[0-9]*/device/mem_info_vram_total'):
            try:
                with open(card, 'r') as f:
                    total_bytes = int(f.read().strip())
                    total_gb = total_bytes // (1024 * 1024 * 1024)
                    if total_gb > 0:
                        return total_gb
            except:
                pass
    except:
        pass
    
    return None

def detect():
    """Linux系统GPU检测 - 增强版"""
    info = {
        'gpu_present': False,
        'discrete_gpu': None,
        'integrated_gpu': None,
        'all_gpus': [],
        'gpu_name': None,
        'driver_version': None
    }
    
    try:
        # 使用 lspci 检测所有 GPU
        rc, out, _ = run_cmd('lspci | grep -E "VGA|3D|Display"')
        if rc == 0 and out.strip():
            lines = out.strip().split('\n')
            
            for line in lines:
                if not line.strip():
                    continue
                
                # 提取干净的 GPU 名称
                gpu_name = _extract_gpu_name(line)
                if not gpu_name:
                    gpu_name = line.strip()
                
                gpu_info = {
                    'name': gpu_name,
                    'raw': line.strip(),
                    'type': 'unknown',
                    'memory_gb': None
                }
                
                # 判断显卡类型和品牌
                line_lower = line.lower()
                name_lower = gpu_name.lower()
                
                # NVIDIA - 通常是独立显卡
                if 'nvidia' in line_lower or 'nvidia' in name_lower:
                    gpu_info['type'] = 'discrete'
                    info['discrete_gpu'] = gpu_name
                    info['gpu_name'] = gpu_name
                    # 获取驱动版本
                    rc, out, _ = run_cmd('nvidia-smi --query-gpu=driver_version --format=csv,noheader 2>/dev/null')
                    if rc == 0 and out.strip():
                        info['driver_version'] = out.strip().split('\n')[0]
                
                # Intel - 通常是集成显卡
                elif 'intel' in line_lower or 'intel' in name_lower:
                    gpu_info['type'] = 'integrated'
                    info['integrated_gpu'] = gpu_name
                    if not info['gpu_name']:
                        info['gpu_name'] = gpu_name
                
                # AMD
                elif 'amd' in line_lower or 'radeon' in line_lower or 'amd' in name_lower:
                    # 需要进一步判断是独立还是集成
                    # AMD APU 通常是集成，Ryzen 系列需要判断
                    if any(x in line_lower for x in ['radeon graphics', 'vega', 'renoir', 'cezanne']):
                        gpu_info['type'] = 'integrated'
                        info['integrated_gpu'] = gpu_name
                    else:
                        gpu_info['type'] = 'discrete'
                        info['discrete_gpu'] = gpu_name
                        info['gpu_name'] = gpu_name
                    
                    # 获取 AMD 驱动版本
                    rc, out, _ = run_cmd('modinfo amdgpu 2>/dev/null | grep "^version:"')
                    if rc == 0 and out.strip():
                        version_match = re.search(r'version:\s*(.+)', out)
                        if version_match:
                            info['driver_version'] = version_match.group(1).strip()
                
                # 其他（可能是虚拟 GPU）
                else:
                    if 'virtual' in line_lower or 'vmware' in line_lower:
                        gpu_info['type'] = 'virtual'
                        info['gpu_name'] = gpu_name
                
                # 获取显存大小
                gpu_info['memory_gb'] = _get_gpu_memory(gpu_name, line)
                info['all_gpus'].append(gpu_info)
            
            # 设置 gpu_present
            info['gpu_present'] = len(info['all_gpus']) > 0
            
            # 如果没有检测到独立显卡但有集成显卡，设置 gpu_name 为集成显卡
            if not info['gpu_name'] and info['integrated_gpu']:
                info['gpu_name'] = info['integrated_gpu']
            
            # 如果没有设置 gpu_name 但有 GPU，使用第一个 GPU
            if not info['gpu_name'] and info['all_gpus']:
                info['gpu_name'] = info['all_gpus'][0]['name']
    
    except Exception as e:
        print(f"Linux GPU 检测出错: {e}")
    
    return info