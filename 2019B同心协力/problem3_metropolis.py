import numpy as np
import random

def PathLength(Route, X):
    """
    Calculate the length of a path
    Route: path sequence (0-indexed)
    X: position array
    """
    tan45 = np.sqrt(2) / 2
    n = np.zeros(len(Route))
    
    for i in range(len(Route)):
        if i == 0:
            n[0] = X[Route[0]] + tan45 * X[Route[7]] + tan45 * X[Route[1]]
        elif i == 7:
            n[7] = tan45 * X[Route[0]] + X[Route[7]] + tan45 * X[Route[6]]
        else:
            n[i] = X[Route[i]] + tan45 * X[Route[i+1]] + tan45 * X[Route[i-1]]
    
    Length = abs(n[0] - n[4]) + abs(n[1] - n[5]) + abs(n[2] - n[6]) + abs(n[3] - n[7])
    return Length

def NewAnswer(S1):
    """
    Generate a new answer by swapping two positions
    S1: current solution (0-indexed)
    """
    N = len(S1)
    S2 = S1.copy()
    a = np.random.randint(0, N, size=2)
    W = S2[a[0]]
    S2[a[0]] = S2[a[1]]
    S2[a[1]] = W
    return S2

def Metropolis(S1, S2, X, T):
    """
    Metropolis algorithm for path optimization
    S1: current solution
    S2: new solution
    X: position array
    T: temperature
    """
    R1 = PathLength(S1, X)
    R2 = PathLength(S2, X)
    
    dC = R2 - R1  # difference in cost
    
    if dC < 0:  # if new solution is better
        S = S2
        R = R2
    elif np.exp(-dC / T) >= np.random.rand():  # accept with probability
        S = S2
        R = R2
    else:  # keep current solution
        S = S1
        R = R1
    
    return S, R

def problem3_metropolis(X, initial_temp=100, cooling_rate=0.95, iterations=1000):
    """
    Problem 3: Path optimization using Metropolis algorithm
    X: position array
    initial_temp: initial temperature
    cooling_rate: cooling rate
    iterations: number of iterations
    """
    # Initialize with a random path (0-indexed)
    N = len(X)
    S1 = np.arange(N)
    np.random.shuffle(S1)
    
    T = initial_temp
    best_S = S1.copy()
    best_R = PathLength(S1, X)
    
    print("Problem 3: Path Optimization using Metropolis Algorithm")
    print("=" * 60)
    
    for i in range(iterations):
        # Generate new solution
        S2 = NewAnswer(S1)
        
        # Apply Metropolis criterion
        S1, R1 = Metropolis(S1, S2, X, T)
        
        # Update best solution
        if R1 < best_R:
            best_S = S1.copy()
            best_R = R1
        
        # Cool down
        T *= cooling_rate
        
        if i % 100 == 0:
            print(f"Iteration {i}: Temperature = {T:.4f}, Best Length = {best_R:.4f}")
    
    print("\nFinal Results:")
    print(f"Best path: {best_S}")
    print(f"Best length: {best_R:.4f}")
    
    return best_S, best_R

if __name__ == "__main__":
    # Example position array (8 positions)
    X = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    
    # Run Metropolis algorithm
    best_path, best_length = problem3_metropolis(X)
    
    print(f"\nOptimized path length: {best_length:.4f}")
