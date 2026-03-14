import numpy as np
import math
from ortools.linear_solver import pywraplp

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

def mm_s_infinite_ortools(s, lamda, mu):
    """
    使用OR-Tools优化M/M/s/∞系统
    s: 服务台数量
    lamda: 到达率
    mu: 服务率
    """
    rho = lamda / mu
    rho_s = rho / s
    
    # 创建求解器
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # 决策变量
    L_q = solver.NumVar(0, solver.infinity(), 'L_q')
    L_s = solver.NumVar(0, solver.infinity(), 'L_s')
    W_q = solver.NumVar(0, solver.infinity(), 'W_q')
    W_s = solver.NumVar(0, solver.infinity(), 'W_s')
    P_wait = solver.NumVar(0, 1, 'P_wait')
    
    # 计算等待概率
    P_wait_value = peb(rho, s)
    
    # 添加约束
    solver.Add(L_q == P_wait * rho_s / (1 - rho_s))
    solver.Add(L_s == L_q + rho)
    solver.Add(W_q == L_q / lamda)
    solver.Add(W_s == L_s / lamda)
    solver.Add(P_wait == P_wait_value)
    
    # 目标函数：最小化平均等待时间
    solver.Minimize(W_s)
    
    # 求解
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        return {
            'rho': rho,
            'rho_s': rho_s,
            'P_wait': P_wait.solution_value(),
            'L_q': L_q.solution_value(),
            'L_s': L_s.solution_value(),
            'W_q': W_q.solution_value(),
            'W_s': W_s.solution_value()
        }
    else:
        raise Exception("求解失败")

def mm_1_infinite_ortools(lamda, mu):
    """
    使用OR-Tools优化M/M/1/∞系统
    lamda: 到达率
    mu: 服务率
    """
    s = 1
    rho = lamda / mu
    
    # 创建求解器
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # 决策变量
    L_s = solver.NumVar(0, solver.infinity(), 'L_s')
    L_q = solver.NumVar(0, solver.infinity(), 'L_q')
    W_s = solver.NumVar(0, solver.infinity(), 'W_s')
    W_q = solver.NumVar(0, solver.infinity(), 'W_q')
    P_wait = solver.NumVar(0, 1, 'P_wait')
    
    # 计算等待概率
    P_wait_value = peb(rho, s)
    
    # 添加约束
    solver.Add(L_s == rho / (1 - rho))
    solver.Add(L_q == L_s - rho)
    solver.Add(W_s == L_s / lamda)
    solver.Add(W_q == L_q / lamda)
    solver.Add(P_wait == P_wait_value)
    
    # 目标函数：最小化平均等待时间
    solver.Minimize(W_s)
    
    # 求解
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        return {
            'rho': rho,
            'P_wait': P_wait.solution_value(),
            'L_s': L_s.solution_value(),
            'L_q': L_q.solution_value(),
            'W_s': W_s.solution_value(),
            'W_q': W_q.solution_value()
        }
    else:
        raise Exception("求解失败")

def main():
    """
    主函数：使用OR-Tools计算M/M/s/∞和M/M/1/∞系统
    """
    print("M/M/s/∞系统计算 (使用OR-Tools):")
    print("=" * 50)
    s = 2
    lamda = 25
    mu = 12.52
    result = mm_s_infinite_ortools(s, lamda, mu)
    
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
    print("M/M/1/∞系统计算 (使用OR-Tools):")
    print("=" * 50)
    lamda = 12.5
    mu = 12.52
    result = mm_1_infinite_ortools(lamda, mu)
    
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
