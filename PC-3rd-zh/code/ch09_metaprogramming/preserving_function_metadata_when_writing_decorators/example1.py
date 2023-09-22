"""
@Title: 编写装饰器时如何保存函数的元数据
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 10:11:08
@Description: 
"""

import time
from functools import wraps


def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


def time_this_forget_wrap(func):
    """忘记写@wraps()导致丢失被包装函数的元数据"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper


@time_this
def count_down(n: int):
    """
    Count down
    """
    while n > 0:
        n -= 1


@time_this_forget_wrap
def count_down_forget(n: int):
    """丢失元数据"""
    while n > 0:
        n -= 1


count_down(100_000)
print(count_down.__name__)
print(count_down.__doc__)
print(count_down.__annotations__)

# 被包装的函数元数据丢失了
count_down_forget(100_000)
print(count_down_forget.__name__)
print(count_down_forget.__annotations__)
print(count_down_forget.__doc__)

# @wraps 装饰器的一个重要特性
# 就是它可以通过__wrapped__属性来访问被包装的那个
# 函数。
count_down.__wrapped__(100_000)

# __wrapped__属性的存在同样使得装饰器函数
# 可以合适地将底层被包装函数的签名暴露出来。
from inspect import signature
print(signature(count_down))
