import numpy as np
from scipy.optimize import minimize

def pig_farming_management():
    """
    生猪养殖管理问题
    基于LINGO代码的Python实现
    """
    print("Problem: Pig Farming Management")
    print("=" * 60)
    
    # 定义参数
    num_days = 365  # 一年365天
    
    # 养殖参数
    initial_pigs = 100  # 初始猪数量
    max_pigs = 10000  # 最大猪数量
    growth_rate = 0.02  # 日增长率
    feed_cost_per_pig = 5  # 每头猪每天饲料成本
    selling_price = 1500  # 每头猪售价
    purchase_price = 800  # 每头猪购买价格
    
    # 问题1：最优出栏策略
    print("\nProblem 1: Optimal Selling Strategy")
    print("-" * 40)
    
    def objective_function(x):
        """
        目标函数：最大化利润
        x: 决策变量，表示每天卖出的猪数量
        """
        total_profit = 0
        current_pigs = initial_pigs
        
        for day in range(num_days):
            # 卖猪收入
            selling_revenue = x[day] * selling_price
            
            # 买猪成本
            purchase_cost = 0  # 假设不买猪
            
            # 饲料成本
            feed_cost = current_pigs * feed_cost_per_pig
            
            # 净利润
            daily_profit = selling_revenue - purchase_cost - feed_cost
            total_profit += daily_profit
            
            # 更新猪数量
            current_pigs = current_pigs - x[day] + current_pigs * growth_rate
            current_pigs = min(current_pigs, max_pigs)
        
        return -total_profit  # 最小化负利润 = 最大化利润
    
    # 约束条件
    def constraints(x):
        """
        约束条件：
        1. 每天卖出的猪数量 >= 0
        2. 每天卖出的猪数量 <= 当前猪数量
        3. 总猪数量不超过最大值
        """
        constraints_list = []
        
        current_pigs = initial_pigs
        for day in range(num_days):
            # 每天卖出的猪数量 >= 0
            constraints_list.append(x[day])
            
            # 每天卖出的猪数量 <= 当前猪数量
            constraints_list.append(current_pigs - x[day])
            
            # 更新猪数量
            current_pigs = current_pigs - x[day] + current_pigs * growth_rate
            current_pigs = min(current_pigs, max_pigs)
        
        return np.array(constraints_list)
    
    # 初始猜测
    x0 = np.zeros(num_days)
    
    # 边界条件
    bounds = [(0, max_pigs)] * num_days
    
    # 约束
    cons = {'type': 'ineq', 'fun': constraints}
    
    # 优化（简化版，只优化关键决策点）
    # 为了简化计算，我们只优化每周的决策
    num_weeks = 52
    x_weekly = np.zeros(num_weeks)
    
    def objective_function_weekly(x):
        total_profit = 0
        current_pigs = initial_pigs
        
        for week in range(num_weeks):
            # 这周卖猪收入
            selling_revenue = x[week] * selling_price
            
            # 这周饲料成本
            feed_cost = current_pigs * feed_cost_per_pig * 7
            
            # 净利润
            weekly_profit = selling_revenue - feed_cost
            total_profit += weekly_profit
            
            # 更新猪数量
            current_pigs = current_pigs - x[week] + current_pigs * growth_rate * 7
            current_pigs = min(current_pigs, max_pigs)
        
        return -total_profit
    
    # 简化的约束
    def constraints_weekly(x):
        constraints_list = []
        current_pigs = initial_pigs
        
        for week in range(num_weeks):
            constraints_list.append(x[week])
            constraints_list.append(current_pigs - x[week])
            current_pigs = current_pigs - x[week] + current_pigs * growth_rate * 7
            current_pigs = min(current_pigs, max_pigs)
        
        return np.array(constraints_list)
    
    x0_weekly = np.zeros(num_weeks)
    bounds_weekly = [(0, max_pigs)] * num_weeks
    cons_weekly = {'type': 'ineq', 'fun': constraints_weekly}
    
    result = minimize(objective_function_weekly, x0_weekly, method='SLSQP',
                    bounds=bounds_weekly, constraints=cons_weekly,
                    options={'maxiter': 1000})
    
    if result.success:
        print("Optimization successful!")
        print(f"Maximum profit: {-result.fun:.2f} yuan")
        print(f"Total pigs sold: {np.sum(result.x):.0f}")
        
        # 计算最终猪数量
        final_pigs = initial_pigs
        for week in range(num_weeks):
            final_pigs = final_pigs - result.x[week] + final_pigs * growth_rate * 7
            final_pigs = min(final_pigs, max_pigs)
        
        print(f"Final pig count: {final_pigs:.0f}")
    else:
        print("Optimization failed!")
        print(result.message)
    
    # 问题2：不同策略比较
    print("\nProblem 2: Strategy Comparison")
    print("-" * 40)
    
    # 策略1：定期出栏
    def strategy_regular():
        current_pigs = initial_pigs
        total_profit = 0
        
        for day in range(num_days):
            # 每周出栏一次
            if day % 7 == 0 and day > 0:
                sell_amount = min(current_pigs * 0.1, 100)
                selling_revenue = sell_amount * selling_price
                total_profit += selling_revenue
                current_pigs -= sell_amount
            
            # 饲料成本
            feed_cost = current_pigs * feed_cost_per_pig
            total_profit -= feed_cost
            
            # 增长
            current_pigs = current_pigs * (1 + growth_rate)
            current_pigs = min(current_pigs, max_pigs)
        
        return total_profit, current_pigs
    
    # 策略2：达到目标数量出栏
    def strategy_target():
        current_pigs = initial_pigs
        total_profit = 0
        target = 5000
        
        for day in range(num_days):
            # 达到目标数量出栏
            if current_pigs >= target:
                sell_amount = current_pigs - target
                selling_revenue = sell_amount * selling_price
                total_profit += selling_revenue
                current_pigs = target
            
            # 饲料成本
            feed_cost = current_pigs * feed_cost_per_pig
            total_profit -= feed_cost
            
            # 增长
            current_pigs = current_pigs * (1 + growth_rate)
            current_pigs = min(current_pigs, max_pigs)
        
        return total_profit, current_pigs
    
    profit1, pigs1 = strategy_regular()
    profit2, pigs2 = strategy_target()
    
    print(f"Strategy 1 (Regular selling): Profit = {profit1:.2f} yuan, Final pigs = {pigs1:.0f}")
    print(f"Strategy 2 (Target-based): Profit = {profit2:.2f} yuan, Final pigs = {pigs2:.0f}")
    
    return {
        'optimal_profit': -result.fun if result.success else None,
        'regular_profit': profit1,
        'target_profit': profit2
    }

if __name__ == "__main__":
    result = pig_farming_management()
    print("\n" + "=" * 60)
    print("Pig farming management analysis completed!")
    print("=" * 60)