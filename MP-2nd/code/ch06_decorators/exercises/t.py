"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 18:16:10
@Description: 不同的函数 t 共用同一个 count
"""
from typing import Callable
import functools


def test(function: Callable):
    count = []

    @functools.wraps(function)
    def _test(*args, **kwargs):
        result = function(*args, **kwargs)
        count.append(1)
        print(count)
        return result
    return _test


@test
def t():
    pass
# t = test(t)


for i in range(10):
    t()
