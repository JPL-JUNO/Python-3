"""
@File         : balanced_symbols.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-20 21:51:54
@Email        : cuixuanstephen@gmail.com
@Description  : 普通情况：匹配符号
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
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(o, c):
    opens = "([{"
    closes = ")]}"
    return opens.index(o) == closes.index(c)


if __name__ == "__main__":
    print(par_checker("{{([][])}()}"))
    print(par_checker("[{()]"))
