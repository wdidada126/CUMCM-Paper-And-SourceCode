#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 2023年利润统计
"""

import pandas as pd

def average_price(price_range):
    """处理销售单价，支持字符串格式的区间"""
    if isinstance(price_range, str):
        low, high = map(float, price_range.split('-'))
        return (low + high) / 2
    else:
        return 0.0

def main():
    """主函数"""
    file_path = '附件2.2.xlsx'
    
    print("加载数据...")
    df = pd.read_excel(file_path)
    
    print(f"数据行数: {len(df)}")
    
    # 初始化列表
    cost_list = []
    min_price_list = []
    max_price_list = []
    yield_list = []
    land_type_list = []
    crop_name_list = []
    
    print("处理数据...")
    for index, row in df.iterrows():
        cost = row['种植成本/(元/亩)']
        yield_per_mu = row['亩产量/斤']
        land_type = row['地块类型']
        crop_name = row['作物名称']
        
        min_price, max_price = average_price(row['销售单价/(元/斤)']), average_price(row['销售单价/(元/斤)'])
        
        cost_list.append(cost)
        min_price_list.append(min_price)
        max_price_list.append(max_price)
        yield_list.append(yield_per_mu)
        land_type_list.append(land_type)
        crop_name_list.append(crop_name)
    
    print("计算利润...")
    max_profit_list = [(y * max_p - c) for y, max_p, c in zip(yield_list, max_price_list, cost_list) 
                      if c != 0 and max_p != 0]
    min_profit_list = [(y * min_p - c) for y, min_p, c in zip(yield_list, min_price_list, cost_list) 
                      if c != 0 and min_p != 0]
    
    print("\n利润统计:")
    print(f"最大利润列表长度: {len(max_profit_list)}")
    print(f"最小利润列表长度: {len(min_profit_list)}")
    
    if max_profit_list:
        print(f"平均最大利润: {sum(max_profit_list) / len(max_profit_list):.2f} 元/亩")
    if min_profit_list:
        print(f"平均最小利润: {sum(min_profit_list) / len(min_profit_list):.2f} 元/亩")
    
    print("创建结果DataFrame...")
    profit_df = pd.DataFrame({
        '作物名称': crop_name_list,
        '地块类型': land_type_list,
        '最大利润': max_profit_list,
        '最小利润': min_profit_list
    })
    
    output_path = '利润分析结果.xlsx'
    profit_df.to_excel(output_path, index=False)
    print(f"利润分析结果已保存到: {output_path}")
    
    print("\n利润统计分析完成！")

if __name__ == "__main__":
    main()
