import numpy as np
import math

def peb(rho, s):
    """
    计算等待概率 P_wait
    rho: 服务强度
    s: 服务台数量
    """
    if rho < s:
        # 计算Erlang C公式
        numerator = (s * rho)**s / (math.factorial(s) * (1 - rho/s))
        
        denominator = 0
        for k in range(s):
            denominator += (s * rho)**k / math.factorial(k)
        denominator += numerator
        
        P_wait = numerator / denominator
        return P_wait
    else:
        return 1.0

def mm_s_infinite(s, lamda, mu):
    """
    M/M/s/∞系统计算
    s: 服务台数量
    lamda: 到达率
    mu: 服务率
    """
    rho = lamda / mu
    rho_s = rho / s
    
    P_wait = peb(rho, s)
    
    if s == 2:
        p0 = 2 * (1 - rho_s) / rho**3 * P_wait
    else:
        p0 = 1 - P_wait
    
    L_q = P_wait * rho_s / (1 - rho_s)
    L_s = L_q + rho
    W_q = L_q / lamda
    W_s = L_s / lamda
    
    return {
        'rho': rho,
        'rho_s': rho_s,
        'P_wait': P_wait,
        'p0': p0,
        'L_q': L_q,
        'L_s': L_s,
        'W_q': W_q,
        'W_s': W_s
    }

def mm_1_infinite(lamda, mu):
    """
    M/M/1/∞系统计算
    lamda: 到达率
    mu: 服务率
    """
    s = 1
    rho = lamda / mu
    P_wait = peb(rho, s)
    p0 = 1 - P_wait
    
    L_s = rho / (1 - rho)
    L_q = L_s - rho
    W_s = L_s / lamda
    W_q = L_q / lamda
    
    return {
        'rho': rho,
        'P_wait': P_wait,
        'p0': p0,
        'L_s': L_s,
        'L_q': L_q,
        'W_s': W_s,
        'W_q': W_q
    }

def main():
    """
    主函数：计算M/M/s/∞和M/M/1/∞系统
    """
    print("M/M/s/∞系统计算:")
    print("=" * 50)
    s = 2
    lamda = 25
    mu = 12.52
    result = mm_s_infinite(s, lamda, mu)
    
    print(f"服务台数量 (s): {s}")
    print(f"到达率 (λ): {lamda}")
    print(f"服务率 (μ): {mu}")
    print(f"服务强度 (ρ): {result['rho']:.4f}")
    print(f"单个服务台服务强度 (ρ/s): {result['rho_s']:.4f}")
    print(f"等待概率 (P_wait): {result['P_wait']:.4f}")
    print(f"系统空闲概率 (p0): {result['p0']:.4f}")
    print(f"平均队列长度 (L_q): {result['L_q']:.4f}")
    print(f"系统平均顾客数 (L_s): {result['L_s']:.4f}")
    print(f"平均等待时间 (W_q): {result['W_q']:.4f}")
    print(f"平均逗留时间 (W_s): {result['W_s']:.4f}")
    
    print("\n" + "=" * 50)
    print("M/M/1/∞系统计算:")
    print("=" * 50)
    lamda = 12.5
    mu = 12.52
    result = mm_1_infinite(lamda, mu)
    
    print(f"服务台数量 (s): 1")
    print(f"到达率 (λ): {lamda}")
    print(f"服务率 (μ): {mu}")
    print(f"服务强度 (ρ): {result['rho']:.4f}")
    print(f"等待概率 (P_wait): {result['P_wait']:.4f}")
    print(f"系统空闲概率 (p0): {result['p0']:.4f}")
    print(f"系统平均顾客数 (L_s): {result['L_s']:.4f}")
    print(f"平均队列长度 (L_q): {result['L_q']:.4f}")
    print(f"平均逗留时间 (W_s): {result['W_s']:.4f}")
    print(f"平均等待时间 (W_q): {result['W_q']:.4f}")

if __name__ == "__main__":
    main()
