#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 主程序入口
全国大学生数学建模竞赛 CUMCM 2024
"""

import os
import sys

def print_usage():
    """打印使用说明"""
    print("=" * 70)
    print("2024C种植策略 - Python代码集合")
    print("=" * 70)
    print("\n使用方法:")
    print("  python main.py <module> [args]")
    print("\n可用模块:")
    print("  1. cost_profit_full   - 成本利润完整分析")
    print("  2. clustering_full    - 聚类完整分析")
    print("  3. price_analysis     - 平均售价分析")
    print("  4. field_area_full    - 田地面积完整分析")
    print("  5. plot_full          - 绘图完整模块")
    print("  6. year2023_acres     - 2023年种植亩数分析")
    print("  7. year2023_profit    - 2023年利润统计")
    print("  8. data_label         - 数据标签处理")
    print("  9. cost_reformat      - 成本数据整理")
    print(" 10. question2          - 问题2求解")
    print(" 11. question3          - 问题3求解")
    print(" 12. all                - 运行所有分析")
    print("\n示例:")
    print("  python main.py cost_profit_full")
    print("  python main.py clustering_full")
    print("  python main.py question2")
    print("  python main.py question3")
    print("  python main.py all")
    print("=" * 70)

def run_cost_profit_full():
    """运行成本利润完整分析"""
    print("\n" + "=" * 70)
    print("运行成本利润完整分析...")
    print("=" * 70)
    try:
        import cost_profit_full
        print("成本利润完整分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_clustering_full():
    """运行聚类完整分析"""
    print("\n" + "=" * 70)
    print("运行聚类完整分析...")
    print("=" * 70)
    try:
        import clustering_full
        print("聚类完整分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_price_analysis():
    """运行平均售价分析"""
    print("\n" + "=" * 70)
    print("运行平均售价分析...")
    print("=" * 70)
    try:
        import price_analysis
        print("平均售价分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_field_area_full():
    """运行田地面积完整分析"""
    print("\n" + "=" * 70)
    print("运行田地面积完整分析...")
    print("=" * 70)
    try:
        import field_area_full
        print("田地面积完整分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_plot_full():
    """运行绘图完整模块"""
    print("\n" + "=" * 70)
    print("运行绘图完整模块...")
    print("=" * 70)
    try:
        import plot_full
        print("绘图完整模块完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_year2023_acres():
    """运行2023年种植亩数分析"""
    print("\n" + "=" * 70)
    print("运行2023年种植亩数分析...")
    print("=" * 70)
    try:
        import year2023_acres
        print("2023年种植亩数分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_year2023_profit():
    """运行2023年利润统计"""
    print("\n" + "=" * 70)
    print("运行2023年利润统计...")
    print("=" * 70)
    try:
        import year2023_profit
        print("2023年利润统计完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_data_label():
    """运行数据标签处理"""
    print("\n" + "=" * 70)
    print("运行数据标签处理...")
    print("=" * 70)
    try:
        import data_label
        print("数据标签处理完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_cost_reformat():
    """运行成本数据整理"""
    print("\n" + "=" * 70)
    print("运行成本数据整理...")
    print("=" * 70)
    try:
        import cost_reformat
        print("成本数据整理完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_question2():
    """运行问题2求解"""
    print("\n" + "=" * 70)
    print("运行问题2求解...")
    print("=" * 70)
    try:
        import question2.script as q2
        print("问题2求解完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_question3():
    """运行问题3求解"""
    print("\n" + "=" * 70)
    print("运行问题3求解...")
    print("=" * 70)
    try:
        import question3.script as q3
        print("问题3求解完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_all():
    """运行所有分析"""
    print("\n" + "=" * 70)
    print("运行所有分析...")
    print("=" * 70)
    run_cost_profit_full()
    run_clustering_full()
    run_price_analysis()
    run_field_area_full()
    run_plot_full()
    run_year2023_acres()
    run_year2023_profit()
    run_data_label()
    run_cost_reformat()
    run_question2()
    run_question3()
    print("\n" + "=" * 70)
    print("所有分析完成！")
    print("=" * 70)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    module = sys.argv[1].lower()
    
    if module == 'cost_profit_full':
        run_cost_profit_full()
    elif module == 'clustering_full':
        run_clustering_full()
    elif module == 'price_analysis':
        run_price_analysis()
    elif module == 'field_area_full':
        run_field_area_full()
    elif module == 'plot_full':
        run_plot_full()
    elif module == 'year2023_acres':
        run_year2023_acres()
    elif module == 'year2023_profit':
        run_year2023_profit()
    elif module == 'data_label':
        run_data_label()
    elif module == 'cost_reformat':
        run_cost_reformat()
    elif module == 'question2':
        run_question2()
    elif module == 'question3':
        run_question3()
    elif module == 'all':
        run_all()
    else:
        print(f"未知模块: {module}")
        print_usage()

if __name__ == "__main__":
    main()
