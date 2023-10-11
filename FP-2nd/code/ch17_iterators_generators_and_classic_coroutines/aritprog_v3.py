"""
@Title: 使用 itertools 模块生成等差数列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-11 22:22:26
@Description: 
"""

import itertools
gen = itertools.count(1, .5)
next(gen)
next(gen)
next(gen)

# 绝对不允许这样操作，count() 是无穷的，该函数不会停止
# list(itertools.count())

# itertools.takewhile 函数则不同
# 它返回一个使用另一个生成器的生成器，在指定条件求值为 False 时停止

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
list(gen)


def aritprog_gen(begin, step, end=None):
    """缺点在于使用的累积策略，对浮点数可能没有那么的精确（只是相比于乘法）"""
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end, ap_gen)
