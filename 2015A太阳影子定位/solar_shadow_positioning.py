import numpy as np
import matplotlib.pyplot as plt

def solar_shadow_positioning():
    """
    太阳影子定位问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Solar Shadow Positioning")
    print("=" * 60)
    
    # 问题1：计算太阳影子长度
    print("\nProblem 1: Solar Shadow Length Calculation")
    print("-" * 40)
    
    # 定义参数
    # Φ -> A   纬度
    # δ -> F   太阳赤道纬度夹角
    # ω -> C   太阳时角
    # h -> Oh  太阳高度角
    # λ -> D   经度
    
    # 10月22日北京时间9:00-15:00
    # 10月22日是一年的第295天
    n = 295.0
    
    # 地理位置北纬39度54分26秒，东经116度23分29秒
    A = 39 + 54/60 + 26/3600  # 纬度
    D = 116 + 23/60 + 29/3600  # 经度
    Dm = 120  # 时区经度
    
    # 太阳赤纬夹角（度）
    F = 23.45 * np.sin(2 * np.pi * (284 + n) / 365)
    
    # 太阳时
    B = 2 * np.pi * (n - 81) / 364
    E = 9.87 * np.sin(2 * B) - 7.53 * np.cos(B) - 1.5 * np.sin(B)
    
    # 计算影子长度
    Ls_arr = []
    X_arr = []
    
    # 9:00-15:00
    for m in range(9, 15):
        for nn in range(0, 60, 10):
            T0 = m + nn / 60
            Ts = T0 + E / 60 + (D - Dm) / 15
            
            # 太阳时角（度）
            C = 15 * (Ts - 12)
            
            # 太阳高度角
            Oh = np.arcsin(np.sin(A * np.pi / 180) * np.sin(F * np.pi / 180) + 
                         np.cos(A * np.pi / 180) * np.cos(F * np.pi / 180) * 
                         np.cos(C * np.pi / 180))
            
            # 杆长 L = 3 m
            L = 3
            
            # 影长 Ls
            Ls = L / np.tan(Oh)
            
            Ls_arr.append(Ls)
            X_arr.append(m + nn / 60)
    
    Ls_arr = np.array(Ls_arr)
    X_arr = np.array(X_arr)
    
    print(f"Minimum shadow length: {np.min(Ls_arr):.2f} m")
    print(f"Maximum shadow length: {np.max(Ls_arr):.2f} m")
    print(f"Average shadow length: {np.mean(Ls_arr):.2f} m")
    
    # 绘制影子长度随时间变化曲线
    plt.figure(figsize=(10, 6))
    plt.plot(X_arr, Ls_arr, 'r-', linewidth=2, label='Shadow Length')
    plt.xlabel('Time (hours)')
    plt.ylabel('Shadow Length (m)')
    plt.title('Solar Shadow Length vs Time (Oct 22, Beijing)')
    plt.legend()
    plt.grid(True)
    plt.savefig('solar_shadow_length.png')
    plt.close()
    
    print("Shadow length plot saved as 'solar_shadow_length.png'")
    
    # 问题2：不同杆长的影子长度
    print("\nProblem 2: Shadow Length for Different Pole Lengths")
    print("-" * 40)
    
    L_values = [3, 4, 5, 6, 7, 8, 9, 10]
    
    plt.figure(figsize=(10, 6))
    
    for L in L_values:
        Ls_arr_L = []
        X_arr_L = []
        
        for m in range(9, 15):
            for nn in range(0, 60, 10):
                T0 = m + nn / 60
                Ts = T0 + E / 60 + (D - Dm) / 15
                C = 15 * (Ts - 12)
                Oh = np.arcsin(np.sin(A * np.pi / 180) * np.sin(F * np.pi / 180) + 
                             np.cos(A * np.pi / 180) * np.cos(F * np.pi / 180) * 
                             np.cos(C * np.pi / 180))
                Ls = L / np.tan(Oh)
                Ls_arr_L.append(Ls)
                X_arr_L.append(m + nn / 60)
        
        plt.plot(X_arr_L, Ls_arr_L, linewidth=2, label=f'L={L}m')
    
    plt.xlabel('Time (hours)')
    plt.ylabel('Shadow Length (m)')
    plt.title('Solar Shadow Length vs Time for Different Pole Lengths')
    plt.legend()
    plt.grid(True)
    plt.savefig('solar_shadow_length_different_poles.png')
    plt.close()
    
    print("Shadow length plot for different poles saved as 'solar_shadow_length_different_poles.png'")
    
    # 问题3：不同日期的影子长度
    print("\nProblem 3: Shadow Length for Different Dates")
    print("-" * 40)
    
    # 不同日期（一年中的第几天）
    days = [80, 172, 266, 355]  # 春分、夏至、秋分、冬至
    
    plt.figure(figsize=(10, 6))
    
    for n in days:
        F = 23.45 * np.sin(2 * np.pi * (284 + n) / 365)
        B = 2 * np.pi * (n - 81) / 364
        E = 9.87 * np.sin(2 * B) - 7.53 * np.cos(B) - 1.5 * np.sin(B)
        
        Ls_arr_n = []
        X_arr_n = []
        
        for m in range(9, 15):
            for nn in range(0, 60, 10):
                T0 = m + nn / 60
                Ts = T0 + E / 60 + (D - Dm) / 15
                C = 15 * (Ts - 12)
                Oh = np.arcsin(np.sin(A * np.pi / 180) * np.sin(F * np.pi / 180) + 
                             np.cos(A * np.pi / 180) * np.cos(F * np.pi / 180) * 
                             np.cos(C * np.pi / 180))
                Ls = 3 / np.tan(Oh)
                Ls_arr_n.append(Ls)
                X_arr_n.append(m + nn / 60)
        
        plt.plot(X_arr_n, Ls_arr_n, linewidth=2, label=f'Day {n}')
    
    plt.xlabel('Time (hours)')
    plt.ylabel('Shadow Length (m)')
    plt.title('Solar Shadow Length vs Time for Different Dates')
    plt.legend()
    plt.grid(True)
    plt.savefig('solar_shadow_length_different_dates.png')
    plt.close()
    
    print("Shadow length plot for different dates saved as 'solar_shadow_length_different_dates.png'")
    
    return {
        'min_shadow_length': np.min(Ls_arr),
        'max_shadow_length': np.max(Ls_arr),
        'avg_shadow_length': np.mean(Ls_arr)
    }

if __name__ == "__main__":
    result = solar_shadow_positioning()
    print("\n" + "=" * 60)
    print("Solar shadow positioning analysis completed!")
    print("=" * 60)