import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
import random

def problem3_parameter_optimization():
    """
    Problem 3: Parameter Optimization using PSO
    参数优化 - 使用粒子群优化算法
    """
    L = 50 + 30.5*11 + 5*10
    alpha = 7.15e-04
    H1 = 6975.37
    H2 = 97.60
    xm = np.array([alpha, H1, alpha, H1, alpha, H1, alpha, H1, alpha, H2])
    
    # PSO参数
    pop_size = 60
    w = 0.8
    c1 = 2
    c2 = 2
    max_iter = 1000
    dim = 5
    
    # 搜索空间
    upper_bound = np.array([185, 205, 245, 265, 10/6])
    lower_bound = np.array([165, 185, 225, 245, 65/60])
    
    # 初始化粒子群
    particles = np.random.uniform(lower_bound, upper_bound, (pop_size, dim))
    velocities = np.random.uniform(-1, 1, (pop_size, dim))
    personal_best = particles.copy()
    personal_best_fitness = np.array([objective_function(p, xm, L) for p in particles])
    global_best_idx = np.argmin(personal_best_fitness)
    global_best = personal_best[global_best_idx].copy()
    
    print("Problem 3: Parameter Optimization using PSO")
    print("=" * 60)
    print(f"Population size: {pop_size}")
    print(f"Max iterations: {max_iter}")
    
    # PSO主循环
    for iteration in range(max_iter):
        for i in range(pop_size):
            # 更新速度
            r1 = random.random()
            r2 = random.random()
            velocities[i] = (w * velocities[i] + 
                            c1 * r1 * (personal_best[i] - particles[i]) + 
                            c2 * r2 * (global_best - particles[i]))
            
            # 更新位置
            particles[i] = particles[i] + velocities[i]
            
            # 边界处理
            particles[i] = np.clip(particles[i], lower_bound, upper_bound)
            
            # 计算适应度
            fitness = objective_function(particles[i], xm, L)
            
            # 更新个体最优
            if fitness < personal_best_fitness[i]:
                personal_best[i] = particles[i].copy()
                personal_best_fitness[i] = fitness
                
                # 更新全局最优
                if fitness < personal_best_fitness[global_best_idx]:
                    global_best_idx = i
                    global_best = particles[i].copy()
        
        if iteration % 100 == 0:
            print(f"Iteration {iteration}: Best fitness = {personal_best_fitness[global_best_idx]:.4f}")
    
    # 最优解
    F = np.array([25, global_best[0], global_best[1], global_best[2], global_best[3], 25])
    v = global_best[4]
    T = L/v
    
    print(f"\nOptimal parameters:")
    print(f"F2: {global_best[0]:.2f} °C")
    print(f"F3: {global_best[1]:.2f} °C")
    print(f"F4: {global_best[2]:.2f} °C")
    print(f"F5: {global_best[3]:.2f} °C")
    print(f"Velocity: {v*60:.2f} cm/min")
    print(f"Best fitness: {personal_best_fitness[global_best_idx]:.4f}")
    
    # 绘制最优温度曲线
    u0 = heat(global_best[0], global_best[1], global_best[2], global_best[3], v, xm, L, F)
    t = np.arange(0, T + 0.5, 0.5)
    k = np.argmax(u0)
    
    plt.figure(figsize=(12, 6))
    plt.plot(t, u0, 'b-', linewidth=2, label='Temperature')
    plt.plot(t, 217 * np.ones(len(t)), 'r-', linewidth=1.5, label='217°C')
    plt.axvline(x=t[k], color='g', linewidth=1.5, linestyle='--', label='Max Temp')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.title('Optimized Furnace Temperature Curve')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return global_best, personal_best_fitness[global_best_idx]

