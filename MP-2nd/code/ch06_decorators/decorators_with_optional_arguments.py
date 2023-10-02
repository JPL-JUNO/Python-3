"""
@Title: 带有可选参数的装饰器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 10:15:25
@Description: 
"""
# we need to check the decorator arguments
# to see if they are the decorated method or a regular argument.
# The only caveat is that the optional argument should not be callable.
# If the argument has to be callable, you will need to pass it as a
# keyword argument instead.
import functools


def add(function=None, add_n=0):
    if not callable(function):
        if function is not None:
            add_n = function
        return functools.partial(add, add_n=add_n)

    @functools.wraps(function)
    def _add(n):
        return function(n) + add_n
    return _add


@add
def add_zero(n):
    return n
# add_zero = add(add_zero)


@add(1)
def add_one(n):
    return n
# add_one = add(1)(add_one)


@add(add_n=2)
def add_two(n):
    return n
# add_two = add(add_n=2)(add_two)


assert add_zero(5) == 5
assert add_one(5) == 6
assert add_two(5) == 7
