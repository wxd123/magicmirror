# magicm/detector/hardware/gpu/system/mac_detecter.py
from magicm.utils.util import run_cmd
def detect():
    """macOS系统GPU检测"""
    info = {
        'gpu_present': False,
        'discrete_gpu': None,
        'integrated_gpu': None,
        'all_gpus': []
    }
    
    try:
        rc, out, _ = run_cmd('system_profiler SPDisplaysDataType')
        if rc == 0:
            lines = out.split('\n')
            current_gpu = {}
            for line in lines:
                if 'Chipset Model:' in line:
                    if current_gpu:
                        info['all_gpus'].append(current_gpu)
                    gpu_name = line.split(':', 1)[1].strip()
                    current_gpu = {'name': gpu_name}
                    
                    if 'intel' in gpu_name.lower():
                        current_gpu['type'] = 'integrated'
                        info['integrated_gpu'] = gpu_name
                    else:
                        current_gpu['type'] = 'discrete'
                        info['discrete_gpu'] = gpu_name
            
            if current_gpu:
                info['all_gpus'].append(current_gpu)
    except:
        pass
    
    return info
