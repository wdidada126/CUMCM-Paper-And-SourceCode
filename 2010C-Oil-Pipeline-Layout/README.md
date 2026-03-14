# 2010C 输油管的布置 - Oil Pipeline Layout
# 全国大学生数学建模竞赛 CUMCM 2010

## 问题描述
2010年C题：输油管的布置优化问题

## 代码说明
本目录包含两个程序，用于解决输油管布置的最优化问题：

### 1. company3_eval_2_1.cpp
- **功能**：按照公司三的评估标准计算总费用
- **算法**：穷举法（暴力搜索）
- **变量**：
  - h1, h2: 两个分点的高度
  - w: 总费用
  - min: 最小费用
  - a, b: 最优解对应的h1和h2值

### 2. company3_eval_3_1.cpp
- **功能**：公司三评估总费用计算
- **算法**：三维穷举搜索
- **变量**：
  - x2, y1, y2: 三个决策变量
  - w: 总费用
  - min: 最小费用
  - a, b, c: 最优解对应的变量值

## 编译运行

### 方法1: 使用CMake（推荐）
```bash
cd 2010C-Oil-Pipeline-Layout
mkdir build
cd build
cmake ..
make
./company3_eval_2_1
./company3_eval_3_1
```

### 方法2: 直接编译
```bash
g++ -o company3_eval_2_1 company3_eval_2_1.cpp -lm
g++ -o company3_eval_3_1 company3_eval_3_1.cpp -lm
./company3_eval_2_1
./company3_eval_3_1
```

## 运行结果
- **程序1**：输出最小费用和对应的h1、h2值
- **程序2**：输出最小费用min、x2、y2、y1的值

## 环境要求
- C++编译器（支持C++11标准）
- CMake 3.10+
- 数学库（libm）
