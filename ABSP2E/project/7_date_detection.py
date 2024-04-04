"""
@File         : 7_date_detection.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-13 19:58:02
@Email        : cuixuanstephen@gmail.com
@Description  : 日期检测
"""

import re

date_regex = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
date_regex.search("01/01/2024")


def date_decomposition(date: str) -> tuple[int, int, int]:
    """日期格式分解为年，月，日

    Parameters
    ----------
    date : str
        DD/MM/YYYY 格式的日期

    Returns
    -------
    tuple[int, int, int]
        年，月，日
    """
    date_regex = re.compile(r"(\d{2})/(\d{2})/(\d{4})")
    mo = date_regex.search(date)
    if mo:
        return int(mo.group(3)), int(mo.group(2)), int(mo.group(1))
    else:
        return None


def is_leap(year: int):
    if year % 4:
        return False
    else:
        if year % 100 or year % 400:
            return False
        else:
            return True


def is_valid_date(date: str) -> bool:
    try:
        year, month, day = date_decomposition(date)
    except ValueError:
        print("Invalid date Format")
    if month in (4, 6, 9, 11) and day <= 30:
        return True
    if month in (1, 3, 5, 7, 8, 12) and day <= 31:
        return True
    if month == 2:
        if is_leap(year):
            return day <= 29
        else:
            return day <= 28


if __name__ == "__main__":
    assert is_valid_date("22/03/2014") == True
    assert is_valid_date("29/02/2014") == False
    assert is_valid_date("29/02/2000") == True
    assert is_valid_date("29/02/1900") == False
