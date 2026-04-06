#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2023C蔬菜类商品的自动定价与补货决策 - 主程序入口
全国大学生数学建模竞赛 (CUMCM 2023) 问题C
"""

import os
import sys

# 添加packages目录到Python路径
script_dir = os.path.dirname(os.path.abspath(__file__))
packages_path = os.path.join(script_dir, 'packages')
if os.path.exists(packages_path) and packages_path not in sys.path:
    sys.path.insert(0, packages_path)

def print_usage():
    """打印使用说明"""
    print("=" * 70)
    print("2023C蔬菜类商品的自动定价与补货决策 - Python代码集合")
    print("=" * 70)
    print("\n使用方法:")
    print("  python3 main.py <module> [args]")
    print("\n可用模块:")
    print("  1. preprocess    - 数据预处理")
    print("  2. plot          - 绘图分析")
    print("  3. model_ai      - AI模型训练")
    print("  4. model_math    - 数学模型求解")
    print("  5. get_index     - 指标计算")
    print("  6. xiaohan     - 小韩的代码")
    print("  7. all           - 运行所有分析")
    print("\n示例:")
    print("  python3 main.py preprocess")
    print("  python3 main.py model_ai")
    print("  python3 main.py model_math")
    print("  python3 main.py all")
    print("=" * 70)

def run_preprocess():
    """运行数据预处理"""
    print("\n" + "=" * 70)
    print("运行数据预处理...")
    print("=" * 70)
    try:
        import preprocess
        print("数据预处理完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_plot():
    """运行绘图分析"""
    print("\n" + "=" * 70)
    print("运行绘图分析...")
    print("=" * 70)
    try:
        import analyse
        print("绘图分析完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_model_ai():
    """运行AI模型训练"""
    print("\n" + "=" * 70)
    print("运行AI模型训练...")
    print("=" * 70)
    try:
        import model_AI
        print("AI模型训练完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_model_math():
    """运行数学模型求解"""
    print("\n" + "=" * 70)
    print("运行数学模型求解...")
    print("=" * 70)
    try:
        import model_math
        print("数学模型求解完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_get_index():
    """运行指标计算"""
    print("\n" + "=" * 70)
    print("运行指标计算...")
    print("=" * 70)
    try:
        import get_index
        print("指标计算完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_xiaohan():
    """运行小韩的代码"""
    print("\n" + "=" * 70)
    print("运行小韩的代码...")
    print("=" * 70)
    try:
        import XiaoHan
        print("小韩的代码完成！")
    except Exception as e:
        print(f"错误: {e}")

def run_all():
    """运行所有分析"""
    print("\n" + "=" * 70)
    print("运行所有分析...")
    print("=" * 70)
    run_preprocess()
    run_plot()
    run_model_ai()
    run_model_math()
    run_get_index()
    run_xiaohan()
    print("\n" + "=" * 70)
    print("所有分析完成！")
    print("=" * 70)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        print_usage()
        return
    
    module = sys.argv[1].lower()
    
    if module == 'preprocess':
        run_preprocess()
    elif module == 'plot':
        run_plot()
    elif module == 'model_ai':
        run_model_ai()
    elif module == 'model_math':
        run_model_math()
    elif module == 'get_index':
        run_get_index()
    elif module == 'xiaohan':
        run_xiaohan()
    elif module == 'all':
        run_all()
    else:
        print(f"未知模块: {module}")
        print_usage()

if __name__ == "__main__":
    main()
