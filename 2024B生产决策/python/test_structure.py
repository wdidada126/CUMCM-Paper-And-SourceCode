#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试代码结构
"""

import sys
import importlib.util

def test_import(module_name):
    """测试模块是否可以导入"""
    print(f"\n测试导入: {module_name}")
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            print(f"  ❌ 模块 '{module_name}' 未找到")
            return False
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"  ✓ 成功导入 {module_name}")
        return True
    except Exception as e:
        print(f"  ❌ 导入失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 70)
    print("2024B生产决策 - 代码结构测试")
    print("=" * 70)
    
    modules = [
        'problem_1_binomial_distribution_min_value_solver',
        'problem_1_normal_distribution_min_value_solver',
        'problem_2_exhaustive_process_decision_analysis',
        'problem_3_semi_finished_goods_analysis',
        'problem_4_sampling_simulation_and_plot',
        'problem_4_defective_rate_change_with_problem_2_execution',
        'problem_4_defective_rate_change_with_problem_3_execution'
    ]
    
    results = {}
    for module in modules:
        results[module] = test_import(module)
    
    print("\n" + "=" * 70)
    print("测试结果汇总")
    print("=" * 70)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for module, success in results.items():
        status = "✓ 通过" if success else "❌ 失败"
        print(f"{module}: {status}")
    
    print(f"\n总计: {passed}/{total} 通过")
    
    if passed == total:
        print("\n✓ 所有模块结构正确！")
        return 0
    else:
        print(f"\n❌ {total - passed} 个模块存在问题")
        return 1

if __name__ == "__main__":
    sys.exit(main())
