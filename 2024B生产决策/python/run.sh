#!/bin/bash

# 2024B生产决策 - 快速启动脚本

echo "=========================================="
echo "2024B生产决策 - Python代码集合"
echo "=========================================="

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python3"
    exit 1
fi

echo "Python版本:"
python3 --version

# 检查依赖是否安装
echo ""
echo "检查依赖..."
python3 -c "import scipy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "警告: 未检测到scipy，正在安装依赖..."
    pip install -r requirements.txt
fi

# 显示使用说明
echo "=========================================="
echo "使用方法:"
echo "  ./run.sh <module> [args]"
echo ""
echo "可用模块:"
echo "  1. problem_1_binomial    - 二项分布最小值求解"
echo "  2. problem_1_normal      - 正态分布最小值求解"
echo "  3. problem_2             - 问题2决策分析"
echo "  4. problem_3             - 问题3半成品分析"
echo "  5. problem_4_sampling    - 问题4抽样模拟"
echo "  6. problem_4_p2          - 问题4-问题2执行"
echo "  7. problem_4_p3          - 问题4-问题3执行"
echo "  8. all                   - 运行所有分析"
echo "  9. test                  - 测试代码结构"
echo "=========================================="

if [ -z "$1" ]; then
    echo ""
    echo "示例:"
    echo "  ./run.sh problem_1_binomial"
    echo "  ./run.sh problem_2"
    echo "  ./run.sh problem_4_sampling"
    echo "  ./run.sh all"
    echo ""
    exit 0
fi

MODULE=$1
shift

case $MODULE in
    test)
        python3 test_structure.py
        ;;
    all)
        python3 main.py all
        ;;
    *)
        python3 main.py $MODULE $@
        ;;
esac
