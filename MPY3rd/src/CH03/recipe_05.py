"""
@File         : recipe_05.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-12 14:00:19
@Email        : cuixuanstephen@gmail.com
@Description  : Defining position-only parameters with the / separator
"""


def F_1(c: float) -> float:
    return 32 + 9 * c / 5


def F_2(c: float, /) -> float:
    return 32 + 9 * c / 5


def C(f: float, /, truncate: bool = False) -> float:
    c = 5 * (f - 32) / 9
    if truncate:
        return round(c, 0)
    return c
