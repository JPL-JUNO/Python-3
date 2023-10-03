"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 18:57:17
@Description: 
"""

from collections import Counter
from collections.abc import Iterable

# from typing import TypeVar
# T = TypeVar('T')
# def mode(data: Iterable[T]) -> T:
#     """看似简单，但不正确的签名
#     任何可以迭代的对象都与 Iterable['T] 相容，包括 Counter 无法处理的不可哈希的可迭代类型
#     """


def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common[1]

    if len(pairs) == 0:
        raise ValueError("no mode for empty data")
    return pairs[0][0]


# TypeVar accepts extra positional arguments to restrict the type parameter. We can
# improve the signature of mode to accept specific number types, like this:
from decimal import Decimal
from fraction import Fraction
from typing import TypeVar
NumberT = TypeVar('NumberT', float, Decimal, Fraction)
# 似乎可以使用 Union 来进行，但是发送要保守，即返回的值应该明确类型


def mode(data: Iterable[NumberT]) -> NumberT:
    pass


# However, the statistics.mode documentation includes this example:
# In a hurry, we could just add str to the NumberT definition:
NumberT = TypeVar('NumberT', float, Decimal, Fraction, str)
# That certainly works, but NumberT is badly misnamed if it accepts str.
# More importantly,
# we can’t keep listing types forever, as we realize mode can deal with them.
