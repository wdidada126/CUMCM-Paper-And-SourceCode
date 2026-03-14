#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024B生产决策 - 主程序入口
全国大学生数学建模竞赛 (CUMCM 2024) 问题B：企业生产决策
"""

import os
import sys

def print_usage():
    """打印使用说明"""
    print("=" * 70)
    print("2024B生产决策 - Python代码集合")
    print("=" * 70)
    print("\n使用方法:")
    print("  python3 main.py <module> [args]")
    print("\n可用模块:")
    print("  1. problem_1_binomial    - 二项分布最小值求解")
    print("  2. problem_1_normal      - 正态分布最小值求解")
    print("  3. problem_2             - 问题2决策分析")
    print("  4. problem_3             - 问题3半成品分析")
    print("  5. problem_4_sampling    - 问题4抽样模拟")
    print("  6. problem_4_p2          - 问题4-问题2执行")
    print("  7. problem_4_p3          - 问题4-问题3执行")
    print("  8. all                   - 运行所有分析")
    print("\n示例:")
    print("  python3 main.py problem_1_binomial")
    print("  python3 main.py problem_2")
    print("  python3 main.py problem_4_sampling")
    print("  python3 main.py all")
    print("=" * 70)

def run_problem_1_binomial():
    """运行问题1-二项分布最小值求解"""
    print("\n" + "=" * 70)
    print("运行问题1-二项分布最小值求解...")
    print("=" * 70)
    try:
        import problem_1_binomial_distribution_min_value_solver
        print("问题1-二项分布最小值求解完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_1_normal():
    """运行问题1-正态分布最小值求解"""
    print("\n" + "=" * 70)
    print("运行问题1-正态分布最小值求解...")
    print("=" * 70)
    try:
        import problem_1_normal_distribution_min_value_solver
        print("问题1-正态分布最小值求解完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_2():
    """运行问题2决策分析"""
    print("\n" + "=" * 70)
    print("运行问题2决策分析...")
    print("=" * 70)
    try:
        import problem_2_exhaustive_process_decision_analysis
        print("问题2决策分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_3():
    """运行问题3半成品分析"""
    print("\n" + "=" * 70)
    print("运行问题3半成品分析...")
    print("=" * 70)
    try:
        import problem_3_semi_finished_goods_analysis
        print("问题3半成品分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_4_sampling():
    """运行问题4抽样模拟"""
    print("\n" + "=" * 70)
    print("运行问题4抽样模拟...")
    print("=" * 70)
    try:
        import problem_4_sampling_simulation_and_plot
        print("问题4抽样模拟完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_4_p2():
    """运行问题4-问题2执行"""
    print("\n" + "=" * 70)
    print("运行问题4-问题2执行...")
    print("=" * 70)
    try:
        import problem_4_defective_rate_change_with_problem_2_execution
        print("问题4-问题2执行完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_4_p3():
    """运行问题4-问题3执行"""
    print("\n" + "=" * 70)
    print("运行问题4-问题3执行...")
    print("=" * 70)
    try:
        import problem_4_defective_rate_change_with_problem_3_execution
        print("问题4-问题3执行完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_all():
    """运行所有分析"""
    print("\n" + "=" * 70)
    print("运行所有分析...")
    print("=" * 70)
    run_problem_1_binomial()
    run_problem_1_normal()
    run_problem_2()
    run_problem_3()
    run_problem_4_sampling()
    run_problem_4_p2()
    run_problem_4_p3()
    print("\n" + "=" * 70)
    print("所有分析完成！")
    print("=" * 70)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    module = sys.argv[1].lower()
    
    if module == 'problem_1_binomial':
        run_problem_1_binomial()
    elif module == 'problem_1_normal':
        run_problem_1_normal()
    elif module == 'problem_2':
        run_problem_2()
    elif module == 'problem_3':
        run_problem_3()
    elif module == 'problem_4_sampling':
        run_problem_4_sampling()
    elif module == 'problem_4_p2':
        run_problem_4_p2()
    elif module == 'problem_4_p3':
        run_problem_4_p3()
    elif module == 'all':
        run_all()
    else:
        print(f"未知模块: {module}")
        print_usage()

if __name__ == "__main__":
    main()
