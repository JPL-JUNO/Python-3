"""
@Title: 扁平化处理嵌套型的序列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 09:49:48
@Description: 
"""
# 如果 python 版本大于 3.10
from collections.abc import Iterable
# 小于 3.10
# from collections import Iterable


def flatten_good(items, ignore_types=(str, bytes)):
    """
    >>> items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    >>> for x in flatten_good(items):
    ...     print(x)
    ...
    Dave
    Paula
    Thomas
    Lewis
    >>>
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten_good(x)
        else:
            yield x


def flatten_bad(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten_bad(x):
                yield i
        else:
            yield x
