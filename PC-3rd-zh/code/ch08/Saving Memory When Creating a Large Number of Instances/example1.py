"""
@Title: 当创建大量实例时如何节省内存
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 11:25:57
@Description: 程序创建了大量的（比如百万级）实例，为此占用了大量的内存。
"""


class Date:
    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
