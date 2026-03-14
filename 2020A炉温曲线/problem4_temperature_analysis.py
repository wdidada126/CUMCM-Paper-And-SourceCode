import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def problem4_temperature_analysis():
    """
    Problem 4: Temperature Distribution Analysis
    温度分布分析 - 参数搜索和统计分析
    """
    L = 50 + 30.5*11 + 5*10
    alpha = 7.15e-04
    H1 = 6975.37
    H2 = 97.60
    xm = np.array([alpha, H1, alpha, H1, alpha, H1, alpha, H1, alpha, H2])
    
    # 参数范围
    Temp15 = np.arange(165, 186, 5)
    Temp6 = np.arange(185, 206, 5)
    Temp7 = np.arange(225, 246, 5)
    Temp89 = np.arange(245, 266, 5)
    V = np.arange(65, 101, 5)
    
    Z_SArr = []
    Z_Sk = []
    Z_Result = []
    
    print("Problem 4: Temperature Distribution Analysis")
    print("=" * 60)
    print("Searching parameter space...")
    
    n = 0
    # 参数搜索（简化版，只搜索部分组合）
    for i1 in range(len(Temp15)):
        for i2 in range(len(Temp6)):
            for i3 in range(len(Temp7)):
                for i4 in range(len(Temp89)):
                    for i5 in range(len(V)):
                        x = np.array([Temp15[i1], Temp6[i2], Temp7[i3], Temp89[i4], V[i5]/60])
                        
                        u0 = get_temp(x[0], x[1], x[2], x[3], x[4], xm, L)
                        
                        v = x[4]
                        F = np.array([25, x[0], x[1], x[2], x[3], 25])
                        T = L/v
                        
                        # 计算面积
                        S = area1(x, u0)
                        
                        if S < 999:
                            n += 1
                            Z_SArr.append(S)
                            
                            # 计算统计量
                            AllTemp = u0[u0 > 217]
                            if len(AllTemp) > 0:
                                Xbar = np.mean(AllTemp)
                                M0 = np.max(AllTemp)
                                Sigma = np.std(AllTemp)
                                if Sigma > 0:
                                    Sk = abs(Xbar - M0) / Sigma
                                    Z_Sk.append(Sk)
                                    Z_Result.append(x.copy())
    
    print(f"Found {n} valid parameter combinations")
    
    if len(Z_Sk) > 0:
        # 绘制SK值分布
        plt.figure(figsize=(10, 6))
        plt.scatter(range(1, len(Z_Sk)+1), Z_Sk, s=8, c='b', alpha=0.6)
        plt.xlabel('Index')
        plt.ylabel('SK')
        plt.title('SK Value Distribution')
        plt.grid(True)
        plt.show()
        
        # 找到最优参数
        best_idx = np.argmin(Z_SArr)
        best_params = Z_Result[best_idx]
        best_area = Z_SArr[best_idx]
        best_sk = Z_Sk[best_idx]
        
        print(f"\nBest parameters:")
        print(f"Temp1: {best_params[0]:.2f} °C")
        print(f"Temp2: {best_params[1]:.2f} °C")
        print(f"Temp3: {best_params[2]:.2f} °C")
        print(f"Temp4: {best_params[3]:.2f} °C")
        print(f"Velocity: {best_params[4]*60:.2f} cm/min")
        print(f"Area: {best_area:.4f}")
        print(f"SK: {best_sk:.4f}")
        
        return best_params, best_area, best_sk
    else:
        print("No valid parameter combinations found")
        return None, None, None

def f(x, F):
    """
    External temperature distribution function
    """
    gap = 5
    W = 30.5
    Left = 25
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

def get_temp(u1, u2, u3, u4, v, xm, L):
    """
    Get temperature distribution
    """
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

def area1(x, u0):
    """
    Calculate area above 217°C
    """
    u = u0[u0 >= 30]
    tmp2 = u[u >= 217] - 217
    t2 = len(tmp2) * 0.5
    umax = np.max(u)
    tmp3 = np.abs(u[1:] - u[:-1]) / 0.5
    kmax = np.max(tmp3)
    rising_mask = np.zeros_like(u, dtype=bool)
    rising_mask[1:] = u[1:] >= u[:-1]
    s = u[rising_mask]
    s = s[s >= 150]
    s = s[s <= 190]
    t1 = len(s) * 0.5
    
    y = (umax <= 250) and (umax >= 240) and (t2 >= 40) and (t2 <= 90) and (kmax <= 3) and (t1 <= 120) and (t1 >= 60)
    
    if y:
        k = np.argmax(tmp2)
        if k > 2:
            a = (np.sum(tmp2[:k]) - (tmp2[0] + tmp2[k]) / 2) * 0.5
        else:
            a = (tmp2[0] + tmp2[k]) * 0.5 / 2
        
        if a > 406.1637111 * 1.05:
            return 10000
        return a
    else:
        return 10000

if __name__ == "__main__":
    best_params, best_area, best_sk = problem4_temperature_analysis()
