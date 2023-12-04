"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-12-04 21:18:45
@Description: 
"""

import argparse

parser = argparse.ArgumentParser(
    description='Example with nonoptional arguments'
)

# 如果命令行中遗漏了其中任何一个参数，或者给定值不能转换为正确的类型，便会报告错误
parser.add_argument('count', action='store', type=int)
parser.add_argument('units', action='store')

print(parser.parse_args())
