def convert_size(size_bytes):
    """将字节转换为可读格式 (KB, MB, GB)"""
    for unit in ['B', 'KB', 'MB', 'GB','TB','PB','EB','ZB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} YB"
def to_bytes(value, unit):
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024**2,
        'GB': 1024**3,
        'TB': 1024**4,
        'PB': 1024**5,
        'EB': 1024**6,
        'ZB': 1024**7,
        'YB': 1024**8
    }
    
    unit = unit.upper()  # 处理大小写不敏感
    if unit not in units:
        raise Panic("to_bytes","incorrunt unit.",4,"typeerror")
    
    return value * units[unit]
a=1048576
print(convert_size(a))
print(to_bytes(1,"MB"))