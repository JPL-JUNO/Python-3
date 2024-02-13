"""
@File         : 7_strong_password_detection.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 22:37:03
@Email        : cuixuanstephen@gmail.com
@Description  : 强口令检测
"""

import re


def length(text) -> bool:
    return len(text) >= 8


def lower(text) -> bool:
    regex = re.compile(r"([a-z])")
    return regex.search(text)


def upper(text) -> bool:
    regex = re.compile(r"([A-Z])")
    return regex.search(text)


def digit(text) -> bool:
    regex = re.compile(r"(\d+)")
    return regex.search(text)


def strong_password(text) -> bool:
    if length(text) and lower(text) and upper(text) and digit(text):
        return True
    else:
        return False


if __name__ == "__main__":
    assert strong_password("abcd") == False
    assert strong_password("abcdefghiABCD") == False
    assert strong_password("abcdefghiABCD123") == True
