# 2024C种植策略 - Python代码集合

全国大学生数学建模竞赛 (CUMCM 2024) 问题C：种植策略

## 目录结构

```
python代码/
├── main.py                    # 主程序入口
├── requirements.txt           # Python依赖包列表
├── clustering_full.py         # 聚类分析模块（不依赖sklearn）
├── cost_profit_full.py        # 成本利润分析模块
├── price_analysis.py          # 平均售价分析模块
├── field_area_full.py         # 田地面积分析模块
├── plot_full.py               # 绘图模块
├── year2023_acres.py          # 2023年种植亩数分析
├── year2023_profit.py         # 2023年利润统计
├── data_label.py              # 数据标签处理
├── cost_reformat.py           # 成本数据整理
├── question2/
│   └── script.py              # 问题2求解脚本
├── question3/
│   └── script.py              # 问题3求解脚本
├── test_structure.py          # 代码结构测试脚本
├── README.md                  # 本文件
└── DATA_README.md             # 数据文件说明
```

## 安装依赖

```bash
pip install -r requirements.txt
```

### 依赖包列表

- pandas>=1.5.0 - 数据处理
- numpy>=1.23.0 - 数值计算
- matplotlib>=3.7.0 - 数据可视化
- openpyxl>=3.1.0 - Excel文件读写
- scipy>=1.10.0 - 科学计算和优化

**注意**: 聚类分析使用自定义K-means实现，无需安装scikit-learn

## 使用方法

### 运行特定模块

```bash
python main.py cost_profit_full
python main.py clustering_full
python main.py price_analysis
python main.py field_area_full
python main.py plot_full
python main.py year2023_acres
python main.py year2023_profit
python main.py data_label
python main.py cost_reformat
python main.py question2
python main.py question3
```

### 运行所有分析

```bash
python main.py all
```

### 测试代码结构

```bash
python test_structure.py
```

## 数据文件

需要将以下数据文件放在 `python代码` 目录下：

- `附件2.2.xlsx` - 作物种植数据
- `附件2(1)1.xlsx` - 地块信息数据
- `聚类.xls` - 聚类分析数据

## 模块说明

### cost_profit_full
成本利润完整分析模块，计算各种作物的成本、利润和利润成本比，并生成可视化图表。

### clustering_full
聚类完整分析模块，使用自定义K-means算法对作物进行聚类分析，不依赖sklearn。

### price_analysis
平均售价分析模块，处理价格区间数据并计算平均售价。

### field_area_full
田地面积完整分析模块，创建农场面积矩阵并分析面积分布。

### plot_full
绘图完整模块，绘制种植面积趋势图。

### year2023_acres
2023年种植亩数分析模块。

### year2023_profit
2023年利润统计模块。

### data_label
数据标签处理模块。

### cost_reformat
成本数据整理模块。

### question2
问题2求解模块，优化作物种植分配。

### question3
问题3求解模块，优化三年轮作方案。

## 注意事项

1. 确保所有数据文件已正确放置在代码目录下
2. 首次运行前请安装所有依赖包
3. 代码使用中文标签，请确保系统支持中文显示
4. 聚类分析使用自定义K-means实现，无需安装sklearn
5. 代码中的文件路径是相对路径，确保在正确的目录下运行

## 输出文件

运行后会生成以下输出文件：

- `cost_profit_analysis.png` - 成本利润分析图
- `cost_profit_results.xlsx` - 成本利润分析结果
- `clustering_3d.png` - 三维聚类图
- `clustering_results.xlsx` - 聚类分析结果
- `average_prices.xlsx` - 平均售价结果
- `farm_data.xlsx` - 农场面积矩阵
- `farm_array.npy` - 农场面积矩阵(Numpy格式)
- `acres_trend.png` - 种植面积趋势图
- `问题2_种植方案.xlsx` - 问题2求解结果
- `问题3_轮作方案.xlsx` - 问题3求解结果

## 作者

CUMCM 2024 参赛团队