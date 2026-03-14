# 2024B生产决策 - Python代码集合

全国大学生数学建模竞赛 (CUMCM 2024) 问题B：企业生产决策

## 目录结构

```
python/
├── main.py                                    # 主程序入口
├── requirements.txt                           # Python依赖包列表
├── problem_1_binomial_distribution_min_value_solver.py    # 问题1-二项分布最小值求解
├── problem_1_normal_distribution_min_value_solver.py      # 问题1-正态分布最小值求解
├── problem_2_exhaustive_process_decision_analysis.py      # 问题2决策分析
├── problem_3_semi_finished_goods_analysis.py.py         # 问题3半成品分析
├── problem_4_sampling_simulation_and_plot.py.py         # 问题4抽样模拟
├── problem_4_defective_rate_change_with_problem_2_execution.py  # 问题4-问题2执行
├── problem_4_defective_rate_change_with_problem_3_execution.py.py  # 问题4-问题3执行
├── test_structure.py                          # 代码结构测试脚本
├── run.sh                                     # 快速启动脚本
├── README.md                                  # 本文件
└── DATA_README.md                             # 数据文件说明
```

## 安装依赖

```bash
pip install -r requirements.txt
```

### 依赖包列表

- scipy>=1.10.0 - 科学计算和统计分析
- pandas>=1.5.0 - 数据处理
- matplotlib>=3.7.0 - 数据可视化
- numpy>=1.23.0 - 数值计算

## 使用方法

### 运行特定模块

```bash
python3 main.py problem_1_binomial
python3 main.py problem_1_normal
python3 main.py problem_2
python3 main.py problem_3
python3 main.py problem_4_sampling
python3 main.py problem_4_p2
python3 main.py problem_4_p3
```

### 运行所有分析

```bash
python3 main.py all
```

### 使用run.sh快速启动

```bash
./run.sh <module>
```

### 测试代码结构

```bash
./run.sh test
```

## 模块说明

### problem_1_binomial
二项分布最小值求解模块，计算不同样本量下的临界值和p值，用于判断次品率是否超过标称值。

### problem_1_normal
正态分布最小值求解模块，计算抽样数量和拒收/接收阈值，用于零配件次品率的统计判断。

### problem_2
问题2决策分析模块，对给定的6种情况分别进行决策分析，找出最优的生产决策方案。

### problem_3
问题3半成品分析模块，分析多阶段生产过程中的半成品库存和决策优化。

### problem_4_sampling
问题4抽样模拟模块，通过蒙特卡洛模拟分析次品率估计的分布特性。

### problem_4_p2
问题4-问题2执行模块，在次品率变化的情况下重新执行问题2的决策分析。

### problem_4_p3
问题4-问题3执行模块，在次品率变化的情况下重新执行问题3的多阶段决策分析。

## 输出文件

运行后会生成以下输出文件：

- `decision_results.xlsx` - 问题2的决策结果
- `multi_stage_production_results.xlsx` - 问题3的多阶段生产结果
- `defect_rate_distribution.png` - 次品率估计分布图
- `optimal_strategies_distribution.xlsx` - 最优策略分布

## 注意事项

1. 首次运行前请安装所有依赖包
2. 代码使用中文标签，请确保系统支持中文显示
3. 问题2和问题3的决策分析可能需要较长时间运行
4. 问题4的抽样模拟需要大量计算，建议使用高性能计算资源

## 作者

CUMCM 2024 参赛团队