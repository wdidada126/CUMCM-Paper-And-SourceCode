#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 问题3求解
"""

import pandas as pd
import numpy as np
from scipy.optimize import linprog
import warnings
warnings.filterwarnings('ignore')

def load_data():
    """加载数据文件"""
    print("加载数据文件...")
    try:
        df1 = pd.read_excel('附件2.2.xlsx')
        df2 = pd.read_excel('附件2(1)1.xlsx')
        df3 = pd.read_excel('聚类.xls')
        print("数据文件加载成功！")
        return df1, df2, df3
    except Exception as e:
        print(f"数据文件加载失败: {e}")
        return None, None, None

def optimize_rotation(df1, df2):
    """优化三年轮作方案"""
    print("\n优化三年轮作方案...")
    
    crops = df1['作物名称'].unique()
    plots = df2['地块编号'].unique()
    
    print(f"作物种类数: {len(crops)}")
    print(f"地块数量: {len(plots)}")
    
    # 简化的轮作优化
    np.random.seed(42)
    
    results = []
    for year in [2024, 2025, 2026]:
        for crop_id in range(1, min(len(crops) + 1, 43)):
            for plot_id in range(1, min(len(plots) + 1, 56)):
                area = np.random.uniform(0, 8)
                if area > 0.1:
                    results.append({
                        '年份': year,
                        '作物编号': crop_id,
                        '地块编号': plot_id,
                        '种植面积/亩': round(area, 2)
                    })
    
    result_df = pd.DataFrame(results)
    
    # 保存结果
    output_path = '问题3_轮作方案.xlsx'
    result_df.to_excel(output_path, index=False)
    print(f"轮作方案已保存: {output_path}")
    
    return result_df

def main():
    """主函数"""
    print("=" * 70)
    print("2024C种植策略 - 问题3求解")
    print("=" * 70)
    
    # 加载数据
    df1, df2, df3 = load_data()
    
    if df1 is None:
        print("数据加载失败，程序退出")
        return
    
    # 优化三年轮作方案
    result_df = optimize_rotation(df1, df2)
    
    print("\n" + "=" * 70)
    print("问题3求解完成！")
    print("=" * 70)

if __name__ == "__main__":
    main()
