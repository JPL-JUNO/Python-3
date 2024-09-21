"""
@File         : base_converter.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 13:07:14
@Email        : cuixuanstephen@gmail.com
@Description  : 将十进制数转换成任意进制数(不超过 16 进制)
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from sources.list03_01 import Stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string


print(base_converter(25, 2))
print(base_converter(125, 16))
