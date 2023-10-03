"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 21:18:37
@Description: 
"""

from collections.abc import Iterable
from typing import TypeVar

from comparable import SupportsLessThan

LT = TypeVar('LT', bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> Iterable[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
