import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def problem2_velocity_optimization():
    """
    Problem 2: Velocity Optimization
    速度优化 - 寻找最佳过炉速度
    """
    F = np.array([25, 182, 203, 237, 254, 25])
    L = 50 + 30.5*11 + 5*10
    alpha = 7.15e-04
    H1 = 6975.37
    H2 = 97.60
    xm = np.array([alpha, H1, alpha, H1, alpha, H1, alpha, H1, alpha, H2])
    
    T_150_190_Arr = np.zeros(41)
    T_217_Arr = np.zeros(41)
    T_Max_Arr = np.zeros(41)
    K_Max_Arr = np.zeros(41)
    
    # 遍历速度
    velocities = []
    for i in range(41):
        v = 1 + i/60
        velocities.append(v * 60)  # 转换为cm/min
        T = L/v
        u = heat(xm, T, v, F)
        
        # 计算217℃以上时间
        T_217 = np.where(u >= 217)[0]
        T_217_Arr[i] = (len(T_217) - 1) * 0.5
        
        # 计算最大温度
        T_Max_Arr[i] = np.max(u)
        
        # 计算最大斜率
        tmp3 = np.abs(u[1:] - u[:-1]) / 0.5
        K_Max_Arr[i] = np.max(tmp3)
        
        # 计算150-190℃时间
        rising_mask = np.zeros_like(u, dtype=bool)
        rising_mask[1:] = u[1:] >= u[:-1]
        u_rising = u[rising_mask]
        u_rising = u_rising[u_rising >= 150]
        u_rising = u_rising[u_rising <= 190]
        T_150_190_Arr[i] = (len(u_rising) - 1) * 0.5
    
    # 寻找最优速度
    v1 = 65/60
    v2 = 100/60
    optimal_v = find_optimal_velocity(v1, v2, xm, F, L)
    
    print("Problem 2: Velocity Optimization")
    print("=" * 60)
    print(f"Optimal velocity: {optimal_v*60:.2f} cm/min")
    print(f"Optimal velocity: {optimal_v:.4f} cm/s")
    
    # 绘制结果
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    ax1.plot(velocities, K_Max_Arr, 'b-', linewidth=2)
    ax1.set_title('Maximum Slope vs Velocity')
    ax1.set_xlabel('Velocity (cm/min)')
    ax1.set_ylabel('Slope')
    ax1.grid(True)
    
    ax2.plot(velocities, T_Max_Arr, 'r-', linewidth=2)
    ax2.set_title('Maximum Temperature vs Velocity')
    ax2.set_xlabel('Velocity (cm/min)')
    ax2.set_ylabel('Temperature (°C)')
    ax2.grid(True)
    
    ax3.plot(velocities, T_150_190_Arr, 'g-', linewidth=2)
    ax3.set_title('150-190°C Duration vs Velocity')
    ax3.set_xlabel('Velocity (cm/min)')
    ax3.set_ylabel('Time (s)')
    ax3.grid(True)
    
    ax4.plot(velocities, T_217_Arr, 'm-', linewidth=2)
    ax4.set_title('217°C Duration vs Velocity')
    ax4.set_xlabel('Velocity (cm/min)')
    ax4.set_ylabel('Time (s)')
    ax4.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return optimal_v

def f(x, F):
    """
    External temperature distribution function
    """
    gap = 5
    W = 30.5
    x1 = 0
    x2 = 25
    x3 = x2 + 5*W + 4*gap
    x4 = x3 + gap
    x5 = x4 + W
    x6 = x5 + gap
    x7 = x6 + W
    x8 = x7 + gap
    x9 = x8 + 2*W + gap
    x10 = x9 + gap
    
    y = np.zeros_like(x)
    y = np.where(x <= x2, np.exp(0.2007*x) + 24, y)
    y = np.where((x > x2) & (x <= x3), F[1], y)
    y = np.where((x > x3) & (x <= x4), (F[2]-F[1])/gap*(x-x3) + F[1], y)
    y = np.where((x > x4) & (x <= x5), F[2], y)
    y = np.where((x > x5) & (x <= x6), (F[3]-F[2])/gap*(x-x5) + F[2], y)
    y = np.where((x > x6) & (x <= x7), F[3], y)
    y = np.where((x > x7) & (x <= x8), (F[4]-F[3])/gap*(x-x7) + F[3], y)
    y = np.where((x > x8) & (x <= x9), F[4], y)
    y = np.where((x > x9) & (x <= x10), (F[5]-F[4])/gap*(x-x9) + F[4], y)
    y = np.where(x > x10, F[5], y)
    
    return y

