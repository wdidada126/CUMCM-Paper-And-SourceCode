import numpy as np

def Select(individuals, fitness, sizepop):
    """
    对每一代种群中的染色体进行选择操作，得到新的种群和适应度
    individuals: 种群信息
    fitness: 适应度
    sizepop: 种群规模
    ret: 选择后的种群
    """
    sumfitness = np.sum(fitness)
    sumf = fitness / sumfitness
    index = np.zeros(sizepop, dtype=int)
    
    for n in range(sizepop):
        while True:
            pick = np.random.rand()
            if pick > 0:
                break
        
        for m in range(sizepop):
            pick = pick - sumf[m]
            if pick < 0:
                index[n] = m
                break
    
    individuals = individuals[index, :]
    fitness = fitness[index]
    ret = individuals
    
    return ret, fitness
