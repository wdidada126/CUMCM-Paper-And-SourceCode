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
    print("2024C种植策略 - 代码结构测试")
    print("=" * 70)
    
    modules = [
        'cost_profit_full',
        'clustering_full',
        'price_analysis',
        'field_area_full',
        'plot_full',
        'year2023_acres',
        'year2023_profit',
        'data_label',
        'cost_reformat',
        'question2.script',
        'question3.script'
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
