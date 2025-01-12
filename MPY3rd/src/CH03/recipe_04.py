"""
@File         : recipe_04.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-11 22:38:59
@Email        : cuixuanstephen@gmail.com
@Description  : Forcing keyword-only arguments with the * separator
"""


def T_wc(T: float, V: float) -> float:
    return 13.12 + 0.6215 * T - 11.37 * V**0.16 + 0.3965 * T * V**0.16


import csv
from typing import TextIO


def wind_chill(
    start_T: int,
    stop_T: int,
    step_T: int,
    start_V: int,
    stop_V: int,
    step_V: int,
    target: TextIO,
):
    """Wind Chill Table."""
    writer = csv.writer(target)
    heading = [""] + [str(t) for t in range(start_T, stop_T, step_T)]
    writer.writerow(heading)

    for V in range(start_V, stop_V, step_V):
        row = [float(V)] + [T_wc(T, V) for T in range(start_T, stop_T, step_T)]
        writer.writerow(row)


from pathlib import Path


def wind_chill_k(
    *,
    start_T: int,
    stop_T: int,
    step_T: int,
    start_V: int,
    stop_V: int,
    step_V: int,
    target: TextIO,
) -> None: ...


import sys


def wind_chill_k2(
    *,
    start_T: int,
    stop_T: int,
    step_T: int,
    start_V: int,
    stop_V: int,
    step_V: int,
    target: TextIO = sys.stdout,
) -> None: ...


wind_chill_k2(start_T=0, stop_T=-45, step_T=-5, start_V=0, stop_V=20, step_V=2)
