"""
@Title: 对装饰器进行解包装
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 13:35:46
@Description: 假设装饰器的实现中已经使用了@wraps一般来说我们可以通过访问__wrapped__属性来获取对原始函数的访问。
"""

from functools import wraps


def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2")
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


add(2, 3)
# 这个问题已经被修复
add.__wrapped__(2, 3)
