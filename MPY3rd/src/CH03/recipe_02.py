"""
@File         : recipe_02.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-11 21:44:13
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import random


def die() -> int:
    return random.randint(1, 6)


def craps() -> tuple[int, int]:
    return (die(), die())


def zonk() -> tuple[int, ...]:
    return tuple(die() for _ in range(6))


def craps_v2() -> tuple[int, ...]:
    return tuple(die() for _ in range(2))


def dice_v2(n: int) -> tuple[int, ...]:
    return tuple(die() for _ in range(n))


def dice_v3(n: int = 2) -> tuple[int, ...]:
    return tuple(die() for _ in range(n))
