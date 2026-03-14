import numpy as np
from scipy.optimize import minimize
import math

def problem1_optimization():
    """
    Problem 1: Optimization Model for Team Cooperation
    Objective: Minimize ((35.28*t+3.6*v)/(t*n*cos(q))*(tan(q)*v*t/2)
    """
    def objective(x):
        t, v, n, q = x
        return ((35.28*t + 3.6*v) / (t*n*np.cos(q))) * (np.tan(q)*v*t/2)
    
    def constraints(x):
        t, v, n, q = x
        cons = []
        
        # n >= 8 (integer)
        cons.append(n - 8)
        
        # v*t <= 2
        cons.append(2 - v*t)
        
        # (0.5*(v/t)*(t^2)*tan(q))*sin(3.14159265359/n) >= 0.3
        cons.append((0.5*(v/t)*(t**2)*np.tan(q))*np.sin(3.14159265359/n) - 0.3)
        
        # v >= 0.21
        cons.append(v - 0.21)
        
        # (3.33*v-0.56*2.8)/3.87 <= 2.8
        cons.append(2.8 - (3.33*v - 0.56*2.8)/3.87)
        
        # q < 1.57079632679
        cons.append(1.57079632679 - q)
        
        return np.array(cons)
    
    # Initial guess
    x0 = np.array([1.0, 0.5, 8, 1.0])
    
    # Constraints
    cons = {'type': 'ineq', 'fun': constraints}
    
    # Bounds
    bounds = [(0.1, 2.0), (0.21, 2.0), (8, 20), (0.1, 1.5)]
    
    # Solve
    result = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)
    
    if result.success:
        t, v, n, q = result.x
        n_int = int(round(n))
        
        # Calculate output variables
        R = np.tan(q)*v*t/2
        F = (35.28*t + 3.6*v) / (t*n_int*np.cos(q))
        D = q * 180 / 3.14159265359
        wqe = ((3.33*v - 0.56*2.8)/3.87)/4.9 + np.sqrt(v*t/9.8)
        G = (3.33*v - 0.56*2.8)/3.87
        
        print("Problem 1 Optimization Results:")
        print(f"Time t: {t:.4f}")
        print(f"Velocity v: {v:.4f}")
        print(f"Number of people n: {n_int}")
        print(f"Angle q: {q:.4f} ({D:.2f}°)")
        print(f"Radius R: {R:.4f}")
        print(f"Force F: {F:.4f}")
        print(f"Distance D: {D:.4f}")
        print(f"Height wqe: {wqe:.4f}")
        print(f"Height G: {G:.4f}")
        print(f"Objective function value: {result.fun:.4f}")
        
        return {
            't': t, 'v': v, 'n': n_int, 'q': q,
            'R': R, 'F': F, 'D': D, 'wqe': wqe, 'G': G,
            'objective': result.fun
        }
    else:
        print("Optimization failed:", result.message)
        return None

if __name__ == "__main__":
    problem1_optimization()
