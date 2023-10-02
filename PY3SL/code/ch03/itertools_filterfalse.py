"""
@Title: filterfalse
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 16:51:51
@Description: 
"""
from itertools import filterfalse


def check_item(x) -> bool:
    print("Testing:", x)
    return x < 1


for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print("Yielding:", i)

# 与 filter 的结果正好成一个补集