def heat(xm, T, v, F):
    """
    Heat conduction equation solver
    """
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
    r1 = xm[0]**2 * dt / (x**2)
    r2 = xm[2]**2 * dt / (x**2)
    r3 = xm[4]**2 * dt / (x**2)
    r4 = xm[6]**2 * dt / (x**2)
    r5 = xm[8]**2 * dt / (x**2)
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
    A1 = np.diag([1 + h1*x] + [2*(1+r1)]*(n-2) + [1 + h1*x])
    A1 += np.diag([-1] + [-r1]*(n-2), 1)
    A1 += np.diag([-r1]*(n-2) + [-1], -1)
    B1 = np.diag([0] + [2*(1-r1)]*(n-2) + [0])
    B1 += np.diag([0] + [r1]*(n-2), 1)
    B1 += np.diag([r1]*(n-2) + [0], -1)
    C1 = solve(A1, B1)
    c = np.zeros((n, m))
    c[0, :] = h1 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A1, c)
    
    for j in range(m1-1):
        u[:, j+1] = C1 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 2
    A2 = np.diag([1 + h2*x] + [2*(1+r2)]*(n-2) + [1 + h2*x])
    A2 += np.diag([-1] + [-r2]*(n-2), 1)
    A2 += np.diag([-r2]*(n-2) + [-1], -1)
    B2 = np.diag([0] + [2*(1-r2)]*(n-2) + [0])
    B2 += np.diag([0] + [r2]*(n-2), 1)
    B2 += np.diag([r2]*(n-2) + [0], -1)
    C2 = solve(A2, B2)
    c = np.zeros((n, m))
    c[0, :] = h2 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A2, c)
    
    for j in range(m1, m2-1):
        u[:, j+1] = C2 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 3
    A3 = np.diag([1 + h3*x] + [2*(1+r3)]*(n-2) + [1 + h3*x])
    A3 += np.diag([-1] + [-r3]*(n-2), 1)
    A3 += np.diag([-r3]*(n-2) + [-1], -1)
    B3 = np.diag([0] + [2*(1-r3)]*(n-2) + [0])
    B3 += np.diag([0] + [r3]*(n-2), 1)
    B3 += np.diag([r3]*(n-2) + [0], -1)
    C3 = solve(A3, B3)
    c = np.zeros((n, m))
    c[0, :] = h3 * u0 * x
    c[-1, :] = c[0, :]
    c = solve(A3, c)
    
    for j in range(m2, m3-1):
        u[:, j+1] = C3 @ u[:, j] + c[:, j+1]
        t[j+1] = u[k, j+1]
    
    # Zone 4 and 5
    A4 = np.diag([1 + h4*x] + [2*(1+r4)]*(n-2) + [1 + h4*x])
    A4 += np.diag([-1] + [-r4]*(n-2), 1)
    A4 += np.diag([-r4]*(n-2) + [-1], -1)
    B4 = np.diag([0] + [2*(1-r4)]*(n-2) + [0])
    B4 += np.diag([0] + [r4]*(n-2), 1)
    B4 += np.diag([r4]*(n-2) + [0], -1)
    C4 = solve(A4, B4)
    c4 = np.zeros((n, m))
    c4[0, :] = h4 * u0 * x
    c4[-1, :] = c4[0, :]
    c4 = solve(A4, c4)
    
    A5 = np.diag([1 + h5*x] + [2*(1+r5)]*(n-2) + [1 + h5*x])
    A5 += np.diag([-1] + [-r5]*(n-2), 1)
    A5 += np.diag([-r5]*(n-2) + [-1], -1)
    B5 = np.diag([0] + [2*(1-r5)]*(n-2) + [0])
    B5 += np.diag([0] + [r5]*(n-2), 1)
    B5 += np.diag([r5]*(n-2) + [0], -1)
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

def check_constraints(xm, F, L):
    """
    Check if constraints are satisfied
    """
    v = 1
    T = L/v
    u = heat(xm, T, v, F)
    
    Arr_217 = np.where(u >= 217)[0]
    T217 = len(Arr_217) * 0.5
    TMax = np.max(u)
    K = np.abs(u[1:] - u[:-1]) / 0.5
    KMax = np.max(K)
    rising_mask = np.zeros_like(u, dtype=bool)
    rising_mask[1:] = u[1:] >= u[:-1]
    s = u[rising_mask]
    s = s[s >= 150]
    s = s[s <= 190]
    T_60_120 = len(s) * 0.5
    
    return (TMax <= 250) and (TMax >= 240) and (T217 >= 40) and (T217 <= 90) and (KMax <= 3) and (T_60_120 <= 120) and (T_60_120 >= 60)

def find_optimal_velocity(v1, v2, xm, F, L):
    """
    Binary search for optimal velocity
    """
    while True:
        v = (v1 + v2) / 2
        T = L/v
        if check_constraints(xm, F, L):
            v1 = v
        else:
            v2 = v
        if v2 - v1 < 1e-4:
            break
    return (v1 + v2) / 2

if __name__ == "__main__":
    optimal_v = problem2_velocity_optimization()
