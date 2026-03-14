import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def ethanol_to_olefins():
    """
    乙醇偶合制备烯烃问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Ethanol to Olefins")
    print("=" * 60)
    
    # 问题1：乙醇转化率拟合
    print("\nProblem 1: Ethanol Conversion Rate Fitting")
    print("-" * 40)
    
    # 实验数据（示例数据）
    X = np.array([20, 70, 110, 163, 197, 240, 273])
    YC = np.array([43.5, 37.8, 36.6, 32.7, 31.7, 29.9, 29.9])
    
    print("Experimental data:")
    print(f"Temperature (°C): {X}")
    print(f"Conversion rate (%): {YC}")
    
    # 定义拟合函数：f(x) = a + b * exp(-c * x)
    def fit_function(x, a, b, c):
        return a + b * np.exp(-c * x)
    
    # 定义误差函数
    def error_function(params):
        a, b, c = params
        predicted = fit_function(X, a, b, c)
        error = np.sum((predicted - YC)**2)
        return error
    
    # 初始猜测
    initial_guess = [30, 20, 0.01]
    
    # 优化
    result = minimize(error_function, initial_guess, method='Nelder-Mead')
    
    if result.success:
        a_opt, b_opt, c_opt = result.x
        print(f"\nOptimization successful!")
        print(f"Optimal parameters: a = {a_opt:.4f}, b = {b_opt:.4f}, c = {c_opt:.6f}")
        print(f"Minimum error: {result.fun:.4f}")
        
        # 计算拟合值
        X_fit = np.linspace(min(X), max(X), 100)
        Y_fit = fit_function(X_fit, a_opt, b_opt, c_opt)
        
        # 绘制拟合曲线
        plt.figure(figsize=(10, 6))
        plt.scatter(X, YC, c='r', s=100, label='Experimental Data')
        plt.plot(X_fit, Y_fit, 'b-', linewidth=2, label=f'Fitted Curve: y = {a_opt:.2f} + {b_opt:.2f} * exp(-{c_opt:.4f}x)')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Conversion Rate (%)')
        plt.title('Ethanol Conversion Rate vs Temperature')
        plt.legend()
        plt.grid(True)
        plt.savefig('ethanol_conversion_fitting.png')
        plt.close()
        
        print("Fitting plot saved as 'ethanol_conversion_fitting.png'")
    else:
        print("Optimization failed!")
        print(result.message)
    
    # 问题2：不同温度下的转化率预测
    print("\nProblem 2: Conversion Rate Prediction at Different Temperatures")
    print("-" * 40)
    
    if result.success:
        # 预测不同温度下的转化率
        temperatures = np.array([50, 100, 150, 200, 250, 300])
        predicted_rates = fit_function(temperatures, a_opt, b_opt, c_opt)
        
        print("Predicted conversion rates:")
        for temp, rate in zip(temperatures, predicted_rates):
            print(f"Temperature: {temp}°C, Conversion rate: {rate:.2f}%")
        
        # 绘制预测曲线
        plt.figure(figsize=(10, 6))
        plt.plot(X_fit, Y_fit, 'b-', linewidth=2, label='Fitted Curve')
        plt.scatter(temperatures, predicted_rates, c='g', s=100, marker='s', label='Predicted Points')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Conversion Rate (%)')
        plt.title('Ethanol Conversion Rate Prediction')
        plt.legend()
        plt.grid(True)
        plt.savefig('ethanol_conversion_prediction.png')
        plt.close()
        
        print("Prediction plot saved as 'ethanol_conversion_prediction.png'")
    
    # 问题3：优化反应条件
    print("\nProblem 3: Optimal Reaction Conditions")
    print("-" * 40)
    
    if result.success:
        # 寻找最优温度范围
        # 目标：最大化转化率
        def objective_function_optimization(temp):
            rate = fit_function(temp, a_opt, b_opt, c_opt)
            return -rate  # 最小化负转化率 = 最大化转化率
        
        # 在合理温度范围内搜索
        temp_range = np.linspace(20, 300, 1000)
        rates = fit_function(temp_range, a_opt, b_opt, c_opt)
        
        optimal_temp = temp_range[np.argmax(rates)]
        optimal_rate = np.max(rates)
        
        print(f"Optimal temperature: {optimal_temp:.2f}°C")
        print(f"Maximum conversion rate: {optimal_rate:.2f}%")
        
        # 绘制转化率随温度变化曲线
        plt.figure(figsize=(10, 6))
        plt.plot(temp_range, rates, 'b-', linewidth=2)
        plt.axvline(x=optimal_temp, color='r', linestyle='--', label=f'Optimal Temp: {optimal_temp:.2f}°C')
        plt.axhline(y=optimal_rate, color='g', linestyle='--', label=f'Max Rate: {optimal_rate:.2f}%')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Conversion Rate (%)')
        plt.title('Ethanol Conversion Rate vs Temperature')
        plt.legend()
        plt.grid(True)
        plt.savefig('ethanol_conversion_optimization.png')
        plt.close()
        
        print("Optimization plot saved as 'ethanol_conversion_optimization.png'")
    
    # 问题4：误差分析
    print("\nProblem 4: Error Analysis")
    print("-" * 40)
    
    if result.success:
        # 计算拟合误差
        predicted_values = fit_function(X, a_opt, b_opt, c_opt)
        errors = predicted_values - YC
        relative_errors = errors / YC * 100
        
        print(f"Absolute errors: {errors}")
        print(f"Relative errors (%): {relative_errors}")
        print(f"Mean absolute error: {np.mean(np.abs(errors)):.4f}")
        print(f"Mean relative error: {np.mean(np.abs(relative_errors)):.2f}%")
        print(f"Maximum absolute error: {np.max(np.abs(errors)):.4f}")
        print(f"Maximum relative error: {np.max(np.abs(relative_errors)):.2f}%")
        
        # 绘制误差分布
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(errors)), errors, color='b', alpha=0.7)
        plt.axhline(y=0, color='r', linestyle='--')
        plt.xlabel('Data Point')
        plt.ylabel('Absolute Error')
        plt.title('Fitting Error Distribution')
        plt.grid(True)
        plt.savefig('ethanol_conversion_error.png')
        plt.close()
        
        print("Error distribution plot saved as 'ethanol_conversion_error.png'")
    
    return {
        'a': a_opt if result.success else None,
        'b': b_opt if result.success else None,
        'c': c_opt if result.success else None,
        'min_error': result.fun if result.success else None
    }

if __name__ == "__main__":
    result = ethanol_to_olefins()
    print("\n" + "=" * 60)
    print("Ethanol to olefins analysis completed!")
    print("=" * 60)