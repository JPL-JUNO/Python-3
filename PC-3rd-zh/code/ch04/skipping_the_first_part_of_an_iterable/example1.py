"""
@Title: 跳过可迭代对象中的前一部分元素
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 09:29:42
@Description: 
"""

with open("./passwd.txt") as f:
    for line in f:
        print(line, end='')
print("\n")
from itertools import dropwhile
with open('./passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith("#"), f):
        print(line, end='')
