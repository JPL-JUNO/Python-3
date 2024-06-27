"""
@File         : data_structures.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-06-10 00:58:57
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import timeit
from statistics import median
from random import choice

# 这是一个字符串常量
from string import ascii_uppercase


def random_string(length):
    """生成由 length 个大写 ascii 字符组成的随机字符串"""
    return "".join(choice(ascii_uppercase) for _ in range(length))


def print_scaling(
    stmt, setup, sizes=[10_000, 20_000, 30_000], repeat=False, units="us"
):
    """
    打印在 `setup` 之后执行的语句 `stmt` 的缩放信息。

    `setup` 和 `stmt` 参数采用模板字符串，其中“{N}”
    将被替换为输入的大小。

    `repeat` 标志确定是否需要在每次测试运行之间运行设置。
    """
    values = []
    for size in sizes:
        if repeat:
            timings = timeit.repeat(
                stmt.format(N=size), setup=setup.format(N=size), number=1, repeat=1_000
            )
            values.append(min(timings))
        else:
            timings = timeit.repeat(
                stmt.format(N=size),
                setup=setup.format(N=size),
                number=1_000,
                repeat=3,
            )
            values.append(min(t / 1000 for t in timings))
    unit_factor = {"us": 1e6, "ms": 1e3}[units]

    print(
        " | ".join(
            "N = {} t = {:.2f} ({})".format(n, t * unit_factor, units)
            for n, t in zip(sizes, values)
        )
    )


from bisect import bisect_left


def index_bisect(a, x):
    """"""
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError
