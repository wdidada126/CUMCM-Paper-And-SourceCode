#!/bin/bash
# 批量转换MATLAB项目到Octave的脚本

cd /mnt/d/develops/git/github/cpp/mathematical_modeling/CUMCM-Paper-And-SourceCode

# 需要转换的项目列表
projects=(
    "2016A系泊系统的设计"
    "2016B小区开放OK"
    "2017ACT系统参数标定及成像OK"
    "2017B拍照赚钱OK"
    "2018A高温服装OK"
    "2018B智能RGV的动态调度策略"
    "2019A高压油管的压力控制"
    "2019B同心协力"
    "2020A炉温曲线"
    "2020C中小微企业的信贷决策"
    "2021A射电望远镜"
    "2021B乙醇偶合制备烯烃"
    "2021C原材料的订购与运输"
    "2022B无人机定位OK"
    "2022C古代玻璃制品成分分析"
    "2023A定日镜场的优化设计"
    "2023C蔬菜类商品的自动定价与补货决策"
    "2023华为杯C题竞赛评审方案"
    "2023电工杯B题人工智能"
    "2024A板凳龙"
)

for project in "${projects[@]}"; do
    echo "正在处理: $project"
    if [ -d "$project" ]; then
        mkdir -p "$project/octave"
        
        # 查找所有包含.m文件的位置
        m_files=$(find "$project" -name "*.m" 2>/dev/null)
        if [ -n "$m_files" ]; then
            # 复制所有子文件夹
            cd "$project"
            # 复制所有可能的子文件夹到octave目录
            for subdir in */; do
                if [ -d "$subdir" ] && [ "$subdir" != "octave/" ]; then
                    cp -r "$subdir" octave/
                fi
            done
            # 复制根目录下的所有MATLAB相关文件
            cp -f *.m octave/ 2>/dev/null || true
            cp -f *.mat octave/ 2>/dev/null || true
            cp -f *.fig octave/ 2>/dev/null || true
            cp -f *.txt octave/ 2>/dev/null || true
            cp -f *.xls* octave/ 2>/dev/null || true
            cd ..
            echo "  ✓ 完成"
        else
            echo "  ⚠ 没有找到.m文件"
        fi
    else
        echo "  ✗ 项目不存在"
    fi
done

echo "所有项目处理完成！"
