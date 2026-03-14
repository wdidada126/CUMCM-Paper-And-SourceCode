import numpy as np
import matplotlib.pyplot as plt

def robot_obstacle_avoidance():
    """
    机器人避障问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Robot Obstacle Avoidance")
    print("=" * 60)
    
    # 定义障碍物坐标
    # 障碍物1：正方形
    obstacle1 = np.array([
        [300, 400], [300, 500], [400, 500], [400, 400]
    ])
    
    # 障碍物2：圆形，圆心(550, 600)，半径70
    obstacle2_center = np.array([550, 600])
    obstacle2_radius = 70
    
    # 障碍物3：平行四边形
    obstacle3 = np.array([
        [720, 400], [720, 500], [800, 400], [800, 300]
    ])
    
    # 障碍物4：三角形
    obstacle4 = np.array([
        [600, 300], [650, 400], [700, 300]
    ])
    
    # 障碍物5：正方形
    obstacle5 = np.array([
        [50, 600], [50, 700], [150, 700], [150, 600]
    ])
    
    # 问题1：从起点(0,0)到终点(300,300)的最短路径
    print("\nProblem 1: Shortest path from (0,0) to (300,300)")
    print("-" * 40)
    
    start = np.array([0, 0])
    end = np.array([300, 300])
    
    # 方法1：直接路径（无障碍物）
    direct_distance = np.linalg.norm(end - start)
    print(f"Direct distance: {direct_distance:.2f}")
    
    # 方法2：绕过障碍物1
    # 路径：起点 -> 障碍物1左上角 -> 终点
    path1 = np.array([
        [0, 0],
        [300, 400],
        [300, 300]
    ])
    distance1 = np.sum(np.linalg.norm(np.diff(path1, axis=0), axis=1))
    print(f"Path 1 (via obstacle 1): {distance1:.2f}")
    
    # 方法3：绕过障碍物1的另一个方向
    path2 = np.array([
        [0, 0],
        [400, 400],
        [300, 300]
    ])
    distance2 = np.sum(np.linalg.norm(np.diff(path2, axis=0), axis=1))
    print(f"Path 2 (via obstacle 1 alternative): {distance2:.2f}")
    
    # 绘制路径
    plt.figure(figsize=(10, 10))
    
    # 绘制障碍物
    plt.fill(obstacle1[:, 0], obstacle1[:, 1], 'r', alpha=0.3, label='Obstacle 1')
    
    # 绘制障碍物2（圆形）
    theta = np.linspace(0, 2*np.pi, 100)
    circle_x = obstacle2_center[0] + obstacle2_radius * np.cos(theta)
    circle_y = obstacle2_center[1] + obstacle2_radius * np.sin(theta)
    plt.fill(circle_x, circle_y, 'g', alpha=0.3, label='Obstacle 2')
    
    # 绘制障碍物3
    plt.fill(obstacle3[:, 0], obstacle3[:, 1], 'b', alpha=0.3, label='Obstacle 3')
    
    # 绘制障碍物4
    plt.fill(obstacle4[:, 0], obstacle4[:, 1], 'y', alpha=0.3, label='Obstacle 4')
    
    # 绘制障碍物5
    plt.fill(obstacle5[:, 0], obstacle5[:, 1], 'm', alpha=0.3, label='Obstacle 5')
    
    # 绘制路径
    plt.plot(path1[:, 0], path1[:, 1], 'r--', linewidth=2, label='Path 1')
    plt.plot(path2[:, 0], path2[:, 1], 'b--', linewidth=2, label='Path 2')
    
    # 绘制起点和终点
    plt.plot(start[0], start[1], 'go', markersize=10, label='Start')
    plt.plot(end[0], end[1], 'ro', markersize=10, label='End')
    
    plt.xlim(-50, 900)
    plt.ylim(-50, 800)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Robot Obstacle Avoidance - Problem 1')
    plt.legend()
    plt.grid(True)
    plt.savefig('robot_obstacle_avoidance_p1.png')
    plt.close()
    
    print("Path plot saved as 'robot_obstacle_avoidance_p1.png'")
    
    # 问题2：从起点(70, 630)到终点(530, 140)的最短路径
    print("\nProblem 2: Shortest path from (70,630) to (530,140)")
    print("-" * 40)
    
    start2 = np.array([70, 630])
    end2 = np.array([530, 140])
    
    # 绕过障碍物5和障碍物2
    path3 = np.array([
        [70, 630],
        [50, 700],
        [50, 800],
        [600, 800],
        [600, 670],
        [530, 140]
    ])
    distance3 = np.sum(np.linalg.norm(np.diff(path3, axis=0), axis=1))
    print(f"Path 3 (via obstacles 5 and 2): {distance3:.2f}")
    
    # 绘制问题2的路径
    plt.figure(figsize=(10, 10))
    
    # 绘制障碍物
    plt.fill(obstacle1[:, 0], obstacle1[:, 1], 'r', alpha=0.3, label='Obstacle 1')
    plt.fill(circle_x, circle_y, 'g', alpha=0.3, label='Obstacle 2')
    plt.fill(obstacle3[:, 0], obstacle3[:, 1], 'b', alpha=0.3, label='Obstacle 3')
    plt.fill(obstacle4[:, 0], obstacle4[:, 1], 'y', alpha=0.3, label='Obstacle 4')
    plt.fill(obstacle5[:, 0], obstacle5[:, 1], 'm', alpha=0.3, label='Obstacle 5')
    
    # 绘制路径
    plt.plot(path3[:, 0], path3[:, 1], 'r--', linewidth=2, label='Path 3')
    
    # 绘制起点和终点
    plt.plot(start2[0], start2[1], 'go', markersize=10, label='Start')
    plt.plot(end2[0], end2[1], 'ro', markersize=10, label='End')
    
    plt.xlim(-50, 900)
    plt.ylim(-50, 900)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Robot Obstacle Avoidance - Problem 2')
    plt.legend()
    plt.grid(True)
    plt.savefig('robot_obstacle_avoidance_p2.png')
    plt.close()
    
    print("Path plot saved as 'robot_obstacle_avoidance_p2.png'")
    
    return {
        'p1_distance': min(distance1, distance2),
        'p2_distance': distance3
    }

if __name__ == "__main__":
    result = robot_obstacle_avoidance()
    print("\n" + "=" * 60)
    print("Robot obstacle avoidance analysis completed!")
    print("=" * 60)