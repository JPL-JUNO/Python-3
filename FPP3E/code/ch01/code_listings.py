def sum_numeric(limit: int = 10) -> int:
    s = 0
    for n in range(1, limit):
        if n % 3 == 0 or n % 5 == 0:
            s += n
    return s


# 使用函数式范式
from collections.abc import Sequence


def sumr(seq: Sequence[int]) -> int:
    if len(seq) == 0:
        return 0
    # if not seq:
    #     return 0
    return seq[0] + sumr(seq=seq[1:])


from collections.abc import Sequence, Callable


def until(limit: int, filter_func: Callable[[int], bool], v: int) -> list[int]:
    if v == limit:
        return []
    elif filter_func(v):
        return [v] + until(limit, filter_func, v + 1)
    else:
        return until(limit, filter_func, v + 1)


def mult_3_5(x: int) -> bool:
    return x % 3 == 0 or x % 5 == 0


def sum_functional(limit: int = 10) -> int:
    return sumr(until(limit, mult_3_5, 0))


# 使用混合范式
def sum_hybrid(limit: int = 10) -> int:
    return sum(n for n in range(1, limit) if n % 3 == 0 or n % 5 == 0)
