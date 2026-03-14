import numpy as np
from scipy.optimize import minimize
import math

def problem4_optimization():
    """
    Problem 4: Optimization Model for Team Cooperation (Extended)
    Objective: Minimize ((35.28*t+3.6*v)/(t*n*cos(q))
    """
    def objective(x):
        t, v, n, q = x
        return ((35.28*t + 3.6*v) / (t*n*np.cos(q)))
    
    def constraints(x):
        t, v, n, q = x
        cons = []
        
        # n = 10 (integer)
        cons.append(n - 10)
        
        # 2*sin(q)*sin(3.14159265359/n) >= 0.3
        cons.append(2*np.sin(q)*np.sin(3.14159265359/n) - 0.3)
        
        # v >= 0.257
        cons.append(v - 0.257)
        
        # (3.33*v-0.56*3.43)/3.87 <= 3.43
        cons.append(3.43 - (3.33*v - 0.56*3.43)/3.87)
        
        # q < 1.57079632679
        cons.append(1.57079632679 - q)
        
        return np.array(cons)
    
    # Initial guess
    x0 = np.array([1.0, 0.5, 10, 1.0])
    
    # Constraints
    cons = {'type': 'ineq', 'fun': constraints}
    
    # Bounds
    bounds = [(0.1, 2.0), (0.257, 2.0), (10, 20), (0.1, 1.5)]
    
    # Solve
    result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
    
    if result.success:
        t, v, n, q = result.x
        n_int = int(round(n))
        
        # Calculate output variables
        F = (35.28*t + 3.6*v) / (t*n_int*np.cos(q))
        D = q * 180 / 3.14159265359
        wqe = ((3.33*v - 1.8522)/3.87)/4.9 + 2*np.sqrt(np.cos(q)/9.8) + t
        G = (3.33*v - 0.56*3.43)/3.87
        
        print("Problem 4 Optimization Results:")
        print(f"Time t: {t:.4f}")
        print(f"Velocity v: {v:.4f}")
        print(f"Number of people n: {n_int}")
        print(f"Angle q: {q:.4f} ({D:.2f}°)")
        print(f"Force F: {F:.4f}")
        print(f"Distance D: {D:.4f}")
        print(f"Height wqe: {wqe:.4f}")
        print(f"Height G: {G:.4f}")
        print(f"Objective function value: {result.fun:.4f}")
        
        return {
            't': t, 'v': v, 'n': n_int, 'q': q,
            'F': F, 'D': D, 'wqe': wqe, 'G': G,
            'objective': result.fun
        }
    else:
        print("Optimization failed:", result.message)
        return None

if __name__ == "__main__":
    problem4_optimization()
