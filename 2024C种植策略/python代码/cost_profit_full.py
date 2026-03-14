#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 成本利润完整分析
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置支持中文的字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

def average_price(price_range):
    """处理销售单价，支持字符串格式的区间"""
    if isinstance(price_range, str):
        low, high = map(float, price_range.split('-'))
        return (low + high) / 2
    else:
        return float(price_range)

def main():
    """主函数"""
    file_path = '附件2.2.xlsx'
    
    print("=" * 70)
    print("2024C种植策略 - 成本利润分析")
    print("=" * 70)
    
    print("\n加载数据...")
    df = pd.read_excel(file_path)
    
    print(f"数据行数: {len(df)}")
    print(f"数据列名: {list(df.columns)}")
    
    print("\n处理销售单价...")
    df['销售单价/(元/斤)'] = df['销售单价/(元/斤)'].apply(average_price)
    
    print("计算各项指标...")
    df['总收入（元）'] = df['亩产量/斤'] * df['销售单价/(元/斤)']
    df['利润（元/亩）'] = df['总收入（元）'] - df['种植成本/(元/亩)']
    df['利润成本比'] = df['利润（元/亩）'] / df['种植成本/(元/亩)']
    
    print("\n" + "=" * 70)
    print("统计信息")
    print("=" * 70)
    print(f"总作物数: {len(df)}")
    print(f"平均利润: {df['利润（元/亩）'].mean():.2f} 元/亩")
    print(f"最大利润: {df['利润（元/亩）'].max():.2f} 元/亩")
    print(f"最小利润: {df['利润（元/亩）'].min():.2f} 元/亩")
    print(f"平均利润成本比: {df['利润成本比'].mean():.2f}")
    
    print("\n绘制图表...")
    fig, ax1 = plt.subplots(figsize=(20, 8))
    
    作物名称 = df['作物名称'].astype(str)
    bar_width = 0.4
    index = range(len(作物名称))
    
    ax1.bar(index, df['种植成本/(元/亩)'], width=bar_width, label='种植成本', color='blue')
    ax1.bar([i + bar_width for i in index], df['利润（元/亩）'], width=bar_width, label='利润', color='green')
    
    ax2 = ax1.twinx()
    ax2.plot([i + bar_width / 2 for i in index], df['利润成本比'], 'r-o', label='利润成本比')
    
    ax1.set_xlabel('作物名称', fontsize=12)
    ax1.set_ylabel('成本和利润（元）', fontsize=12)
    ax2.set_ylabel('利润成本比', fontsize=12)
    ax1.set_title('各种作物的成本、利润及利润成本比', fontsize=14)
    ax1.set_xticks([i + bar_width / 2 for i in index])
    ax1.set_xticklabels(作物名称, rotation=90)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    plt.tight_layout()
    plt.savefig('cost_profit_analysis.png', dpi=300, bbox_inches='tight')
    print("图表已保存: cost_profit_analysis.png")
    plt.close()
    
    print("\n保存结果...")
    output_path = 'cost_profit_results.xlsx'
    df.to_excel(output_path, index=False)
    print(f"结果已保存: {output_path}")
    
    print("\n" + "=" * 70)
    print("成本利润分析完成！")
    print("=" * 70)

if __name__ == "__main__":
    main()