def objective_function(x, xm, L):
    """
    目标函数：计算温度曲线在217℃以上的面积
    """
    u0 = heat(x[0], x[1], x[2], x[3], x[4], xm, L)
    u = u0[u0 >= 30]
    
    # 温度大于217的部分
    tmp2 = u[u >= 217] - 217
    t2 = len(tmp2) * 0.5
    TMax = np.max(u)
    tmp3 = np.abs(u[1:] - u[:-1]) / 0.5
    KMax = np.max(tmp3)
    rising_mask = np.zeros_like(u, dtype=bool)
    rising_mask[1:] = u[1:] >= u[:-1]
    s = u[rising_mask]
    s = s[s >= 150]
    s = s[s <= 190]
    t1 = len(s) * 0.5
    
    # 检查约束条件
    y = (TMax <= 250) and (TMax >= 240) and (t2 >= 40) and (t2 <= 90) and (KMax <= 3) and (t1 <= 120) and (t1 >= 60)
    
    if y:
        k = np.argmax(tmp2)
        if k > 2:
            a = (np.sum(tmp2[:k]) - (tmp2[0] + tmp2[k]) / 2) * 0.5
        else:
            a = (tmp2[0] + tmp2[k]) * 0.5 / 2
        return -a  # 最大化面积，所以取负值
    else:
        return float('inf')

def f(x, F):
    """
    External temperature distribution function
    """
    l = 5
    L = 30.5
    s = 25
    x1 = 0
    x2 = 25
    x3 = x2 + 5*L + 4*l
    x4 = x3 + l
    x5 = x4 + L
    x6 = x5 + l
    x7 = x6 + L
    x8 = x7 + l
    x9 = x8 + 2*L + l
    x10 = x9 + l
    
    y = np.zeros_like(x)
    y = np.where(x <= x2, np.exp(0.2007*x) + 24, y)
    y = np.where((x > x2) & (x <= x3), F[1], y)
    y = np.where((x > x3) & (x <= x4), (F[2]-F[1])/l*(x-x3) + F[1], y)
    y = np.where((x > x4) & (x <= x5), F[2], y)
    y = np.where((x > x5) & (x <= x6), (F[3]-F[2])/l*(x-x5) + F[2], y)
    y = np.where((x > x6) & (x <= x7), F[3], y)
    y = np.where((x > x7) & (x <= x8), (F[4]-F[3])/l*(x-x7) + F[3], y)
    y = np.where((x > x8) & (x <= x9), F[4], y)
    y = np.where((x > x9) & (x <= x10), (F[5]-F[4])/l*(x-x9) + F[4], y)
    y = np.where(x > x10, F[5], y)
    
    return y

