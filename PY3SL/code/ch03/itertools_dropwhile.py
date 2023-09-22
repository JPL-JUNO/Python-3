"""
@Title: dropwhile
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 12:58:34
@Description: 
"""
from itertools import dropwhile


def should_drop(x) -> bool:
    print("Testing:", x)
    return x < 1


for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    # 在 1 的时候之后停止，不在调用 should_drop，同时将 1 之后生成输入迭代器
    # dropwhile() 并不会过滤输入的每一个元素，第一次条件为 False 之后，输入迭代器的所有其余元素都会返回（含）
    print("Yielding:", i)
