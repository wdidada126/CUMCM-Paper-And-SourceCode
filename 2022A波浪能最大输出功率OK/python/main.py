#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2022A波浪能最大输出功率 - 主程序入口
全国大学生数学建模竞赛 (CUMCM 2022) 问题A
"""

import os
import sys

def print_usage():
    """打印使用说明"""
    print("=" * 70)
    print("2022A波浪能最大输出功率 - Python代码集合")
    print("=" * 70)
    print("\n使用方法:")
    print("  python3 main.py <module> [args]")
    print("\n可用模块:")
    print("  1. problem_1_1   - 第一题第一问")
    print("  2. problem_1_2   - 第一题第二问")
    print("  3. problem_2_1   - 第二题第一问")
    print("  4. problem_2_2   - 第二题第二问")
    print("  5. problem_3     - 第三题")
    print("  6. problem_4     - 第四题")
    print("  7. all           - 运行所有问题")
    print("\n示例:")
    print("  python3 main.py problem_1_1")
    print("  python3 main.py problem_2_1")
    print("  python3 main.py problem_3")
    print("  python3 main.py all")
    print("=" * 70)

def run_problem_1_1():
    """运行第一题第一问"""
    print("\n" + "=" * 70)
    print("运行第一题第一问...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T1'))
        import T1_1
        print("第一题第一问完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_1_2():
    """运行第一题第二问"""
    print("\n" + "=" * 70)
    print("运行第一题第二问...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T1'))
        import T1_2
        print("第一题第二问完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_2_1():
    """运行第二题第一问"""
    print("\n" + "=" * 70)
    print("运行第二题第一问...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T2'))
        import T2_1
        print("第二题第一问完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_2_2():
    """运行第二题第二问"""
    print("\n" + "=" * 70)
    print("运行第二题第二问...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T2'))
        import T2_2
        print("第二题第二问完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_3():
    """运行第三题"""
    print("\n" + "=" * 70)
    print("运行第三题...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T3'))
        import T3_1
        import T3_2
        print("第三题完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_problem_4():
    """运行第四题"""
    print("\n" + "=" * 70)
    print("运行第四题...")
    print("=" * 70)
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'T4'))
        import T4_1
        import T4_2
        print("第四题完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_all():
    """运行所有问题"""
    print("\n" + "=" * 70)
    print("运行所有问题...")
    print("=" * 70)
    run_problem_1_1()
    run_problem_1_2()
    run_problem_2_1()
    run_problem_2_2()
    run_problem_3()
    run_problem_4()
    print("\n" + "=" * 70)
    print("所有问题完成！")
    print("=" * 70)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    module = sys.argv[1].lower()
    
    if module == 'problem_1_1':
        run_problem_1_1()
    elif module == 'problem_1_2':
        run_problem_1_2()
    elif module == 'problem_2_1':
        run_problem_2_1()
    elif module == 'problem_2_2':
        run_problem_2_2()
    elif module == 'problem_3':
        run_problem_3()
    elif module == 'problem_4':
        run_problem_4()
    elif module == 'all':
        run_all()
    else:
        print(f"未知模块: {module}")
        print_usage()

if __name__ == "__main__":
    main()
