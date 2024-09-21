"""
@File         : balance_parentheses.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-20 20:51:34
@Email        : cuixuanstephen@gmail.com
@Description  : 匹配括号
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from sources.list03_01 import Stack


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


print(par_checker("((()))"))
print(par_checker("(()"))
