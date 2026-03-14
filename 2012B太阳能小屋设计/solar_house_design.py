import numpy as np
import pandas as pd

def solar_house_design():
    """
    太阳能小屋设计问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Solar House Design")
    print("=" * 60)
    
    # 定义太阳能板参数
    # area: 太阳能板面积 [长*宽]
    area = np.array([
        1.58*0.808, 1.966*0.991, 1.58*0.808, 1.651*0.991, 
        1.65*0.991, 1.956*0.991, 1.65*0.991, 1.956*0.991,
        1.482*0.992, 1.64*0.992, 1.956*0.992, 1.956*0.992,
        1.668*1, 1.3*1.1, 1.321*0.711, 1.414*1.114,
        1.4*1.1, 1.4*1.1, 0.310*0.355, 0.615*0.180,
        0.615*0.355, 0.92*0.355, 0.818*0.355, 1.645*0.712
    ])
    
    # 定义屋顶朝向
    # 0: 东, 1: 南, 2: 西, 3: 北
    roof_orientation = np.zeros(24, dtype=int)
    
    # 问题1：屋顶设计
    print("\nProblem 1: Roof Design")
    print("-" * 40)
    
    # 设置屋顶朝向（示例：朝南）
    roof_orientation[2] = 42  # 南向，倾斜42度
    
    # 计算成本和发电量
    def calculate_cost_value(orientation, radiation):
        """
        计算成本和发电量
        orientation: 屋顶朝向数组
        radiation: 太阳辐射数据
        """
        # 简化的成本计算
        num_panels = np.sum(orientation > 0)
        cost = num_panels * 1000  # 假设每块板成本1000元
        
        # 简化的发电量计算
        total_radiation = np.sum(radiation)
        value = total_radiation * 0.15 * num_panels  # 假设转换效率15%
        
        return cost, value
    
    # 生成示例辐射数据
    np.random.seed(42)
    radiation1 = np.random.uniform(100, 800, 8760)  # 8760小时数据
    
    cost1, value1 = calculate_cost_value(roof_orientation, radiation1)
    print(f"Cost: {cost:.2f} yuan")
    print(f"Annual power generation: {value1:.2f} kWh")
    
    # 问题2：优化设计
    print("\nProblem 2: Optimization Design")
    print("-" * 40)
    
    # 读取天气数据（示例）
    # radiation2 = pd.read_excel('weather.xls', sheet_name='E1:E8760')
    radiation2 = np.random.uniform(100, 800, 8760)
    
    roof_orientation2 = np.zeros(24, dtype=int)
    roof_orientation2[13] = 13  # 优化后的朝向
    roof_orientation2[19] = 40
    
    cost2, value2 = calculate_cost_value(roof_orientation2, radiation2)
    print(f"Optimized cost: {cost2:.2f} yuan")
    print(f"Optimized annual power generation: {value2:.2f} kWh")
    
    # 计算经济效益
    print("\nEconomic Analysis")
    print("-" * 40)
    
    # 年发电量
    year_value = value1 * 40 * 0.94 / 42 + value1 * 2 * 0.86 / 42 + 0.94 * (value2 + value1 + value1)
    year_electricity = year_value * 2
    
    # 总成本
    total_cost = cost1 + cost2 + cost1 + cost1
    
    # 总价值
    total_value = year_value * (10 + 15 * 0.9 + 10 * 0.8)
    total_electricity = 2 * total_value
    
    print(f"Annual power generation: {year_value:.2f} kWh")
    print(f"Annual electricity value: {year_electricity:.2f} yuan")
    print(f"Total cost: {total_cost:.2f} yuan")
    print(f"Total value: {total_value:.2f} yuan")
    print(f"Total electricity value: {total_electricity:.2f} yuan")
    
    # 投资回报率
    roi = (total_electricity - total_cost) / total_cost * 100
    print(f"Return on investment: {roi:.2f}%")
    
    return {
        'cost': total_cost,
        'value': total_value,
        'electricity': total_electricity,
        'roi': roi
    }

if __name__ == "__main__":
    result = solar_house_design()
    print("\n" + "=" * 60)
    print("Solar house design analysis completed!")
    print("=" * 60)