import numpy as np
import matplotlib.pyplot as plt

def medicine_cabinet_design():
    """
    储药柜的设计问题
    基于MATLAB代码的Python实现
    """
    print("Problem: Medicine Cabinet Design")
    print("=" * 60)
    
    # 问题1：药盒尺寸分析
    print("\nProblem 1: Medicine Box Size Analysis")
    print("-" * 40)
    
    # 定义药盒尺寸（示例数据）
    num_boxes = 100
    np.random.seed(42)
    
    # 长度、宽度、高度（单位：mm）
    length = np.random.uniform(30, 120, num_boxes)
    width = np.random.uniform(20, 80, num_boxes)
    height = np.random.uniform(10, 50, num_boxes)
    
    # 计算药盒体积
    volume = length * width * height
    
    print(f"Number of medicine boxes: {num_boxes}")
    print(f"Average length: {np.mean(length):.2f} mm")
    print(f"Average width: {np.mean(width):.2f} mm")
    print(f"Average height: {np.mean(height):.2f} mm")
    print(f"Average volume: {np.mean(volume):.2f} mm³")
    
    # 绘制尺寸分布图
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0, 0].hist(length, bins=20, color='b', alpha=0.7)
    axes[0, 0].set_xlabel('Length (mm)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Length Distribution')
    axes[0, 0].grid(True)
    
    axes[0, 1].hist(width, bins=20, color='g', alpha=0.7)
    axes[0, 1].set_xlabel('Width (mm)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].set_title('Width Distribution')
    axes[0, 1].grid(True)
    
    axes[1, 0].hist(height, bins=20, color='r', alpha=0.7)
    axes[1, 0].set_xlabel('Height (mm)')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Height Distribution')
    axes[1, 0].grid(True)
    
    axes[1, 1].hist(volume, bins=20, color='m', alpha=0.7)
    axes[1, 1].set_xlabel('Volume (mm³)')
    axes[1, 1].set_ylabel('Frequency')
    axes[1, 1].set_title('Volume Distribution')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig('medicine_box_size_analysis.png')
    plt.close()
    
    print("Size analysis plot saved as 'medicine_box_size_analysis.png'")
    
    # 问题2：储药柜设计
    print("\nProblem 2: Medicine Cabinet Design")
    print("-" * 40)
    
    # 定义储药柜参数
    cabinet_length = 2000  # 柜体长度（mm）
    cabinet_width = 1000   # 柜体宽度（mm）
    cabinet_height = 2000  # 柜体高度（mm）
    
    # 定义储药柜层数和列数
    num_layers = 10
    num_columns = 5
    
    # 计算每层的高度
    layer_height = cabinet_height / num_layers
    print(f"Layer height: {layer_height:.2f} mm")
    
    # 计算每列的宽度
    column_width = cabinet_width / num_columns
    print(f"Column width: {column_width:.2f} mm")
    
    # 问题3：药盒分配
    print("\nProblem 3: Medicine Box Allocation")
    print("-" * 40)
    
    # 根据药盒高度分配到不同层
    def allocate_boxes(height, num_layers, layer_height):
        """
        根据药盒高度分配到不同层
        """
        allocation = np.zeros(len(height), dtype=int)
        
        for i, h in enumerate(height):
            # 计算应该放在哪一层
            layer = int(h / layer_height)
            if layer >= num_layers:
                layer = num_layers - 1
            allocation[i] = layer
        
        return allocation
    
    allocation = allocate_boxes(height, num_layers, layer_height)
    
    # 统计每层的药盒数量
    boxes_per_layer = np.bincount(allocation, minlength=num_layers)
    print(f"Boxes per layer: {boxes_per_layer}")
    
    # 计算每层的利用率
    layer_utilization = boxes_per_layer / (num_columns * 10)  # 假设每列每层最多放10个药盒
    print(f"Layer utilization: {layer_utilization}")
    
    # 绘制药盒分配图
    plt.figure(figsize=(12, 6))
    plt.bar(range(num_layers), boxes_per_layer, color='b', alpha=0.7)
    plt.xlabel('Layer')
    plt.ylabel('Number of Boxes')
    plt.title('Medicine Box Allocation by Layer')
    plt.grid(True)
    plt.savefig('medicine_box_allocation.png')
    plt.close()
    
    print("Allocation plot saved as 'medicine_box_allocation.png'")
    
    # 问题4：优化设计
    print("\nProblem 4: Optimal Design")
    print("-" * 40)
    
    # 计算最优层数和列数
    def calculate_optimal_design(height, width, length, cabinet_height, cabinet_width):
        """
        计算最优层数和列数
        """
        # 尝试不同的层数和列数
        best_utilization = 0
        best_layers = 1
        best_columns = 1
        
        for layers in range(5, 20):
            for columns in range(3, 10):
                layer_height = cabinet_height / layers
                column_width = cabinet_width / columns
                
                # 分配药盒
                allocation = allocate_boxes(height, layers, layer_height)
                
                # 计算利用率
                boxes_per_layer = np.bincount(allocation, minlength=layers)
                max_boxes_per_layer = columns * 10
                utilization = np.sum(boxes_per_layer) / (layers * max_boxes_per_layer)
                
                if utilization > best_utilization:
                    best_utilization = utilization
                    best_layers = layers
                    best_columns = columns
        
        return best_layers, best_columns, best_utilization
    
    optimal_layers, optimal_columns, optimal_utilization = calculate_optimal_design(
        height, width, length, cabinet_height, cabinet_width
    )
    
    print(f"Optimal number of layers: {optimal_layers}")
    print(f"Optimal number of columns: {optimal_columns}")
    print(f"Optimal utilization: {optimal_utilization:.2%}")
    
    # 计算最优设计下的层高和列宽
    optimal_layer_height = cabinet_height / optimal_layers
    optimal_column_width = cabinet_width / optimal_columns
    print(f"Optimal layer height: {optimal_layer_height:.2f} mm")
    print(f"Optimal column width: {optimal_column_width:.2f} mm")
    
    return {
        'num_boxes': num_boxes,
        'average_volume': np.mean(volume),
        'optimal_layers': optimal_layers,
        'optimal_columns': optimal_columns,
        'optimal_utilization': optimal_utilization
    }

if __name__ == "__main__":
    result = medicine_cabinet_design()
    print("\n" + "=" * 60)
    print("Medicine cabinet design analysis completed!")
    print("=" * 60)