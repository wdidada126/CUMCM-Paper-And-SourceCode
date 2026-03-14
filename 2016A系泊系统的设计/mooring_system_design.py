import numpy as np
import matplotlib.pyplot as plt

def mooring_system_design():
    """
    系泊系统的设计问题
    基于C++代码的Python实现
    """
    print("Problem: Mooring System Design")
    print("=" * 60)
    
    # 问题1：系泊系统受力分析
    print("\nProblem 1: Mooring System Force Analysis")
    print("-" * 40)
    
    # 定义系泊系统参数
    # 水深
    water_depth = 18  # 米
    
    # 钢桶参数
    drum_radius = 1  # 米
    drum_height = 2  # 米
    drum_mass = 1000  # kg
    
    # 钢管参数
    pipe_length = 12  # 米
    pipe_radius = 0.1  # 米
    pipe_mass = 50  # kg
    
    # 链条参数
    chain_length = 20  # 米
    chain_mass = 10  # kg
    
    # 浮标参数
    buoy_mass = 500  # kg
    buoy_radius = 1.5  # 米
    
    # 计算重力
    g = 9.81  # 重力加速度
    drum_weight = drum_mass * g
    pipe_weight = pipe_mass * g
    chain_weight = chain_mass * g
    buoy_weight = buoy_mass * g
    
    print(f"Drum weight: {drum_weight:.2f} N")
    print(f"Pipe weight: {pipe_weight:.2f} N")
    print(f"Chain weight: {chain_weight:.2f} N")
    print(f"Buoy weight: {buoy_weight:.2f} N")
    
    # 计算浮力
    def calculate_buoyancy(radius, height):
        """
        计算浮力
        """
        volume = np.pi * radius**2 * height
        water_density = 1000  # kg/m³
        buoyancy = volume * water_density * g
        return buoyancy
    
    drum_buoyancy = calculate_buoyancy(drum_radius, drum_height)
    pipe_buoyancy = calculate_buoyancy(pipe_radius, pipe_length)
    buoy_buoyancy = calculate_buoyancy(buoy_radius, buoy_height=2)
    
    print(f"Drum buoyancy: {drum_buoyancy:.2f} N")
    print(f"Pipe buoyancy: {pipe_buoyancy:.2f} N")
    print(f"Buoy buoyancy: {buoy_buoyancy:.2f} N")
    
    # 计算总受力
    total_weight = drum_weight + pipe_weight + chain_weight + buoy_weight
    total_buoyancy = drum_buoyancy + pipe_buoyancy + buoy_buoyancy
    
    print(f"Total weight: {total_weight:.2f} N")
    print(f"Total buoyancy: {total_buoyancy:.2f} N")
    print(f"Net force: {total_buoyancy - total_weight:.2f} N")
    
    # 问题2：系泊系统运动分析
    print("\nProblem 2: Mooring System Motion Analysis")
    print("-" * 40)
    
    # 模拟系泊系统的运动
    time = np.linspace(0, 100, 1000)
    
    # 海浪参数
    wave_amplitude = 1  # 米
    wave_frequency = 0.5  # Hz
    
    # 浮标位移
    buoy_displacement = wave_amplitude * np.sin(2 * np.pi * wave_frequency * time)
    
    # 链条张力
    def calculate_tension(displacement, chain_length, water_depth):
        """
        计算链条张力
        """
        # 简化的张力计算
        tension = np.abs(displacement) * 1000 + chain_length * 50
        return tension
    
    chain_tension = calculate_tension(buoy_displacement, chain_length, water_depth)
    
    print(f"Maximum buoy displacement: {np.max(np.abs(buoy_displacement)):.2f} m")
    print(f"Maximum chain tension: {np.max(chain_tension):.2f} N")
    print(f"Average chain tension: {np.mean(chain_tension):.2f} N")
    
    # 绘制运动和张力图
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1.plot(time, buoy_displacement, 'b-', linewidth=2)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Displacement (m)')
    ax1.set_title('Buoy Displacement')
    ax1.grid(True)
    
    ax2.plot(time, chain_tension, 'r-', linewidth=2)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Tension (N)')
    ax2.set_title('Chain Tension')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('mooring_system_motion.png')
    plt.close()
    
    print("Motion analysis plot saved as 'mooring_system_motion.png'")
    
    # 问题3：优化设计
    print("\nProblem 3: Optimal Design")
    print("-" * 40)
    
    # 优化链条长度
    def objective_function(chain_length):
        """
        目标函数：最小化最大张力
        """
        # 计算最大张力
        max_tension = np.max(calculate_tension(buoy_displacement, chain_length, water_depth))
        
        # 计算成本（链条越长成本越高）
        cost = chain_length * 100
        
        # 目标：最小化张力和成本的加权和
        return max_tension + 0.1 * cost
    
    # 搜索最优链条长度
    chain_lengths = np.linspace(10, 30, 100)
    objective_values = [objective_function(L) for L in chain_lengths]
    
    optimal_index = np.argmin(objective_values)
    optimal_chain_length = chain_lengths[optimal_index]
    
    print(f"Optimal chain length: {optimal_chain_length:.2f} m")
    print(f"Objective value: {objective_values[optimal_index]:.2f}")
    
    # 绘制优化结果
    plt.figure(figsize=(10, 6))
    plt.plot(chain_lengths, objective_values, 'b-', linewidth=2)
    plt.axvline(x=optimal_chain_length, color='r', linestyle='--', label='Optimal')
    plt.xlabel('Chain Length (m)')
    plt.ylabel('Objective Value')
    plt.title('Mooring System Optimization')
    plt.legend()
    plt.grid(True)
    plt.savefig('mooring_system_optimization.png')
    plt.close()
    
    print("Optimization plot saved as 'mooring_system_optimization.png'")
    
    return {
        'total_weight': total_weight,
        'total_buoyancy': total_buoyancy,
        'net_force': total_buoyancy - total_weight,
        'max_tension': np.max(chain_tension),
        'optimal_chain_length': optimal_chain_length
    }

if __name__ == "__main__":
    result = mooring_system_design()
    print("\n" + "=" * 60)
    print("Mooring system design analysis completed!")
    print("=" * 60)