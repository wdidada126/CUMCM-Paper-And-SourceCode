import numpy as np

def Fun(x):
    """
    计算适应度函数
    """
    y = 60000.0 / (2750.0 * x[-2] * x[-1])
    return y
