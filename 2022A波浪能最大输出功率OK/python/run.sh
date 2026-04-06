#!/bin/bash

# 2022A波浪能最大输出功率 - 快速启动脚本

echo "=========================================="
echo "2022A波浪能最大输出功率 - Python代码集合"
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
python3 -c "import numpy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "警告: 未检测到numpy，正在安装依赖..."
    pip install -r requirements.txt --break-system-packages
fi

# 显示使用说明
echo "=========================================="
echo "使用方法:"
echo "  ./run.sh <module> [args]"
echo ""
echo "可用模块:"
echo "  1. problem_1_1   - 第一题第一问"
echo "  2. problem_1_2   - 第一题第二问"
echo "  3. problem_2_1   - 第二题第一问"
echo "  4. problem_2_2   - 第二题第二问"
echo "  5. problem_3     - 第三题"
echo "  6. problem_4     - 第四题"
echo "  7. all           - 运行所有问题"
echo "  8. test          - 测试代码结构"
echo "=========================================="

if [ -z "$1" ]; then
    echo ""
    echo "示例:"
    echo "  ./run.sh problem_1_1"
    echo "  ./run.sh problem_2_1"
    echo "  ./run.sh problem_3"
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
