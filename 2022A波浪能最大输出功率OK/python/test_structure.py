#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试代码结构
"""

import sys
import os
import importlib.util

def test_import(module_name, module_path):
    """测试模块是否可以导入"""
    print(f"\n测试导入: {module_name}")
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
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
    print("2022A波浪能最大输出功率 - 代码结构测试")
    print("=" * 70)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    modules = [
        ('T1_1', os.path.join(script_dir, 'T1', 'T1.1.py')),
        ('T1_2', os.path.join(script_dir, 'T1', 'T1.2.py')),
        ('T2_1', os.path.join(script_dir, 'T2', 'T2.1.py')),
        ('T2_2', os.path.join(script_dir, 'T2', 'T2.2.py')),
        ('T3_1', os.path.join(script_dir, 'T3', 'T3.1.py')),
        ('T3_2', os.path.join(script_dir, 'T3', 'T3.2.py')),
        ('T4_1', os.path.join(script_dir, 'T4', 'T4.1.py')),
        ('T4_2', os.path.join(script_dir, 'T4', 'T4.2.py')),
    ]
    
    results = {}
    for module_name, module_path in modules:
        results[module_name] = test_import(module_name, module_path)
    
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
