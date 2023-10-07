"""
@Title: Generators wrapping iterables
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 14:59:29
@Description: 
"""


def square(iterable):
    for i in iterable:
        yield i**2


assert list(square(range(5))) == [0, 1, 4, 9, 16]


def padding_square(iterable):
    yield "begin"
    for i in iterable:
        yield i**2
    yield "end"


assert list(padding_square(range(5))) == ['begin', 0, 1, 4, 9, 16, 'end']


def odd(iterable):
    for i in iterable:
        if i % 2:
            yield i


assert list(square(odd(range(10)))) == [1, 9, 25, 49, 81]
