import numpy as np
from Code import Code
from Fun import Fun
from Cross import Cross
from Mutation import Mutation
from Select import Select
from E_show import E_show

def GA(alps, gams):
    """
    遗传算法主函数
    """
    popsize = 5
    lenchrom = 58
    maxgen = 10
    
    pc = 0.7
    pm = 0.5
    
    bound = np.tile([100, 350], (55, 1))
    bound = np.vstack([bound, [2, 8], [2, 8], [2, 6]])
    
    GApop = np.zeros((popsize, lenchrom))
    fitness = np.zeros(popsize)
    
    for n in range(popsize):
        GApop[n, :] = Code(lenchrom, bound, alps, gams)
        fitness[n] = Fun(GApop[n, :])
    
    bestfitness = np.max(fitness)
    bestindex = np.argmax(fitness)
    zbest = GApop[bestindex, :]
    fitnesszbest = bestfitness
    y = np.zeros(maxgen)
    
    for n in range(maxgen):
        GApop, fitness = Select(GApop, fitness, popsize)
        GApop = Cross(pc, lenchrom, GApop, popsize, bound, alps, gams)
        GApop = Mutation(pm, lenchrom, GApop, popsize, [n+1, maxgen], bound, alps, gams)
        
        print(n)
        
        for m in range(popsize):
            fitness[m] = Fun(GApop[m, :])
            if fitness[m] > fitnesszbest:
                zbest = GApop[m, :]
                fitnesszbest = fitness[m]
        
        y[n] = fitnesszbest
    
    y = y[-1]
    E = E_show(lenchrom, bound, zbest, alps, gams)
    
    return zbest, y, E
