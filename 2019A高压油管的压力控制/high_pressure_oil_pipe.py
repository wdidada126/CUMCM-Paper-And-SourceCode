import numpy as np
import matplotlib.pyplot as plt

def high_pressure_oil_pipe():
    """
    高压油管的压力控制问题
    基于MATLAB代码的Python实现
    """
    print("Problem: High Pressure Oil Pipe Control")
    print("=" * 60)
    
    # 问题1：压力控制优化
    print("\nProblem 1: Pressure Control Optimization")
    print("-" * 40)
    
    # 定义参数
    C = 0.85  # 流量系数
    A = 0.49 * np.pi  # 小孔面积
    V = 12500 * np.pi  # 油管体积
    tstep = 0.02  # 时间步长
    
    # 油泵和油管参数
    Pyb = 160  # 油泵压力
    rouyb = 0.8725  # 油泵油密度
    rouyg = 0.85  # 油管油密度
    tclose = 10  # 闭阀时间
    
    # 密度转化为压力的函数
    def density_to_pressure(x):
        """
        密度转化为压力
        """
        return 17284.0015 * x**2 - 27111.3456 * x + 10656.1125
    
    # 单向阀状态函数
    def valve_state(t, topen, tclose):
        """
        单向阀状态
        topen: 开阀时间
        tclose: 关阀时间
        """
        T = topen + tclose  # 总周期
        mt = t % T  # 放入第一周期
        if mt <= topen:
            return 1  # 开阀
        else:
            return 0  # 闭阀
    
    # 输入时间，输出喷油速率
    def injection_rate(t):
        """
        喷油速率函数
        """
        nt = t % 100  # 放入第一周期
        if nt <= 0.2:
            return 100 * nt
        elif nt <= 2.2:
            return 20
        elif nt <= 2.4:
            return 240 - 100 * nt
        else:
            return 0
    
    # 遍历法寻找最优开阀时间
    topen_values = np.arange(0.01, 5.01, 0.01)
    z_values = []
    
    for topen in topen_values:
        Pyb = 160
        Pyg = 100
        rouyb = 0.8725
        rouyg = 0.85
        tclose = 10
        myg = rouyg * V  # 起始油管油质量
        
        P = []
        t_values = np.arange(0, 2000 + tstep, tstep)
        
        for t in t_values:
            # 计算体积变化
            if Pyb > Pyg:
                Qin = valve_state(t, topen, tclose) * C * A * np.sqrt(2 * (Pyb - Pyg) / rouyb) * tstep
            else:
                Qin = 0
            
            Qout = injection_rate(t) * tstep
            myg = myg + (Qin - Qout) * rouyg  # 计算油管油质量
            rouyg = myg / V  # 更新油管油密度
            Pyg = density_to_pressure(rouyg)  # 更新油管油压力
            P.append(Pyg)
        
        # 计算误差
        z = np.sum((100 - np.array(P))**2)
        z_values.append(z)
    
    # 找到最优开阀时间
    min_index = np.argmin(z_values)
    optimal_topen = topen_values[min_index]
    min_error = z_values[min_index]
    
    print(f"Optimal valve opening time: {optimal_topen:.2f} s")
    print(f"Minimum error: {min_error:.2f}")
    
    # 绘制误差随开阀时间变化曲线
    plt.figure(figsize=(10, 6))
    plt.plot(topen_values, z_values, 'b-', linewidth=2)
    plt.axvline(x=optimal_topen, color='r', linestyle='--', label='Optimal')
    plt.xlabel('Valve Opening Time (s)')
    plt.ylabel('Error')
    plt.title('Error vs Valve Opening Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('pressure_control_optimization.png')
    plt.close()
    
    print("Optimization plot saved as 'pressure_control_optimization.png'")
    
    # 问题2：压力变化曲线
    print("\nProblem 2: Pressure Variation Curve")
    print("-" * 40)
    
    # 使用最优开阀时间计算压力变化
    topen = optimal_topen
    Pyb = 160
    Pyg = 100
    rouyb = 0.8725
    rouyg = 0.85
    tclose = 10
    myg = rouyg * V
    
    P = []
    t_values = np.arange(0, 2000 + tstep, tstep)
    
    for t in t_values:
        if Pyb > Pyg:
            Qin = valve_state(t, topen, tclose) * C * A * np.sqrt(2 * (Pyb - Pyg) / rouyb) * tstep
        else:
            Qin = 0
        
        Qout = injection_rate(t) * tstep
        myg = myg + (Qin - Qout) * rouyg
        rouyg = myg / V
        Pyg = density_to_pressure(rouyg)
        P.append(Pyg)
    
    P = np.array(P)
    
    print(f"Maximum pressure: {np.max(P):.2f}")
    print(f"Minimum pressure: {np.min(P):.2f}")
    print(f"Average pressure: {np.mean(P):.2f}")
    print(f"Pressure standard deviation: {np.std(P):.2f}")
    
    # 绘制压力变化曲线
    plt.figure(figsize=(12, 6))
    plt.plot(t_values, P, 'b-', linewidth=2)
    plt.axhline(y=100, color='r', linestyle='--', label='Target Pressure')
    plt.xlabel('Time (s)')
    plt.ylabel('Pressure')
    plt.title('Pressure Variation Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('pressure_variation_curve.png')
    plt.close()
    
    print("Pressure variation plot saved as 'pressure_variation_curve.png'")
    
    # 问题3：喷油速率分析
    print("\nProblem 3: Injection Rate Analysis")
    print("-" * 40)
    
    # 计算喷油速率
    injection_rates = [injection_rate(t) for t in t_values]
    
    print(f"Maximum injection rate: {np.max(injection_rates):.2f}")
    print(f"Average injection rate: {np.mean(injection_rates):.2f}")
    
    # 绘制喷油速率曲线
    plt.figure(figsize=(12, 6))
    plt.plot(t_values, injection_rates, 'g-', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Injection Rate')
    plt.title('Injection Rate Over Time')
    plt.grid(True)
    plt.savefig('injection_rate_curve.png')
    plt.close()
    
    print("Injection rate plot saved as 'injection_rate_curve.png'")
    
    return {
        'optimal_topen': optimal_topen,
        'min_error': min_error,
        'max_pressure': np.max(P),
        'min_pressure': np.min(P),
        'avg_pressure': np.mean(P)
    }

if __name__ == "__main__":
    result = high_pressure_oil_pipe()
    print("\n" + "=" * 60)
    print("High pressure oil pipe control analysis completed!")
    print("=" * 60)