import numpy as np
import matplotlib.pyplot as plt

def traffic_capacity_analysis():
    """
    道路通行能力分析问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Traffic Capacity Analysis")
    print("=" * 60)
    
    # 问题1：视频分析
    print("\nProblem 1: Video Analysis")
    print("-" * 40)
    
    # 模拟视频处理（需要OpenCV处理实际视频）
    # 这里使用模拟数据
    
    # 视频参数
    n_frames = 10000
    vid_height = 480
    vid_width = 640
    
    # 模拟帧处理
    K = 0.90
    M = 30
    
    # 模拟背景差分
    C1 = np.random.randint(0, 256, (vid_height, vid_width))
    B1 = np.zeros((vid_height, vid_width))
    
    vehicle_count = 0
    
    # 模拟处理每15帧
    for i in range(4960, n_frames, 15):
        # 模拟当前帧
        C = np.random.randint(0, 256, (vid_height, vid_width))
        
        # 背景差分
        B = K * B1 + (1 - K) * C1
        D = C - B
        
        # 阈值化
        D[D > M] = 255
        D[D <= M] = 0
        
        # 车辆检测（简化）
        if np.sum(D > 0) > 10000:
            vehicle_count += 1
        
        C1 = C
        B1 = B
    
    print(f"Detected vehicles: {vehicle_count}")
    
    # 问题2：通行能力计算
    print("\nProblem 2: Traffic Capacity Calculation")
    print("-" * 40)
    
    # 道路参数
    lane_width = 3.75  # 车道宽度（米）
    num_lanes = 3  # 车道数
    road_length = 100  # 道路长度（米）
    
    # 车辆参数
    vehicle_length = 5  # 车辆长度（米）
    vehicle_speed = 15  # 车辆速度（米/秒）
    safe_distance = 2  # 安全距离（米）
    
    # 计算通行能力
    headway = (vehicle_length + safe_distance) / vehicle_speed  # 车头时距（秒）
    capacity = 3600 / headway  # 每小时通行能力（辆/小时）
    total_capacity = capacity * num_lanes  # 总通行能力
    
    print(f"Lane width: {lane_width} m")
    print(f"Number of lanes: {num_lanes}")
    print(f"Vehicle length: {vehicle_length} m")
    print(f"Vehicle speed: {vehicle_speed} m/s")
    print(f"Safe distance: {safe_distance} m")
    print(f"Headway: {headway:.2f} s")
    print(f"Capacity per lane: {capacity:.0f} vehicles/hour")
    print(f"Total capacity: {total_capacity:.0f} vehicles/hour")
    
    # 问题3：拥堵分析
    print("\nProblem 3: Congestion Analysis")
    print("-" * 40)
    
    # 模拟交通流量数据
    time = np.arange(0, 24, 0.1)  # 24小时，每0.1小时一个数据点
    flow = 1000 + 500 * np.sin(2 * np.pi * time / 24) + 200 * np.random.randn(len(time))
    flow[flow < 0] = 0  # 确保流量为正
    
    # 计算拥堵指数
    congestion_index = flow / total_capacity
    
    # 绘制交通流量和拥堵指数
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1.plot(time, flow, 'b-', linewidth=2)
    ax1.axhline(y=total_capacity, color='r', linestyle='--', label='Capacity')
    ax1.set_xlabel('Time (hours)')
    ax1.set_ylabel('Traffic Flow (vehicles/hour)')
    ax1.set_title('Traffic Flow Over 24 Hours')
    ax1.legend()
    ax1.grid(True)
    
    ax2.plot(time, congestion_index, 'g-', linewidth=2)
    ax2.axhline(y=1.0, color='r', linestyle='--', label='Congestion threshold')
    ax2.set_xlabel('Time (hours)')
    ax2.set_ylabel('Congestion Index')
    ax2.set_title('Congestion Index Over 24 Hours')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.savefig('traffic_capacity_analysis.png')
    plt.close()
    
    print("Traffic analysis plot saved as 'traffic_capacity_analysis.png'")
    
    # 计算拥堵时间
    congestion_time = np.sum(congestion_index > 1.0) * 0.1
    print(f"Congestion time: {congestion_time:.1f} hours")
    
    return {
        'vehicle_count': vehicle_count,
        'capacity': total_capacity,
        'congestion_time': congestion_time
    }

if __name__ == "__main__":
    result = traffic_capacity_analysis()
    print("\n" + "=" * 60)
    print("Traffic capacity analysis completed!")
    print("=" * 60)