# magicm/detector/hardware/gpu/system/win_detecter.py

from magicm.utils.util import run_cmd
from ..gpu_typer import determine as determine_gpu_type
from ..nvidia_detecter import nvidia_gpu_name, cuda_version, nvidia_driver
def detect():
    """Windows系统GPU检测（独立+集成）"""
    info = {
        'gpu_present': False,
        'discrete_gpu': None,
        'integrated_gpu': None,
        'driver_version': None,
        'cuda_supported_by_driver': None,
        'gpu_name': None,
        'all_gpus': []
    }
    
    # 方法1: 使用wmic获取所有显示适配器
    try:
        rc, out, _ = run_cmd('wmic path win32_videocontroller get name,adapterram,driverversion /format:csv')
        if rc == 0:
            lines = out.strip().split('\n')
            for line in lines[1:]:  # 跳过标题行
                if line.strip() and ',' in line:
                    parts = line.split(',')
                    if len(parts) >= 3:
                        # CSV格式: Node,DriverVersion,Name,AdapterRAM
                        # 根据实际输出调整索引
                        gpu_info = {}
                        
                        # 尝试找到名称
                        for part in parts:
                            if any(x in part.lower() for x in ['nvidia', 'amd', 'radeon', 'intel', 'geforce', 'rtx', 'gtx', 'iris', 'uhd', 'hd graphics']):
                                gpu_info['name'] = part.strip()
                                break
                        
                        if 'name' in gpu_info:
                            # 判断显卡类型
                            gpu_info['type'] = determine_gpu_type(gpu_info['name'])
                            
                            # 提取显存
                            for part in parts:
                                if part.strip().isdigit():
                                    ram_bytes = int(part.strip())
                                    if ram_bytes > 0:
                                        ram_mb = ram_bytes / (1024 * 1024)
                                        gpu_info['memory'] = f"{ram_mb:.0f} MB"
                            
                            info['all_gpus'].append(gpu_info)
                            
                            # 分别记录独立和集成显卡
                            if gpu_info['type'] == 'discrete':
                                info['discrete_gpu'] = gpu_info['name']
                            else:
                                info['integrated_gpu'] = gpu_info['name']
    except Exception as e:
        print(f"wmic显卡检测失败: {e}")
    
    # 方法2: 使用PowerShell获取详细信息
    if not info['all_gpus']:
        try:
            ps_cmd = 'powershell -command "Get-WmiObject -Class Win32_VideoController | Select-Object Name, AdapterRAM, DriverVersion, VideoProcessor | ConvertTo-Csv -NoTypeInformation"'
            rc, out, _ = run_cmd(ps_cmd)
            if rc == 0:
                lines = out.strip().split('\n')
                for line in lines[1:]:
                    if line.strip() and ',' in line:
                        parts = line.strip('"').split('","')
                        if len(parts) >= 1 and parts[0].strip():
                            gpu_info = {'name': parts[0].strip()}
                            
                            # 判断显卡类型
                            gpu_info['type'] = determine_gpu_type(gpu_info['name'])
                            
                            # 获取显存
                            if len(parts) >= 2 and parts[1].strip().isdigit():
                                ram_bytes = int(parts[1].strip())
                                if ram_bytes > 0:
                                    ram_mb = ram_bytes / (1024 * 1024)
                                    gpu_info['memory'] = f"{ram_mb:.0f} MB"
                            
                            info['all_gpus'].append(gpu_info)
                            
                            if gpu_info['type'] == 'discrete':
                                info['discrete_gpu'] = gpu_info['name']
                            else:
                                info['integrated_gpu'] = gpu_info['name']
        except Exception as e:
            print(f"PowerShell显卡检测失败: {e}")
    
    # 方法3: 使用nvidia-smi检测NVIDIA显卡（独立显卡）
    try:
        rc, out, _ = run_cmd('nvidia-smi')
        if rc == 0:
            info['driver_version'] = nvidia_driver(out)
            info['cuda_supported_by_driver'] = cuda_version(out)
            
            # 获取NVIDIA显卡名称
            nvidia_name = nvidia_gpu_name(out)
            if nvidia_name:
                # 检查是否已经添加过
                nvidia_exists = False
                for gpu in info['all_gpus']:
                    if 'nvidia' in gpu['name'].lower():
                        nvidia_exists = True
                        break
                
                if not nvidia_exists:
                    info['all_gpus'].append({
                        'name': nvidia_name,
                        'type': 'discrete',
                        'driver': info['driver_version']
                    })
                    info['discrete_gpu'] = nvidia_name
    except:
        pass
    
    return info
