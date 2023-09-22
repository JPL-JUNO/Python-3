"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 14:09:23
@Description: 这个迭代器将会返回输入迭代器由保证测试条件为 True 的元素
"""
from itertools import takewhile


def should_take(x):
    print("Testing:", x)
    return x < 2


for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    # 一旦 should_take() 返回 False，takewhile() 就停止处理输入
    print("Yielding:", i)
