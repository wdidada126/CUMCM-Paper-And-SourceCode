import numpy as np

def Cross(pcross, lenchrom, chrom, sizepop, bound, alps, gams):
    """
    实数编码的交叉算子
    pcross: 交叉概率
    lenchrom: 染色体的长度
    chrom: 染色体种群/种群
    sizepop: 种群规模
    ret: 交叉后的染色体
    """
    for n in range(sizepop):
        while True:
            pick = np.random.rand(2)
            if np.prod(pick) > 0:
                break
        index = np.ceil(pick * sizepop).astype(int) - 1
        
        while True:
            pick = np.random.rand()
            if pick > 0:
                break
        
        if pick > pcross:
            continue
        
        while True:
            while True:
                pick = np.random.rand()
                if pick > 0:
                    break
            pos = np.ceil(pick * lenchrom).astype(int) - 1
            pick = np.random.rand()
            v1 = chrom[index[0], pos]
            v2 = chrom[index[1], pos]
            chrom[index[0], pos] = pick * v2 + (1 - pick) * v1
            chrom[index[1], pos] = pick * v1 + (1 - pick) * v2
            
            flag = [Test(lenchrom, bound, chrom[index[0], :], alps, gams),
                    Test(lenchrom, bound, chrom[index[1], :], alps, gams)]
            if np.prod(flag) > 0:
                break
    
    return chrom
