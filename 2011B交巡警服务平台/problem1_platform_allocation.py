import numpy as np

def floyd(a):
    n = len(a)
    D = a.copy()
    R = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        for j in range(n):
            R[i, j] = j
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i, k] + D[k, j] < D[i, j]:
                    D[i, j] = D[i, k] + D[k, j]
                    R[i, j] = R[i, k]
    
    return D, R