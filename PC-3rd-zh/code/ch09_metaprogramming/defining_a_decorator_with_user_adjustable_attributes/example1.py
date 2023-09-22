"""
@Title: 定义一个属性可由用户修改的装饰器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 14:23:49
@Description: 
引入访问器函数，通过使用 nonlocal 关键字声明变量来修改装饰器内部的属性。之后把访问器
函数作为函数属性附加到包装函数上。
"""

from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function.
    level is the logging level, name is the logger name,
    and message is the log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)

        # attach setter functions
        # 关键的访问器函数
        # 它们以属性的形式
        # 附加到了包装函数上。
        # 每个访问器函数允许对 nonlocal 变量赋值来调整内部参数。
        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_message(new_msg):
            nonlocal log_msg
            log_msg = new_msg
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam!")


import logging
logging.basicConfig(level=logging.DEBUG)
add(2, 3)

# change the log message
add.set_message("Add called")
# DEBUG:__main__:Add called
add(2, 3)

# change the log level
add.set_level(logging.WARNING)
add(2, 3)
