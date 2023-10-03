"""
@Title: 有界的 TypeVar
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 19:12:25
@Description: 
"""

from collections import Counter
from collections.abc import Iterable, Hashable
from typing import TypeVar

HashableT = TypeVar('HashableT', bound=Hashable)


# def mode(data: Iterable[Hashable]) -> Hashable:
#     """Now the problem is that the type of the returned item is Hashable: an ABC that
#     implements only the __hash__ method. So the type checker will not let us do
#     anything with the return value except call hash() on it. Not very useful.
#     """


def mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 1:
        raise ValueError("no mode for empty data")
    return pairs[0][0]
