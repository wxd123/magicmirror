# magicm/detector/hardware/gpu/gpu_typer.py

def determine(name):
    """判断显卡类型（独立还是集成）"""
    name_lower = name.lower()
    
    # 集成显卡关键词
    integrated_keywords = ['intel', 'uhd', 'hd graphics', 'iris', 'amd radeon(tm) graphics', 'radeon(tm) graphics']
    # 独立显卡关键词
    discrete_keywords = ['nvidia', 'geforce', 'rtx', 'gtx', 'quadro', 'tesla', 'amd radeon rx', 'radeon rx', 'amd radeon pro']
    
    for keyword in integrated_keywords:
        if keyword in name_lower:
            return 'integrated'
    
    for keyword in discrete_keywords:
        if keyword in name_lower:
            return 'discrete'
    
    # 默认：如果包含显卡相关词但无法判断，根据常见规则
    if 'amd' in name_lower:
        # AMD的APU通常是集成的，RX系列是独立的
        if 'rx' in name_lower:
            return 'discrete'
        return 'integrated'
    
    return 'unknown'