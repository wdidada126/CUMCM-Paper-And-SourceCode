#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 数据标签处理
"""

import pandas as pd

def main():
    """主函数"""
    file_path = '附件2(1)1.xlsx'
    
    print("加载数据...")
    df = pd.read_excel(file_path)
    
    print(f"数据行数: {len(df)}")
    print(f"数据列名: {list(df.columns)}")
    
    # 提取农作物编号和种植地编号
    crop_ids = df['作物编号'].tolist()
    plot_ids = df['地块编号'].tolist()
    areas = df['种植面积/亩'].tolist()
    
    print(f"作物编号数量: {len(crop_ids)}")
    print(f"地块编号数量: {len(plot_ids)}")
    print(f"种植面积数量: {len(areas)}")
    
    # 初始化42*55的二维数组
    crops = 42
    plots = 55
    farm_array = [[0 for _ in range(plots)] for _ in range(crops)]
    
    print("填充数据...")
    for crop_id, plot_id, area in zip(crop_ids, plot_ids, areas):
        if crop_id <= crops and plot_id <= plots:
            farm_array[crop_id - 1][plot_id - 1] = area
    
    print("创建DataFrame...")
    df_result = pd.DataFrame(farm_array)
    
    output_path = 'farm_data.xlsx'
    df_result.to_excel(output_path, index=False, header=False)
    print(f"Excel文件已生成: {output_path}")
    
    # 统计信息
    total_area = sum(sum(row) for row in farm_array)
    used_plots = sum(1 for row in farm_array for val in row if val > 0)
    
    print("\n统计信息:")
    print(f"总种植面积: {total_area:.2f} 亩")
    print(f"使用地块数: {used_plots}")
    
    print("\n数据标签处理完成！")

if __name__ == "__main__":
    main()
