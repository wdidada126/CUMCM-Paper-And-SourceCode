import numpy as np

def E_limit(lenchrom, bound, ret, alps, gams):
    """
    lenchrom: 染色体长度
    bound: 变量的取值范围
    code: 染色体的编码值
    flag: 可行性标志变量
    """
    flag = 0
    eta_cos = 0
    DNI_ave = 0.9686
    eta_sb = 0.95
    eta_ref = 0.92
    
    for i in range(55):
        eta_at = (0.99321 - 0.000176 * np.sqrt(ret[i]**2 + (ret[-1] - 80)**2) + 
                  0.0000000197 * (ret[i]**2 + (ret[-1] - 80)**2))
        
        for j in range(12):
            for k in range(5):
                inline = np.array([-np.cos(alps[j, k]) * np.sin(gams[j, k]),
                                   -np.cos(alps[j, k]) * np.cos(gams[j, k]),
                                   -np.sin(alps[j, k])])
                outline = np.array([0, 0, ret[-1] - 80])
                eta_cos += (25 + 25 * np.dot(inline, outline) / 
                           np.sqrt(ret[i]**2 + (ret[-1] - 80)**2))
        
        eta[i] = eta_at * eta_cos * eta_sb * eta_ref / 60
        eta_cos = 0
    
    eta_ave = np.sum(eta) / 55
    E = eta_ave * DNI_ave * 55 * ret[-2] * ret[-1]
    
    if E < 62000 and E > 59000:
        flag = 1
    
    return flag
