import numpy as np
import math
import pulp

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

def mm_s_infinite_optimization(s, lamda, mu):
    """
    使用PuLP优化M/M/s/∞系统
    s: 服务台数量
    lamda: 到达率
    mu: 服务率
    """
    rho = lamda / mu
    rho_s = rho / s
    
    # 创建优化问题
    prob = pulp.LpProblem("MM_s_Queueing_System", pulp.LpMinimize)
    
    # 决策变量
    L_q = pulp.LpVariable("L_q", lowBound=0)
    L_s = pulp.LpVariable("L_s", lowBound=0)
    W_q = pulp.LpVariable("W_q", lowBound=0)
    W_s = pulp.LpVariable("W_s", lowBound=0)
    P_wait = pulp.LpVariable("P_wait", lowBound=0, upBound=1)
    
    # 计算等待概率
    P_wait_value = peb(rho, s)
    
    # 添加约束
    prob += L_q == P_wait * rho_s / (1 - rho_s)
    prob += L_s == L_q + rho
    prob += W_q == L_q / lamda
    prob += W_s == L_s / lamda
    prob += P_wait == P_wait_value
    
    # 目标函数：最小化平均等待时间
    prob += W_s
    
    # 求解
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    return {
        'rho': rho,
        'rho_s': rho_s,
        'P_wait': P_wait.varValue,
        'L_q': L_q.varValue,
        'L_s': L_s.varValue,
        'W_q': W_q.varValue,
        'W_s': W_s.varValue
    }

def mm_1_infinite_optimization(lamda, mu):
    """
    使用PuLP优化M/M/1/∞系统
    lamda: 到达率
    mu: 服务率
    """
    s = 1
    rho = lamda / mu
    
    # 创建优化问题
    prob = pulp.LpProblem("MM_1_Queueing_System", pulp.LpMinimize)
    
    # 决策变量
    L_s = pulp.LpVariable("L_s", lowBound=0)
    L_q = pulp.LpVariable("L_q", lowBound=0)
    W_s = pulp.LpVariable("W_s", lowBound=0)
    W_q = pulp.LpVariable("W_q", lowBound=0)
    P_wait = pulp.LpVariable("P_wait", lowBound=0, upBound=1)
    
    # 计算等待概率
    P_wait_value = peb(rho, s)
    
    # 添加约束
    prob += L_s == rho / (1 - rho)
    prob += L_q == L_s - rho
    prob += W_s == L_s / lamda
    prob += W_q == L_q / lamda
    prob += P_wait == P_wait_value
    
    # 目标函数：最小化平均等待时间
    prob += W_s
    
    # 求解
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    
    return {
        'rho': rho,
        'P_wait': P_wait.varValue,
        'L_s': L_s.varValue,
        'L_q': L_q.varValue,
        'W_s': W_s.varValue,
        'W_q': W_q.varValue
    }

def main():
    """
    主函数：使用PuLP计算M/M/s/∞和M/M/1/∞系统
    """
    print("M/M/s/∞系统计算 (使用PuLP):")
    print("=" * 50)
    s = 2
    lamda = 25
    mu = 12.52
    result = mm_s_infinite_optimization(s, lamda, mu)
    
    print(f"服务台数量 (s): {s}")
    print(f"到达率 (λ): {lamda}")
    print(f"服务率 (μ): {mu}")
    print(f"服务强度 (ρ): {result['rho']:.4f}")
    print(f"单个服务台服务强度 (ρ/s): {result['rho_s']:.4f}")
    print(f"等待概率 (P_wait): {result['P_wait']:.4f}")
    print(f"平均队列长度 (L_q): {result['L_q']:.4f}")
    print(f"系统平均顾客数 (L_s): {result['L_s']:.4f}")
    print(f"平均等待时间 (W_q): {result['W_q']:.4f}")
    print(f"平均逗留时间 (W_s): {result['W_s']:.4f}")
    
    print("\n" + "=" * 50)
    print("M/M/1/∞系统计算 (使用PuLP):")
    print("=" * 50)
    lamda = 12.5
    mu = 12.52
    result = mm_1_infinite_optimization(lamda, mu)
    
    print(f"服务台数量 (s): 1")
    print(f"到达率 (λ): {lamda}")
    print(f"服务率 (μ): {mu}")
    print(f"服务强度 (ρ): {result['rho']:.4f}")
    print(f"等待概率 (P_wait): {result['P_wait']:.4f}")
    print(f"系统平均顾客数 (L_s): {result['L_s']:.4f}")
    print(f"平均队列长度 (L_q): {result['L_q']:.4f}")
    print(f"平均逗留时间 (W_s): {result['W_s']:.4f}")
    print(f"平均等待时间 (W_q): {result['W_q']:.4f}")

if __name__ == "__main__":
    main()
