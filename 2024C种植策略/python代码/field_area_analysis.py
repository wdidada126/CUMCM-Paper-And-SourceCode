#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 田地面积分析模块
"""

import pandas as pd

def load_data(file_path):
    """加载Excel数据"""
    return pd.read_excel(file_path)

def create_farm_matrix(df, crops=42, plots=55):
    """创建农场面积矩阵"""
    farm_array = [[0 for _ in range(plots)] for _ in range(crops)]
    
    crop_ids = df['作物编号'].tolist()
    plot_ids = df['地块编号'].tolist()
    areas = df['种植面积/亩'].tolist()
    
    for crop_id, plot_id, area in zip(crop_ids, plot_ids, areas):
        if crop_id <= crops and plot_id <= plots:
            farm_array[crop_id - 1][plot_id - 1] = area
    
    return farm_array

def save_to_excel(farm_array, output_path='farm_data.xlsx'):
    """保存到Excel文件"""
    df = pd.DataFrame(farm_array)
    df.to_excel(output_path, index=False, header=False)
    print(f"Excel文件已生成: {output_path}")

def analyze_area_distribution(farm_array):
    """分析面积分布"""
    total_area = sum(sum(row) for row in farm_array)
    crop_totals = [sum(row) for row in farm_array]
    plot_totals = [sum(farm_array[i][j] for i in range(len(farm_array))) 
                   for j in range(len(farm_array[0]))]
    
    print("\n" + "=" * 60)
    print("面积分布分析")
    print("=" * 60)
    print(f"总种植面积: {total_area:.2f} 亩")
    print(f"作物种类数: {sum(1 for x in crop_totals if x > 0)}")
    print(f"地块使用数: {sum(1 for x in plot_totals if x > 0)}")
    
    if crop_totals:
        print(f"平均单作物面积: {sum(crop_totals)/len(crop_totals):.2f} 亩")
    
    return {
        'total_area': total_area,
        'crop_totals': crop_totals,
        'plot_totals': plot_totals
    }

def main():
    """主函数"""
    file_path = '附件2(1)1.xlsx'
    
    print("加载数据...")
    df = load_data(file_path)
    
    print(f"数据行数: {len(df)}")
    print(f"数据列名: {list(df.columns)}")
    
    print("创建农场面积矩阵...")
    farm_array = create_farm_matrix(df)
    
    print("保存结果...")
    save_to_excel(farm_array)
    
    print("分析面积分布...")
    stats = analyze_area_distribution(farm_array)
    
    print("\n田地面积分析完成！")

if __name__ == "__main__":
    main()
