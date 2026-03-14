import numpy as np
from scipy.optimize import minimize

def natural_casing_optimization():
    """
    天然肠衣搭配优化问题
    基于LINGO模型的Python实现
    """
    
    print("Problem: Natural Casing Matching Optimization")
    print("=" * 60)
    
    # 定义肠衣参数（示例数据，需要根据实际情况调整）
    # 这里使用简化的模型，实际应用中需要从数据文件读取
    
    # 假设有109种肠衣规格
    num_casings = 109
    num_groups = 6
    
    # 肠衣参数（示例数据）
    # a: 肠衣长度
    # b: 变动费用
    # c: 天数间隔
    a = np.random.uniform(10, 30, num_casings)  # 肠衣长度
    b = np.random.uniform(100, 500, num_casings)  # 变动费用
    c = np.random.uniform(1, 10, num_casings)  # 天数间隔
    
    # 决策变量：f[i,j]表示第i组是否使用第j种肠衣
    # p[i,j]表示第i组是否采购第j种肠衣
    
    # 目标函数：最大化利润
    def objective(x):
        # x包含f和p的决策变量
        # 简化的目标函数
        f = x[:num_groups * num_casings].reshape(num_groups, num_casings)
        p = x[num_groups * num_casings:].reshape(num_groups, num_casings)
        
        # 收入
        revenue = np.sum(a * f * 100 * 8479) + 8479 * a[1]
        
        # 采购成本
        purchase_cost = np.sum((c * f - c * p) * 8479 * 1.5 * 3) + 8479 * 130 * 1.5 * 3
        
        # 变动费用
        variable_cost = np.sum(f * 8479 * b) + 1503 * 120
        
        # 利润 = 收入 - 成本
        profit = revenue - purchase_cost - variable_cost
        
        return -profit  # 最小化负利润 = 最大化利润
    
    # 约束条件
    def constraints(x):
        f = x[:num_groups * num_casings].reshape(num_groups, num_casings)
        p = x[num_groups * num_casings:].reshape(num_groups, num_casings)
        
        constraints_list = []
        
        # 每组的净肠衣数量 >= 150
        for i in range(num_groups):
            constraints_list.append(np.sum(c * f[i] - c * p[i]) - 150)
        
        # 连续组之间的增量约束
        for i in range(num_groups - 1):
            constraints_list.append(np.sum(c * f[i+1] - c * f[i]) - 150)
            constraints_list.append(np.sum(c * p[i+1] - c * p[i]) - 180)
        
        # 每组最多使用一种肠衣
        for i in range(num_groups):
            constraints_list.append(np.sum(f[i]) - 1)
            constraints_list.append(np.sum(p[i]) - 1)
        
        return np.array(constraints_list)
    
    # 初始猜测
    x0 = np.zeros(2 * num_groups * num_casings)
    
    # 边界条件（0-1变量）
    bounds = [(0, 1)] * (2 * num_groups * num_casings)
    
    # 约束
    cons = {'type': 'ineq', 'fun': constraints}
    
    # 优化
    result = minimize(objective, x0, method='SLSQP', bounds=bounds, 
                    constraints=cons, options={'maxiter': 1000})
    
    if result.success:
        print("Optimization successful!")
        print(f"Maximum profit: {-result.fun:.2f}")
        
        # 解析结果
        f_opt = result.x[:num_groups * num_casings].reshape(num_groups, num_casings)
        p_opt = result.x[num_groups * num_casings:].reshape(num_groups, num_casings)
        
        print("\nOptimal casing allocation:")
        for i in range(num_groups):
            selected_f = np.where(f_opt[i] > 0.5)[0]
            selected_p = np.where(p_opt[i] > 0.5)[0]
            print(f"Group {i+1}: Use casing {selected_f}, Purchase casing {selected_p}")
    else:
        print("Optimization failed!")
        print(result.message)
    
    return result

if __name__ == "__main__":
    natural_casing_optimization()