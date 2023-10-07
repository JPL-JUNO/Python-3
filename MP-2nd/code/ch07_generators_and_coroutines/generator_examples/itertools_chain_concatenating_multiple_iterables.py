"""
@Title: itertools.chain – Concatenating multiple iterables
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 18:25:16
@Description: 可以将不同类型的可迭代数据连接起来（concatenate）
"""


def chain(*iterables):
    for iterable in iterables:
        # yields all items from the given iterable
        yield from iterable


a = 1, 2, 3
b = [4, 5, 6]
c = 'abc'
assert list(chain(a, b, c)) == [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

try:
    a + b + c
except TypeError as err:
    print(err)


def chain(*iterables):
    """更加啰嗦的写法"""
    for iterable in iterables:
        for i in iterable:
            yield i
