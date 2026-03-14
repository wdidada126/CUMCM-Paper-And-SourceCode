import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def problem1_temperature_curve():
    """
    Problem 1: Temperature Curve Modeling
    炉温曲线建模 - 使用热传导方程的数值解
    """
    F = np.array([25, 173, 198, 230, 257, 25])
    v = 78/60
    W = 30.5
    Left = 25
    Right = 25
    gap = 5
    L = Left*2 + W*11 + gap*10
    T = L/v
    dt = 0.5
    t = np.arange(0, T + dt, dt)
    
    alpha = 7.15e-04
    H1 = 6975.37
    H2 = 97.60
    xm = np.array([alpha, H1, alpha, H1, alpha, H1, alpha, H1, alpha, H2])
    
    u = heat(xm, T, v, F)
    
    print("Problem 1: Temperature Curve Modeling")
    print("=" * 60)
    print(f"Total length L: {L:.2f} cm")
    print(f"Total time T: {T:.2f} s")
    print(f"Velocity v: {v:.4f} cm/s")
    print(f"Max temperature: {np.max(u):.2f} °C")
    print(f"Min temperature: {np.min(u):.2f} °C")
    
    return t, u

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

def heat(xm, T, v, F):
    """
    Heat conduction equation solver using finite difference method
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
    t, u = problem1_temperature_curve()
    
    # Plot temperature curve
    plt.figure(figsize=(12, 6))
    plt.plot(t * (78/60), u, 'b-', linewidth=2, label='Temperature')
    plt.xlabel('Distance (cm)')
    plt.ylabel('Temperature (°C)')
    plt.title('Furnace Temperature Curve')
    plt.legend()
    plt.grid(True)
    plt.ylim([0, 280])
    plt.show()
