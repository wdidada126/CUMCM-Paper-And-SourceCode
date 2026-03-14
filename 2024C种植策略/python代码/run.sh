#!/bin/bash

# 2024C种植策略 - 快速启动脚本

echo "=========================================="
echo "2024C种植策略 - Python代码集合"
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

# 检查数据文件
echo ""
echo "检查数据文件..."
DATA_FILES=("附件2.2.xlsx" "附件2(1)1.xlsx" "聚类.xls")
MISSING=0
for file in "${DATA_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        echo "警告: 缺少数据文件: $file"
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -gt 0 ]; then
    echo ""
    echo "提示: 请将以下数据文件放在当前目录:"
    echo "  - 附件2.2.xlsx"
    echo "  - 附件2(1)1.xlsx"
    echo "  - 聚类.xls"
    echo ""
fi

# 显示使用说明
echo "=========================================="
echo "使用方法:"
echo "  ./run.sh <module> [args]"
echo ""
echo "可用模块:"
echo "  1. cost_profit_full   - 成本利润完整分析"
echo "  2. clustering_full    - 聚类完整分析"
echo "  3. price_analysis     - 平均售价分析"
echo "  4. field_area_full    - 田地面积完整分析"
echo "  5. plot_full          - 绘图完整模块"
echo "  6. year2023_acres     - 2023年种植亩数分析"
echo "  7. year2023_profit    - 2023年利润统计"
echo "  8. data_label         - 数据标签处理"
echo "  9. cost_reformat      - 成本数据整理"
echo " 10. question2          - 问题2求解"
echo " 11. question3          - 问题3求解"
echo " 12. all                - 运行所有分析"
echo " 13. test               - 测试代码结构"
echo "=========================================="

if [ -z "$1" ]; then
    echo ""
    echo "示例:"
    echo "  ./run.sh cost_profit_full"
    echo "  ./run.sh clustering_full"
    echo "  ./run.sh question2"
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
