import sys
import os

# 添加packages目录到Python路径
script_dir = os.path.dirname(os.path.abspath(__file__))
packages_path = os.path.join(script_dir, 'packages')
if os.path.exists(packages_path) and packages_path not in sys.path:
    sys.path.insert(0, packages_path)

# 现在导入define模块
import define

# 重新设置路径
os.chdir(define.xlsx_path)
