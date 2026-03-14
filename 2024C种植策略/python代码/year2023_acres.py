#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 2023年种植亩数分析
"""

import pandas as pd
import numpy as np

def load_data(file_path):
    """加载Excel数据"""
    return pd.read_excel(file_path)

def create_field_matrix(df, crops=42, plots=55, seasons=3):
    """创建三维种植面积矩阵 [作物][地块][季节]"""
    field = [[[0 for _ in range(seasons)] for _ in range(plots)] for _ in range(crops)]
    
    for _, row in df.iterrows():
        x = int(row['作物编号']) - 1
        y = int(row['种植地块']) - 1
        z = int(row['季节编号']) - 1
        area = row['种植面积/亩']
        
        if x < crops and y < plots and z < seasons:
            field[x][y][z] = area
    
    return field

def analyze_seasonal_distribution(field):
    """分析季节分布"""
    print("\n" + "=" * 60)
    print("季节分布分析")
    print("=" * 60)
    
    for season in range(3):
        total = sum(field[i][j][season] for i in range(len(field)) for j in range(len(field[0])))
        print(f"季节 {season + 1}: {total:.2f} 亩")
    
    return total

def analyze_crop_distribution(field):
    """分析作物分布"""
    print("\n" + "=" * 60)
    print("作物分布分析")
    print("=" * 60)
    
    crop_totals = []
    for crop in range(len(field)):
        total = sum(sum(field[crop][j]) for j in range(len(field[0])))
        if total > 0:
            crop_totals.append((crop + 1, total))
    
    crop_totals.sort(key=lambda x: x[1], reverse=True)
    
    print("种植面积前10的作物:")
    for i, (crop_id, area) in enumerate(crop_totals[:10]):
        print(f"  作物 {crop_id}: {area:.2f} 亩")
    
    return crop_totals

def main():
    """主函数"""
    file_path = '23年数据.xlsx'
    
    print("加载2023年数据...")
    df = load_data(file_path)
    
    print(f"数据行数: {len(df)}")
    print(f"数据列名: {list(df.columns)}")
    
    print("创建种植面积矩阵...")
    field = create_field_matrix(df)
    
    print("分析季节分布...")
    analyze_seasonal_distribution(field)
    
    print("分析作物分布...")
    analyze_crop_distribution(field)
    
    print("\n2023年种植亩数分析完成！")
    print(f"结果已保存到: field_matrix.npy")
    
    np.save('field_matrix.npy', field)

if __name__ == "__main__":
    main()
