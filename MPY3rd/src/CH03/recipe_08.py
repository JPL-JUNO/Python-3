"""
@File         : recipe_08.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-13 21:37:54
@Email        : cuixuanstephen@gmail.com
@Description  : Designing recursive functions around Python’s stack limits
"""

from typing import Iterable


def fact_r(n: int) -> int:
    if n == 0:
        return 1
    return n * fact_r(n - 1)


def prod_i(int_iter: Iterable[int]) -> int:
    p = 1
    for x in int_iter:
        p *= x
    return p


def fibo(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


from functools import cache


@cache
def fibo_r(n: int) -> int:
    if n <= 2:
        return 1
    else:
        return fibo_r(n - 1) + fibo_r(n - 2)


from collections.abc import Iterator


def fibo_iter() -> Iterator[int]:
    a, b = 1, 1
    yield a
    while True:
        yield b
        a, b = b, a + b


def fibo_i(n: int) -> int:
    for i, f_i in enumerate(fibo_iter()):
        if i == n:
            break
    return f_i


if __name__ == "__main__":
    # Note that the range object is lazy; it doesn’t create a big list object, avoiding the allocation
    # of a great deal of memory.
    assert prod_i(range(1, 6)) == 120
    assert fact_r(5) == 120
