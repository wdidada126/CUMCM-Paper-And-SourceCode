#!/bin/bash

# 2023C蔬菜类商品的自动定价与补货决策 - 快速启动脚本

echo "=========================================="
echo "2023C蔬菜类商品的自动定价与补货决策 - Python代码集合"
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
python3 -c "import pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "警告: 未检测到pandas，正在安装依赖..."
    pip install -r requirements.txt
fi

# 显示使用说明
echo "=========================================="
echo "使用方法:"
echo "  ./run.sh <module> [args]"
echo ""
echo "可用模块:"
echo "  1. preprocess    - 数据预处理"
echo "  2. plot          - 绘图分析"
echo "  3. model_ai      - AI模型训练"
echo "  4. model_math    - 数学模型求解"
echo "  5. get_index     - 指标计算"
echo "  6. xiaohan     - 小韩的代码"
echo "  7. all           - 运行所有分析"
echo "  8. test          - 测试代码结构"
echo "=========================================="

if [ -z "$1" ]; then
    echo ""
    echo "示例:"
    echo "  ./run.sh preprocess"
    echo "  ./run.sh model_ai"
    echo "  ./run.sh model_math"
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
