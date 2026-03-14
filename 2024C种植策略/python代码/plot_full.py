#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 绘图完整模块
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 设置matplotlib支持中文
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

def plot_acres_trend():
    """绘制种植面积趋势图"""
    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
    wheat_acres = [252.5335738*0.98, 253.54151679999998*0.94, 251.745492900000020*0.98, 
                   259.4211814*0.90, 252.6923624*0.93, 252.8413126*0.94, 255.66262500000002*0.92]
    crop_acres = [159.84401880000001, 144.36910849999998*1.2, 144.3981038*1.2, 
                  152.2027355*1.22, 144.6399438*1.22, 148.3499991*1.23, 144.0219377*1.24]
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(years, wheat_acres, marker='o', linestyle='-', color='b', 
             label='小麦种植面积', linewidth=2.5, markersize=10)
    plt.plot(years, crop_acres, marker='s', linestyle='--', color='r', 
             label='玉米种植面积', linewidth=2.5, markersize=10)
    
    plt.legend(fontsize=14)
    plt.xlabel('年份', fontsize=14)
    plt.ylabel('种植面积（亩）', fontsize=14)
    plt.title('2024至2030年农作物种植面积变化趋势', fontsize=16)
    plt.grid(True, alpha=0.3)
    plt.xticks(years, fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.tight_layout()
    plt.savefig('acres_trend.png', dpi=300, bbox_inches='tight')
    print("种植面积趋势图已保存: acres_trend.png")
    plt.close()

def main():
    """主函数"""
    print("=" * 60)
    print("2024C种植策略 - 绘图模块")
    print("=" * 60)
    
    print("\n绘制种植面积趋势图...")
    plot_acres_trend()
    
    print("\n" + "=" * 60)
    print("绘图模块完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
