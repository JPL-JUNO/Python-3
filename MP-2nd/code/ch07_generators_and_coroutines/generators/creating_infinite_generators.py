"""
@Title: Creating infinite generators
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-06 21:04:33
@Description: 
"""


def count(start=0, step=1, stop=None):
    n = start
    while stop is not None and n < stop:
        yield n
        n += step


assert list(count(10, 2.5, 20)) == [10, 12.5, 15.0, 17.5]
