"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-12-04 21:10:15
@Description: 
"""
import argparse

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action='store_true', default=False)
parser.add_argument('-b', action='store', dest='b')
parser.add_argument('-c', action='store', dest='c', type=int)

# 向单字符选项传值有多种方法
print(parser.parse_args(['-a', '-bval', '-c', '3']))
