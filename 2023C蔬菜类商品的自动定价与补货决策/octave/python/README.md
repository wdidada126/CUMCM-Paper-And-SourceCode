# 2023C蔬菜类商品的自动定价与补货决策 - Python代码集合

全国大学生数学建模竞赛 (CUMCM 2023) 问题C：蔬菜类商品的自动定价与补货决策

## 目录结构

```
python/
├── main.py                           # 主程序入口
├── requirements.txt                  # Python依赖包列表
├── preprocess.py                     # 数据预处理模块
├── analyse.py                        # 绘图分析模块
├── model_AI.py                       # AI模型训练模块
├── model_math.py                     # 数学模型求解模块
├── get_index.py                      # 指标计算模块
├── XiaoHan.py                        # 小韩的代码
├── define.py                         # 全局定义模块
├── test_structure.py                 # 代码结构测试脚本
├── run.sh                            # 快速启动脚本
├── README.md                         # 本文件
└── DATA_README.md                    # 数据文件说明
```

## 安装依赖

```bash
pip install -r requirements.txt
```

### 依赖包列表

- pandas>=1.5.0 - 数据处理
- numpy>=1.23.0 - 数值计算
- matplotlib>=3.7.0 - 数据可视化
- scipy>=1.10.0 - 科学计算
- scikit-learn>=1.3.0 - 机器学习
- tensorflow>=2.12.0 - 深度学习
- seaborn>=0.12.0 - 统计数据可视化
- openpyxl>=3.1.0 - Excel文件读写

## 使用方法

### 运行特定模块

```bash
python3 main.py preprocess
python3 main.py plot
python3 main.py model_ai
python3 main.py model_math
python3 main.py get_index
python3 main.py xiaohan
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

### preprocess
数据预处理模块，包括：
- 数据清洗和格式化
- 单品名称标准化
- 数据透视表生成
- 多个Excel文件的合并处理

### analyse
绘图分析模块，包括：
- 互相关矩阵热力图
- 销售单价与销量的散点图
- 数据可视化

### model_AI
AI模型训练模块，包括：
- 神经网络模型训练 (NN)
- 高斯过程回归模型训练 (GPR)
- 决策树回归模型训练 (DTR)
- 模型性能评估和保存

### model_math
数学模型求解模块，包括：
- 基于星期和价格的利润计算
- 最优价格组合搜索
- 补货量计算
- 总利润最大化

### get_index
指标计算模块，包括：
- 季度、月度、周度、小时度的指标计算
- 销量平均值计算
- 批发价格平均值计算

### XiaoHan
小韩的代码模块，实现第三题的补货量和定价计算。

## 数据文件

需要将以下数据文件放在 `define.py` 中定义的 `xlsx_path` 路径下：

- `附件1.xlsx` - 品类信息
- `附件2.xlsx` - 销售数据
- `附件3.xlsx` - 批发价格数据

## 输出文件

运行后会生成以下输出文件：

- `df1.xlsx` - 清洗后的品类数据
- `df2.xlsx` - 重构后的销售数据
- `df3.xlsx` - 合并后的销售、价格、批发价格数据
- `df4.xlsx` - AI模型训练数据
- `品类_quarter.xlsx` - 品类季度指标
- `品类_month.xlsx` - 品类月度指标
- `品类_week.xlsx` - 品类周度指标
- `品类_hour.xlsx` - 品类小时度指标
- `单品_quarter.xlsx` - 单品季度指标
- `单品_month.xlsx` - 单品月度指标
- `单品_week.xlsx` - 单品周度指标
- `单品_hour.xlsx` - 单品小时度指标
- `互相关矩阵_*.png` - 互相关矩阵热力图
- `互相关矩阵_*.xlsx` - 互相关矩阵数据
- `*.png` - 散点图
- `model_*.h5` - 神经网络模型
- `model_*.pkl` - 高斯过程回归模型
- `model_*.joblib` - 决策树回归模型
- `model_*.mat` - MATLAB格式模型文件

## 注意事项

1. 确保所有数据文件已正确放置在代码目录下
2. 首次运行前请安装所有依赖包
3. 代码使用中文标签，请确保系统支持中文显示
4. AI模型训练需要较长时间和较高的计算资源
5. 代码中的路径是Windows路径，需要根据实际情况修改

## 作者

CUMCM 2023 参赛团队