def heat(u1, u2, u3, u4, v, xm, L, F=None):
    """
    Heat conduction equation solver
    """
    if F is None:
        F = np.array([25, u1, u2, u3, u4, 25])
    T = L/v
    
    L1 = 25 + 5*30.5 + 5*5
    L2 = L1 + 30.5 + 5
    L3 = L2 + 30.5 + 5
    t1 = L1/v
    t2 = L2/v
    t3 = L3/v
    dt = 0.5
    m1 = int(np.floor(t1/dt)) + 1
    m2 = int(np.floor(t2/dt)) + 1
    m3 = int(np.floor(t3/dt)) + 1
    
    l = 0.015
    x = 1e-4
    q1 = xm[0]**2 * dt / (x**2)
    q2 = xm[2]**2 * dt / (x**2)
    q3 = xm[4]**2 * dt / (x**2)
    q4 = xm[6]**2 * dt / (x**2)
    q5 = xm[8]**2 * dt / (x**2)
    h1 = xm[1]
    h2 = xm[3]
    h3 = xm[5]
    h4 = xm[7]
    h5 = xm[9]
    
    n = int(np.ceil(l/x)) + 1
    m = int(np.floor(T/dt)) + 1
    u = np.zeros((n, m))
    t = np.ones(m) * 25
    u[:, 0] = 25
    u0 = f(v * np.arange(0, int(np.floor(T/dt)) + 1) * dt, F)
    k = int(np.ceil(l/2/x))
    
    # Zone 1
    A1 = np.diag([1 + h1*x] + [2*(1+q1)]*(n-2) + [1 + h1*x])
    A1 += np.diag([-1] + [-q1]*(n-2), 1)
    A1 += np.diag([-q1]*(n-2) + [-1], -1)
    B1 = np.diag([0] + [2*(1-q1)]*(n-2) + [0])
    B1 += np.diag([0] + [q1]*(n-2), 1)
    B1 += np.diag([q1]*(n-2) + [0], -1)
    C1 = solve(A1, B1)
    c = np.zeros((n, m))
    c[0, :] = h1 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A1, c)
    
    for j in range(m1-1):
        u[:, j+1] = C1 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 2
    A2 = np.diag([1 + h2*x] + [2*(1+q2)]*(n-2) + [1 + h2*x])
    A2 += np.diag([-1] + [-q2]*(n-2), 1)
    A2 += np.diag([-q2]*(n-2) + [-1], -1)
    B2 = np.diag([0] + [2*(1-q2)]*(n-2) + [0])
    B2 += np.diag([0] + [q2]*(n-2), 1)
    B2 += np.diag([q2]*(n-2) + [0], -1)
    C2 = solve(A2, B2)
    c = np.zeros((n, m))
    c[0, :] = h2 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A2, c)
    
    for j in range(m1, m2-1):
        u[:, j+1] = C2 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 3
    A3 = np.diag([1 + h3*x] + [2*(1+q3)]*(n-2) + [1 + h3*x])
    A3 += np.diag([-1] + [-q3]*(n-2), 1)
    A3 += np.diag([-q3]*(n-2) + [-1], -1)
    B3 = np.diag([0] + [2*(1-q3)]*(n-2) + [0])
    B3 += np.diag([0] + [q3]*(n-2), 1)
    B3 += np.diag([q3]*(n-2) + [0], -1)
    C3 = solve(A3, B3)
    c = np.zeros((n, m))
    c[0, :] = h3 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A3, c)
    
    for j in range(m2, m3-1):
        u[:, j+1] = C3 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 4 and 5
    A4 = np.diag([1 + h4*x] + [2*(1+q4)]*(n-2) + [1 + h4*x])
    A4 += np.diag([-1] + [-q4]*(n-2), 1)
    A4 += np.diag([-q4]*(n-2) + [-1], -1)
    B4 = np.diag([0] + [2*(1-q4)]*(n-2) + [0])
    B4 += np.diag([0] + [q4]*(n-2), 1)
    B4 += np.diag([q4]*(n-2) + [0], -1)
    C4 = solve(A4, B4)
    c4 = np.zeros((n, m))
    c4[0, :] = h4 * u0 * x
    c4[-1, :] = c4[0, :]
    c4 = solve(A4, c4)
    
    A5 = np.diag([1 + h5*x] + [2*(1+q5)]*(n-2) + [1 + h5*x])
    A5 += np.diag([-1] + [-q5]*(n-2), 1)
    A5 += np.diag([-q5]*(n-2) + [-1], -1)
    B5 = np.diag([0] + [2*(1-q5)]*(n-2) + [0])
    B5 += np.diag([0] + [q5]*(n-2), 1)
    B5 += np.diag([q5]*(n-2) + [0], -1)
    C5 = solve(A5, B5)
    c5 = np.zeros((n, m))
    c5[0, :] = h5 * u0 * x
    c5[-1, :] = c5[0, :]
    c5 = solve(A5, c5)
    
    for j in range(m3, m-1):
        if t[j] >= t[j-1]:
            u[:, j+1] = C4 @ u[:, j] + c4[:, j+1]
        else:
            u[:, j+1] = C5 @ u[:, j] + c5[:, j+1]
        t[j+1] = u[k, j+1]
    
    return t

if __name__ == "__main__":
    optimal_params, best_fitness = problem3_parameter_optimization()
