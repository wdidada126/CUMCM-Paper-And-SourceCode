import numpy as np

def Code(lenchrom, bound, alps, gams):
    """
    产生实数编码的染色体，随机生成一个种群
    lenchrom: 染色体长度
    bound: 变量的取值范围
    ret: 染色体的编码值
    """
    while True:
        pick = np.random.rand(lenchrom)
        ret = bound[:, 0] + (bound[:, 1] - bound[:, 0]) * pick
        flag = Test(lenchrom, bound, ret, alps, gams)
        if flag:
            break
    return ret
