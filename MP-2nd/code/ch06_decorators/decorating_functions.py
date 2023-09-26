"""
@Title: 装饰函数 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 21:14:20
@Description: 
"""


def decorator(function):
    return function


def add(a, b):
    return a + b


add = decorator(add)


@decorator
def add(a, b):
    return a + b


import functools


def decorator(function):
    # this decorator makes sure we mimic the wrapped function
    @functools.wraps(function)
    def _decorator(a, b):
        # pass the modified arguments to the function
        result = function(a, b + 5)

        # log the function call
        name = function.__name__
        print(f'{name}(a={a}, b={b}): {result}')

        # return a modified result
        return result + 4
    return _decorator


@decorator
def func(a, b):
    return a + b


assert func(1, 2) == 12

print("## generic function decorators")


def decorator(function):
    @functools.wraps(function)
    def _decorator(*args, **kwargs):
        a, b = args
        return function(a, b + 5)
    return _decorator


@decorator
def func(a, b):
    return a + b


assert func(1, 2) == 8
try:
    func(a=1, b=2)
except ValueError as err:
    print(err)


def add(a, b, /):
    """仅接受位置参数"""
    return a + b
# This code uses positional-only arguments
# (the / as the last function argument),
# which have been supported since Python 3.8.


try:
    add(a=1, b=2)
except TypeError as err:
    print(err)


def add(*, a, b):
    """仅接受关键字参数"""
    return a + b


try:
    add(1, 2)
except TypeError as err:
    print(err)


import inspect


def decorator(function):
    # Use the inspect module to get function signature
    signature = inspect.signature(function)

    @functools.wraps(function)
    def _decorator(*args, **kwargs):
        # bind the arguments to the given *arg and **kwargs
        # if you want to make arguments optional, use
        # signature.bind_partial instead
        bound = signature.bind(*args, **kwargs)
        # apply the defaults so b is always filled
        bound.apply_defaults()

        # Extract the filled arguments. if the number of
        # arguments is still expected to be fixed, you can use tuple unpacking
        # a, b = bound.arguments.values()
        a = bound.arguments['a']
        b = bound.arguments['b']
        return function(a, b + 5)
    return _decorator


@decorator
def func(a, b=3):
    return a + b


assert func(1, 2) == 8
assert func(a=1, b=2) == 8
assert func(a=1) == 9

print("## The importance of functools.wraps")
# functools.wraps(function)
# 无论什么时候写装饰器，上面这一行代码是必须写的，否则将丢失很多元数据


def decorator(function):
    def _decorator(*args, **kwargs):
        return function(*args, **kwargs)
    return _decorator


@decorator
def add(a, b):
    """Add a and b"""
    return a + b


help(add)
# 表明实际调用的是 _decorator
add.__name__


def decorator(function):
    @functools.wraps(function)
    def _decorator(*args, **kwargs):
        return function(*args, **kwargs)
    return _decorator


@decorator
def add(a, b):
    """Add a and b"""
    return a + b


help(add)
add.__name__

print("## Chaining or nesting decorators")
# 装饰器的顺序非常重要


def track(function=None, label=None):
    if label and not function:
        # 如果标签不是 None，但函数没有传递，那么就返回这个函数，并且将其标签设置为标签默认
        return functools.partial(track, label=label)
    print(f"initializing {label}")

    @functools.wraps(function)
    def _track(*args, **kwargs):
        print(f"calling {label}")
        function(*args, **kwargs)
        print(f"called {label}")
    return _track


@track(label="outer")
@track(label="inner")
def func():
    print("func")


print('--------------------------')
func()
# the decorators are called from outer to inner before running the function
# and running from inner to outer when processing the results.
