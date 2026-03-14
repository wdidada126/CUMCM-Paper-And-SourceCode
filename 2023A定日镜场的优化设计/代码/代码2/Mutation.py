import numpy as np

def Mutation(pmutation, lenchrom, chrom, sizepop, pop, bound, alps, gams):
    """
    实数编码的变异算子
    pmutation: 变异概率
    lenchrom: 染色体长度
    chrom: 染色体种群
    sizepop: 种群规模
    pop: 当前种群进化的代数和最大进化代数的信息
    ret: 变异后的染色体
    """
    for n in range(sizepop):
        while True:
            pick = np.random.rand()
            if pick > 0:
                break
        index = np.ceil(pick * sizepop).astype(int) - 1
        
        pick = np.random.rand()
        if pick > pmutation:
            continue
        
        while True:
            while True:
                pick = np.random.rand()
                if pick > 0:
                    break
            pos = np.ceil(pick * lenchrom).astype(int) - 1
            v = chrom[n, pos]
            v1 = v - bound[pos, 0]
            v2 = bound[pos, 1] - v
            pick = np.random.rand()
            
            if pick > 0.5:
                delta = v2 * (1 - pick ** ((1 - pop[0] / pop[1]) ** 2))
                chrom[index, pos] = v + delta
            else:
                delta = v1 * (1 - pick ** ((1 - pop[0] / pop[1]) ** 2))
                chrom[index, pos] = v - delta
            
            if Test(lenchrom, bound, chrom[n, :], alps, gams):
                break
    
    return chrom
