"""
@Title: 编写只接受关键字参数的函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 10:54:40
@Description: 
"""


def recv(max_size, *, block):
    "receives a message"
    pass


# recv(1024, True)
recv(1024, block=True)


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


assert minimum(1, 5, 2, -5, 10) == -5
assert minimum(1, 5, 2, -5, 10, clip=0) == 0
