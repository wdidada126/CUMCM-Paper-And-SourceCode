import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def pagoda_deformation_analysis():
    """
    古塔变形分析问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Pagoda Deformation Analysis")
    print("=" * 60)
    
    # 问题1：建立古塔变形模型
    print("\nProblem 1: Pagoda Deformation Model")
    print("-" * 40)
    
    # 定义古塔各层中心点坐标（示例数据）
    # x, y, z: 三维坐标
    layers = 13
    x = np.array([
        5.542, 5.544, 5.546, 5.548, 5.550, 5.552, 5.554, 
        5.556, 5.558, 5.560, 5.562, 5.564, 5.566
    ])
    y = np.array([
        5.542, 5.544, 5.546, 5.548, 5.550, 5.552, 5.554, 
        5.556, 5.558, 5.560, 5.562, 5.564, 5.566
    ])
    z = np.array([
        52.826, 52.670, 52.514, 52.358, 52.202, 52.046, 51.890,
        51.734, 51.578, 51.422, 51.266, 51.110, 50.954
    ])
    
    # 计算各层中心点的偏移
    x_offset = x - x[0]
    y_offset = y - y[0]
    z_offset = z - z[0]
    
    print(f"X offset: {x_offset}")
    print(f"Y offset: {y_offset}")
    print(f"Z offset: {z_offset}")
    
    # 计算倾斜角度
    def calculate_tilt_angle(x, y, z):
        """
        计算古塔的倾斜角度
        """
        # 使用最小二乘法拟合直线
        A = np.vstack([x, y, np.ones_like(x)]).T
        b = z
        
        # 拟合平面 z = ax + by + c
        coeffs, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
        a, b, c = coeffs
        
        # 计算倾斜角度
        tilt_angle = np.arctan(np.sqrt(a**2 + b**2)) * 180 / np.pi
        
        return tilt_angle, coeffs
    
    tilt_angle, coeffs = calculate_tilt_angle(x, y, z)
    print(f"Tilt angle: {tilt_angle:.4f} degrees")
    print(f"Plane coefficients: a={coeffs[0]:.6f}, b={coeffs[1]:.6f}, c={coeffs[2]:.6f}")
    
    # 问题2：分析古塔变形趋势
    print("\nProblem 2: Deformation Trend Analysis")
    print("-" * 40)
    
    # 计算各层的变形量
    deformation = np.sqrt(x_offset**2 + y_offset**2 + z_offset**2)
    print(f"Deformation at each layer: {deformation}")
    
    # 计算变形速率
    deformation_rate = np.diff(deformation)
    print(f"Deformation rate: {deformation_rate}")
    
    # 绘制古塔变形图
    fig = plt.figure(figsize=(15, 10))
    
    # 3D视图
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.scatter(x, y, z, c=range(layers), cmap='viridis', s=100)
    ax1.set_xlabel('X (m)')
    ax1.set_ylabel('Y (m)')
    ax1.set_zlabel('Z (m)')
    ax1.set_title('Pagoda 3D Structure')
    
    # X方向偏移
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(range(layers), x_offset, 'ro-', linewidth=2, markersize=8)
    ax2.set_xlabel('Layer')
    ax2.set_ylabel('X Offset (m)')
    ax2.set_title('X Direction Offset')
    ax2.grid(True)
    
    # Y方向偏移
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.plot(range(layers), y_offset, 'bo-', linewidth=2, markersize=8)
    ax3.set_xlabel('Layer')
    ax3.set_ylabel('Y Offset (m)')
    ax3.set_title('Y Direction Offset')
    ax3.grid(True)
    
    # 总变形量
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(range(layers), deformation, 'go-', linewidth=2, markersize=8)
    ax4.set_xlabel('Layer')
    ax4.set_ylabel('Total Deformation (m)')
    ax4.set_title('Total Deformation')
    ax4.grid(True)
    
    plt.tight_layout()
    plt.savefig('pagoda_deformation_analysis.png')
    plt.close()
    
    print("Pagoda deformation plot saved as 'pagoda_deformation_analysis.png'")
    
    # 问题3：预测未来变形
    print("\nProblem 3: Future Deformation Prediction")
    print("-" * 40)
    
    # 使用线性回归预测未来变形
    def predict_deformation(x, y, z, future_years=10):
        """
        预测未来变形
        """
        # 计算每年的变形速率（假设数据来自不同年份）
        years = np.array([1986, 1996, 2009, 2011])  # 示例年份
        deformation_data = np.array([
            np.sqrt(x[0]**2 + y[0]**2 + z[0]**2),
            np.sqrt(x[4]**2 + y[4]**2 + z[4]**2),
            np.sqrt(x[8]**2 + y[8]**2 + z[8]**2),
            np.sqrt(x[12]**2 + y[12]**2 + z[12]**2)
        ])
        
        # 线性回归
        coeffs = np.polyfit(years, deformation_data, 1)
        poly = np.poly1d(coeffs)
        
        # 预测未来变形
        future_years_array = np.arange(2011, 2011 + future_years + 1)
        predicted_deformation = poly(future_years_array)
        
        return future_years_array, predicted_deformation, coeffs
    
    future_years, predicted_deformation, coeffs = predict_deformation(x, y, z)
    print(f"Regression coefficients: slope={coeffs[0]:.6f}, intercept={coeffs[1]:.6f}")
    print(f"Predicted deformation in {future_years[-1]}: {predicted_deformation[-1]:.6f} m")
    
    # 绘制预测结果
    plt.figure(figsize=(10, 6))
    plt.plot(future_years, predicted_deformation, 'r-', linewidth=2, label='Predicted')
    plt.scatter([1986, 1996, 2009, 2011], 
               [np.sqrt(x[0]**2 + y[0]**2 + z[0]**2),
                np.sqrt(x[4]**2 + y[4]**2 + z[4]**2),
                np.sqrt(x[8]**2 + y[8]**2 + z[8]**2),
                np.sqrt(x[12]**2 + y[12]**2 + z[12]**2)],
               c='b', s=100, label='Measured')
    plt.xlabel('Year')
    plt.ylabel('Deformation (m)')
    plt.title('Pagoda Deformation Prediction')
    plt.legend()
    plt.grid(True)
    plt.savefig('pagoda_deformation_prediction.png')
    plt.close()
    
    print("Deformation prediction plot saved as 'pagoda_deformation_prediction.png'")
    
    return {
        'tilt_angle': tilt_angle,
        'deformation': deformation,
        'predicted_deformation': predicted_deformation[-1]
    }

if __name__ == "__main__":
    result = pagoda_deformation_analysis()
    print("\n" + "=" * 60)
    print("Pagoda deformation analysis completed!")
    print("=" * 60)