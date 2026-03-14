# 项目总结

## 项目概述

本项目是2024年全国大学生数学建模竞赛（CUMCM 2024）问题C：种植策略的Python代码集合。

## 项目结构

```
2024C种植策略/python代码/
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
├── run.sh                     # 快速启动脚本
├── README.md                  # 项目说明文档
├── DATA_README.md             # 数据文件说明
└── PROJECT_SUMMARY.md         # 本文件
```

## 完成的功能

### 1. 代码组织
- ✓ 将所有Python代码组织成模块化结构
- ✓ 创建主程序入口 main.py
- ✓ 每个模块有独立的功能和清晰的文档

### 2. 依赖管理
- ✓ 创建 requirements.txt 文件
- ✓ 列出所有必需的依赖包
- ✓ 移除 scikit-learn 依赖（使用自定义K-means实现）

### 3. 自定义K-means实现
- ✓ 实现不依赖sklearn的K-means聚类算法
- ✓ 包含数据标准化功能
- ✓ 支持三维聚类可视化

### 4. 用户友好性
- ✓ 创建 run.sh 快速启动脚本
- ✓ 创建 test_structure.py 测试脚本
- ✓ 提供详细的使用说明
- ✓ 提供数据文件示例

### 5. 文档
- ✓ README.md - 项目说明文档
- ✓ DATA_README.md - 数据文件说明
- ✓ PROJECT_SUMMARY.md - 项目总结文档
- ✓ 每个模块都有详细的注释

## 安装和使用

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行代码

#### 方法1: 使用run.sh脚本

```bash
./run.sh <module>
```

#### 方法2: 直接运行main.py

```bash
python3 main.py <module>
```

#### 可用模块

- cost_profit_full - 成本利润完整分析
- clustering_full - 聚类完整分析
- price_analysis - 平均售价分析
- field_area_full - 田地面积完整分析
- plot_full - 绘图完整模块
- year2023_acres - 2023年种植亩数分析
- year2023_profit - 2023年利润统计
- data_label - 数据标签处理
- cost_reformat - 成本数据整理
- question2 - 问题2求解
- question3 - 问题3求解
- all - 运行所有分析

### 测试代码结构

```bash
./run.sh test
```

## 技术特点

### 1. 模块化设计
- 每个功能模块独立
- 易于维护和扩展
- 代码复用性高

### 2. 无外部依赖的K-means
- 不依赖scikit-learn
- 使用numpy实现核心算法
- 减少安装复杂度

### 3. 中文支持
- 完整的中文注释
- 支持中文标签显示
- 适合中文用户使用

### 4. 错误处理
- 完善的异常处理
- 友好的错误提示
- 数据验证

## 输出文件

运行代码后会生成以下输出文件：

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

## 注意事项

1. 确保所有数据文件已正确放置在代码目录下
2. 首次运行前请安装所有依赖包
3. 代码使用中文标签，请确保系统支持中文显示
4. 聚类分析使用自定义K-means实现，无需安装sklearn
5. 代码中的文件路径是相对路径，确保在正确的目录下运行

## 依赖包列表

- pandas>=1.5.0 - 数据处理
- numpy>=1.23.0 - 数值计算
- matplotlib>=3.7.0 - 数据可视化
- openpyxl>=3.1.0 - Excel文件读写
- scipy>=1.10.0 - 科学计算和优化

## 作者

CUMCM 2024 参赛团队

## 版本历史

### v1.0 (2024-03-14)
- 初始版本
- 完成代码模块化组织
- 创建requirements.txt
- 实现自定义K-means聚类
- 创建run.sh快速启动脚本
- 创建test_structure.py测试脚本
- 完善文档

## 许可证

本代码仅供学习和研究使用。