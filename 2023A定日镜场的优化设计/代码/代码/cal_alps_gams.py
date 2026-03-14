import numpy as np

def cal_alps_gams(D, phi, ST):
    """
    alps 太阳高度角
    gams 太阳方位角
    D 为以春分作为第 0 天起算的天数，例如， 若春分是 3 月 21 日，则 4 月 1 日对应 D = 11
    ST 为当地时间
    del 太阳赤纬角
    phi 当地纬度 北纬为正
    ome 太阳时角
    """
    ome = (np.pi/12) * (ST - 12)
    del_val = np.arcsin(np.sin(2*np.pi*D/365) * np.sin(2*np.pi*23.45/365))
    alps = np.arcsin(np.cos(del_val) * np.cos(phi) * np.cos(ome) + np.sin(del_val) * np.sin(phi))
    
    # 避免除以零和数值超出范围的情况
    denominator = np.cos(alps) * np.cos(phi)
    if abs(denominator) > 1e-10:
        numerator = (np.sin(del_val) - np.sin(alps) * np.sin(phi))
        ratio = numerator / denominator
        # 限制ratio在[-1, 1]范围内
        ratio = max(-1.0, min(1.0, ratio))
        gams = np.arccos(ratio)
    else:
        gams = 0
    
    return alps, gams
