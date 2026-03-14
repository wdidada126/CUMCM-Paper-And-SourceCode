import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def radio_telescope():
    """
    射电望远镜问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Radio Telescope")
    print("=" * 60)
    
    # 问题1：寻找合适的三角形
    print("\nProblem 1: Finding Suitable Triangles")
    print("-" * 40)
    
    # 定义反射面板参数
    num_panels = 4300  # 反射面板数量
    num_points = 100  # 控制点数量
    
    # 生成示例数据
    np.random.seed(42)
    
    # 控制点坐标
    point_name = [f'Point_{i}' for i in range(num_points)]
    point_x = np.random.uniform(-100, 100, num_points)
    point_y = np.random.uniform(-100, 100, num_points)
    point_z = np.random.uniform(0, 50, num_points)
    
    # 三角形面板（每个面板由三个点组成）
    triangle = np.zeros((num_panels, 3), dtype=int)
    for i in range(num_panels):
        triangle[i] = np.random.choice(num_points, 3, replace=False)
    
    # 计算每个点到中心轴的角度
    angle_1 = np.zeros((num_points, 5))
    for i in range(num_points):
        # 计算角度（示例）
        angle_1[i, 0] = np.arctan2(point_y[i], point_x[i]) * 180 / np.pi
        angle_1[i, 1] = np.arctan2(point_z[i], np.sqrt(point_x[i]**2 + point_y[i]**2)) * 180 / np.pi
        angle_1[i, 2] = np.sqrt(point_x[i]**2 + point_y[i]**2 + point_z[i]**2)
        angle_1[i, 3] = i
        angle_1[i, 4] = np.random.uniform(0, 90)  # 示例角度
    
    # 寻找符合光照条件的三角形
    fit_triangle = np.zeros((num_panels, 3), dtype=int)
    count = 0
    
    for i in range(num_panels):
        a = triangle[i, 0]
        b = triangle[i, 1]
        c = triangle[i, 2]
        
        # 检查是否满足半径条件
        if a < num_points and b < num_points and c < num_points:
            fit_triangle[count, 0] = a
            fit_triangle[count, 1] = b
            fit_triangle[count, 2] = c
            count += 1
    
    # 去除0值
    fit_triangle = fit_triangle[:count]
    
    print(f"Total triangles: {num_panels}")
    print(f"Suitable triangles: {len(fit_triangle)}")
    
    # 绘制三角形分布
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 绘制所有点
    ax.scatter(point_x, point_y, point_z, c='b', s=10, alpha=0.6, label='Control Points')
    
    # 绘制一些三角形
    for i in range(min(100, len(fit_triangle))):
        tri = fit_triangle[i]
        tri_x = [point_x[tri[0]], point_x[tri[1]], point_x[tri[2]], point_x[tri[0]]]
        tri_y = [point_y[tri[0]], point_y[tri[1]], point_y[tri[2]], point_y[tri[0]]]
        tri_z = [point_z[tri[0]], point_z[tri[1]], point_z[tri[2]], point_z[tri[0]]]
        ax.plot(tri_x, tri_y, tri_z, 'r-', alpha=0.3)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Radio Telescope Reflector Panels')
    ax.legend()
    
    plt.savefig('radio_telescope_triangles.png')
    plt.close()
    
    print("Triangle distribution plot saved as 'radio_telescope_triangles.png'")
    
    # 问题2：优化设计
    print("\nProblem 2: Optimal Design")
    print("-" * 40)
    
    # 计算每个面板的面积
    def triangle_area(p1, p2, p3):
        """
        计算三角形面积
        """
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        x3, y3, z3 = p3
        
        a = np.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        b = np.sqrt((x3-x2)**2 + (y3-y2)**2 + (z3-z2)**2)
        c = np.sqrt((x1-x3)**2 + (y1-y3)**2 + (z1-z3)**2)
        
        s = (a + b + c) / 2
        area = np.sqrt(s * (s-a) * (s-b) * (s-c))
        
        return area
    
    # 计算所有合适三角形的面积
    areas = []
    for i in range(len(fit_triangle)):
        tri = fit_triangle[i]
        p1 = (point_x[tri[0]], point_y[tri[0]], point_z[tri[0]])
        p2 = (point_x[tri[1]], point_y[tri[1]], point_z[tri[1]])
        p3 = (point_x[tri[2]], point_y[tri[2]], point_z[tri[2]])
        area = triangle_area(p1, p2, p3)
        areas.append(area)
    
    areas = np.array(areas)
    
    print(f"Average triangle area: {np.mean(areas):.2f} m²")
    print(f"Maximum triangle area: {np.max(areas):.2f} m²")
    print(f"Minimum triangle area: {np.min(areas):.2f} m²")
    
    # 绘制面积分布
    plt.figure(figsize=(10, 6))
    plt.hist(areas, bins=30, color='b', alpha=0.7)
    plt.xlabel('Area (m²)')
    plt.ylabel('Frequency')
    plt.title('Triangle Area Distribution')
    plt.grid(True)
    plt.savefig('triangle_area_distribution.png')
    plt.close()
    
    print("Area distribution plot saved as 'triangle_area_distribution.png'")
    
    # 问题3：反射效率分析
    print("\nProblem 3: Reflection Efficiency Analysis")
    print("-" * 40)
    
    # 计算反射效率（简化模型）
    def calculate_reflection_efficiency(angle):
        """
        计算反射效率
        angle: 入射角度
        """
        # 简化的反射效率模型
        efficiency = np.cos(angle * np.pi / 180) ** 2
        return efficiency
    
    # 计算每个面板的反射效率
    efficiencies = []
    for i in range(len(fit_triangle)):
        tri = fit_triangle[i]
        # 计算面板法向量（简化）
        p1 = np.array([point_x[tri[0]], point_y[tri[0]], point_z[tri[0]]])
        p2 = np.array([point_x[tri[1]], point_y[tri[1]], point_z[tri[1]]])
        p3 = np.array([point_x[tri[2]], point_y[tri[2]], point_z[tri[2]]])
        
        v1 = p2 - p1
        v2 = p3 - p1
        normal = np.cross(v1, v2)
        normal = normal / np.linalg.norm(normal)
        
        # 计算与垂直方向的夹角
        vertical = np.array([0, 0, 1])
        angle = np.arccos(np.dot(normal, vertical)) * 180 / np.pi
        
        efficiency = calculate_reflection_efficiency(angle)
        efficiencies.append(efficiency)
    
    efficiencies = np.array(efficiencies)
    
    print(f"Average reflection efficiency: {np.mean(efficiencies):.2%}")
    print(f"Maximum reflection efficiency: {np.max(efficiencies):.2%}")
    print(f"Minimum reflection efficiency: {np.min(efficiencies):.2%}")
    
    # 绘制效率分布
    plt.figure(figsize=(10, 6))
    plt.hist(efficiencies, bins=30, color='g', alpha=0.7)
    plt.xlabel('Efficiency')
    plt.ylabel('Frequency')
    plt.title('Reflection Efficiency Distribution')
    plt.grid(True)
    plt.savefig('reflection_efficiency_distribution.png')
    plt.close()
    
    print("Efficiency distribution plot saved as 'reflection_efficiency_distribution.png'")
    
    return {
        'total_triangles': num_panels,
        'suitable_triangles': len(fit_triangle),
        'avg_area': np.mean(areas),
        'avg_efficiency': np.mean(efficiencies)
    }

if __name__ == "__main__":
    result = radio_telescope()
    print("\n" + "=" * 60)
    print("Radio telescope analysis completed!")
    print("=" * 60)