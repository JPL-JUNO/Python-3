"""
@Title: 对迭代器做切片操作
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 09:15:16
@Description: 
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
c[10:20]
