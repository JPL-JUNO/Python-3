"""
@File         : recipe_01_reveal.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2025-01-11 16:59:28
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from typing import reveal_type


def hex2rgb(hx_int: int | str) -> tuple[int, int, int]:
    if isinstance(hx_int, str):
        if hx_int[0] == "#":
            hx_int = int(hx_int[1:], 16)
        else:
            hx_int = int(hx_int, 16)

    reveal_type(hx_int)  # Only used by mypy. Must be removed.

    r, g, b = (hx_int >> 16) & 0xFF, (hx_int >> 8) & 0xFF, hx_int & 0xFF

    return r, g, b
