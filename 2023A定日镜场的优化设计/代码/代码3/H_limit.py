import numpy as np

def H_limit(ret, lenchrom):
    """
    检查高度限制约束
    """
    count = 0
    for i in range(lenchrom // 4):
        if ret[2 * (i - 1) + lenchrom + 1] <= 2 * ret[lenchrom * 3 // 4 + i]:
            count += 1
    
    if count == 55:
        flag = 1
    else:
        flag = 0
    
    return flag
