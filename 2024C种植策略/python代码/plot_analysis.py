#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 绘图模块
"""

import matplotlib.pyplot as plt
import matplotlib

# 设置matplotlib支持中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决保存图像时负号'-'显示为方块的问题

def plot_acres():
    """绘制种植面积图"""
    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
    wheat_acres = [252.5335738*0.98, 253.54151679999998*0.94, 251.745492900000020*0.98, 
                   259.4211814*0.90, 252.6923624*0.93, 252.8413126*0.94, 255.66262500000002*0.92]
    crop_acres = [159.84401880000001, 144.36910849999998*1.2, 144.3981038*1.2, 
                  152.2027355*1.22, 144.6399438*1.22, 148.3499991*1.23, 144.0219377*1.24]
    
    plt.figure(figsize=(10, 5))
    
    plt.plot(years, wheat_acres, marker='o', linestyle='-', color='b', 
             label='小麦种植面积', linewidth=2, markersize=8)
    plt.plot(years, crop_acres, marker='s', linestyle='--', color='r', 
             label='玉米种植面积', linewidth=2, markersize=8)
    
    plt.legend(fontsize=12)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('种植面积（亩）', fontsize=12)
    plt.title('2024至2030年农作物种植面积变化趋势', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('acres_trend.png', dpi=300, bbox_inches='tight')
    print("种植面积图已保存: acres_trend.png")
    plt.close()

def plot_cost_profit_distribution(costs, profits, labels):
    """绘制成本利润分布图"""
    x = range(len(labels))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.bar([i - width/2 for i in x], costs, width, label='种植成本', color='steelblue')
    ax.bar([i + width/2 for i in x], profits, width, label='利润', color='forestgreen')
    
    ax.set_xlabel('作物名称', fontsize=12)
    ax.set_ylabel('金额（元）', fontsize=12)
    ax.set_title('作物成本与利润对比', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('cost_profit_distribution.png', dpi=300, bbox_inches='tight')
    print("成本利润分布图已保存: cost_profit_distribution.png")
    plt.close()

def main():
    """主函数"""
    print("绘制种植面积趋势图...")
    plot_acres()
    
    print("\n绘图模块完成！")

if __name__ == "__main__":
    main()
