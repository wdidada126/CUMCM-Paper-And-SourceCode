#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2024C种植策略 - 成本数据整理
"""

import pandas as pd

def load_excel(file_path):
    """读取Excel文件"""
    return pd.read_excel(file_path)

def save_excel(df, file_path):
    """将DataFrame写入Excel文件"""
    df.to_excel(file_path, index=False, engine='openpyxl')

def reformat_data(input_path, output_path):
    """读取成本01.xlsx，然后按照作物编号和地块类型重新整理数据"""
    data = load_excel(input_path)
    
    if set(['种植地块', '作物编号', '种植成本/(元/亩)']).issubset(data.columns):
        data.set_index(['作物编号', '种植地块'], inplace=True)
        data['种植成本/(元/亩)'].unstack(level='种植地块').to_excel(output_path, engine='openpyxl')
        print(f"文件已成功生成: {output_path}")
    else:
        raise ValueError("缺少必要的列: 种植地块, 作物编号, 种植成本/(元/亩)")

def main():
    """主函数"""
    input_file = '成本01.xlsx'
    output_file = '重新整理的成本.xlsx'
    
    print("开始重新整理成本数据...")
    print(f"输入文件: {input_file}")
    print(f"输出文件: {output_file}")
    
    try:
        reformat_data(input_file, output_file)
        print("\n成本数据整理完成！")
    except Exception as e:
        print(f"错误: {e}")
        print("请确保输入文件存在且格式正确")

if __name__ == "__main__":
    main()
