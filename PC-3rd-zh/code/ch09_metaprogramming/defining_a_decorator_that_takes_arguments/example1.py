"""
@Title: 定义一个可接受参数的装饰器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 13:42:51
@Description: 
"""
from functools import wraps
import logging


def logged(level, name=None, message=None):
    """"""
    def decorate(func):
        log_name = name if name else func.__name__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "Example")
def spam():
    print("Spam")
