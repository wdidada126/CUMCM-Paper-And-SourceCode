import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def public_bicycle_system():
    """
    公共自行车系统问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Public Bicycle System")
    print("=" * 60)
    
    # 问题1：站点坐标分析
    print("\nProblem 1: Station Coordinate Analysis")
    print("-" * 40)
    
    # 定义站点坐标（示例数据）
    num_stations = 100
    np.random.seed(42)
    
    # 生成站点坐标
    station_x = np.random.uniform(0, 100, num_stations)
    station_y = np.random.uniform(0, 100, num_stations)
    
    # 计算站点之间的距离矩阵
    def calculate_distance_matrix(x, y):
        """
        计算站点之间的距离矩阵
        """
        n = len(x)
        distance_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                distance_matrix[i, j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
        
        return distance_matrix
    
    distance_matrix = calculate_distance_matrix(station_x, station_y)
    
    print(f"Number of stations: {num_stations}")
    print(f"Average distance between stations: {np.mean(distance_matrix):.2f}")
    print(f"Maximum distance: {np.max(distance_matrix):.2f}")
    print(f"Minimum distance: {np.min(distance_matrix[distance_matrix > 0]):.2f}")
    
    # 绘制站点分布图
    plt.figure(figsize=(10, 10))
    plt.scatter(station_x, station_y, c='b', s=50, alpha=0.6)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Public Bicycle Station Distribution')
    plt.grid(True)
    plt.savefig('bicycle_station_distribution.png')
    plt.close()
    
    print("Station distribution plot saved as 'bicycle_station_distribution.png'")
    
    # 问题2：自行车流量分析
    print("\nProblem 2: Bicycle Flow Analysis")
    print("-" * 40)
    
    # 模拟自行车流量数据
    time_hours = np.arange(0, 24, 0.5)
    
    # 早高峰和晚高峰
    morning_peak = 7
    evening_peak = 18
    
    # 生成流量数据
    flow = 50 + 100 * np.exp(-((time_hours - morning_peak)**2) / 2) + \
           100 * np.exp(-((time_hours - evening_peak)**2) / 2) + \
           20 * np.random.randn(len(time_hours))
    flow[flow < 0] = 0
    
    print(f"Peak flow (morning): {np.max(flow[time_hours < 12]):.2f} bicycles/hour")
    print(f"Peak flow (evening): {np.max(flow[time_hours >= 12]):.2f} bicycles/hour")
    print(f"Average flow: {np.mean(flow):.2f} bicycles/hour")
    
    # 绘制流量图
    plt.figure(figsize=(12, 6))
    plt.plot(time_hours, flow, 'b-', linewidth=2)
    plt.axvline(x=morning_peak, color='r', linestyle='--', label='Morning peak')
    plt.axvline(x=evening_peak, color='g', linestyle='--', label='Evening peak')
    plt.xlabel('Time (hours)')
    plt.ylabel('Bicycle Flow (bicycles/hour)')
    plt.title('Public Bicycle Flow Over 24 Hours')
    plt.legend()
    plt.grid(True)
    plt.savefig('bicycle_flow_analysis.png')
    plt.close()
    
    print("Bicycle flow plot saved as 'bicycle_flow_analysis.png'")
    
    # 问题3：站点优化配置
    print("\nProblem 3: Station Optimization")
    print("-" * 40)
    
    # 定义优化问题
    def objective_function(x):
        """
        目标函数：最小化总成本
        x: 决策变量，表示每个站点的自行车数量
        """
        # 建设成本
        construction_cost = np.sum(x > 0) * 10000
        
        # 运营成本
        operation_cost = np.sum(x) * 100
        
        # 总成本
        total_cost = construction_cost + operation_cost
        
        return total_cost
    
    # 约束条件
    def constraints(x):
        """
        约束条件：
        1. 每个站点的自行车数量 >= 0
        2. 每个站点的自行车数量 <= 50
        3. 总自行车数量 >= 500
        """
        constraints_list = []
        
        # 每个站点的自行车数量 >= 0
        constraints_list.extend(x)
        
        # 每个站点的自行车数量 <= 50
        constraints_list.extend(50 - x)
        
        # 总自行车数量 >= 500
        constraints_list.append(np.sum(x) - 500)
        
        return np.array(constraints_list)
    
    # 初始猜测
    x0 = np.ones(num_stations) * 5
    
    # 边界条件
    bounds = [(0, 50)] * num_stations
    
    # 约束
    cons = {'type': 'ineq', 'fun': constraints}
    
    # 优化
    result = minimize(objective_function, x0, method='SLSQP', 
                    bounds=bounds, constraints=cons, 
                    options={'maxiter': 1000})
    
    if result.success:
        print("Optimization successful!")
        print(f"Optimal total cost: {result.fun:.2f} yuan")
        print(f"Total bicycles: {np.sum(result.x):.0f}")
        print(f"Number of active stations: {np.sum(result.x > 0)}")
        
        # 绘制优化结果
        plt.figure(figsize=(12, 6))
        plt.bar(range(num_stations), result.x, color='b', alpha=0.7)
        plt.xlabel('Station ID')
        plt.ylabel('Number of Bicycles')
        plt.title('Optimal Bicycle Distribution')
        plt.grid(True)
        plt.savefig('bicycle_optimization_result.png')
        plt.close()
        
        print("Optimization result plot saved as 'bicycle_optimization_result.png'")
    else:
        print("Optimization failed!")
        print(result.message)
    
    return {
        'num_stations': num_stations,
        'average_distance': np.mean(distance_matrix),
        'peak_flow_morning': np.max(flow[time_hours < 12]),
        'peak_flow_evening': np.max(flow[time_hours >= 12]),
        'optimal_cost': result.fun if result.success else None
    }

if __name__ == "__main__":
    result = public_bicycle_system()
    print("\n" + "=" * 60)
    print("Public bicycle system analysis completed!")
    print("=" * 60)