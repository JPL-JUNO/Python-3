"""
@Title: 给函数添加一个包装
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 09:50:10
@Description: 
"""

import time
from functools import wraps


def time_this(func):
    """
    报告运行时间的装饰器
    """
    @wraps(func)  # 用来保存函数的元数据，这样函数名、文档字符串、函数注解以及函数签名都不会丢失
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

# 装饰器就是一个函数，
# 它可以接受一个函数作为输入并返回一个新的函数作为输出。


@time_this
def count_down(n):
    """
    Count down

    装饰器就是一个函数，
    它可以接受一个函数作为输入并返回一个新的函数作为输出。

    等同于下面：
    ```
    def count_down(n):
        pass
    count_down = time_this(count_down)
    ```
    装饰器内部的代码一般会涉及创建一个新的函数，利用`*args`和`**kwargs`来接受任意的参数。

    """
    while n > 0:
        n -= 1


count_down(100_000)
count_down(10_000_000)
