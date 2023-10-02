"""
@Title: Acquiring Function Properties for Decorators
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 17:50:55
@Description: 
"""
# 与 update_wraps 类似？
import sys
sys.path.append('./')
from functools import partial
from show_details import show_details
from typing import Iterable
import functools


def simple_decorator(f: Iterable):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print('  decorated:', f(a, b))
        print('  ', end=' ')
        return f(a, b=b)
    return decorated


def my_func(a, b=2) -> None:
    """my_func() is not complicated"""
    print("  my_func:", (a, b))
    return


# The raw function
show_details("my_func", my_func)
my_func("unwrapped, default b")
my_func("unwrapped, passing b", 3)
print()

# Wrap explicitly.
wrapped_my_func = simple_decorator(my_func)
show_details("wrapped_my_func", wrapped_my_func)
wrapped_my_func()
wrapped_my_func("args to wrapped", 4)
print()
# Wrap with decorator syntax.


@simple_decorator
def decorated_my_func(a, b):
    my_func(a, b)
    return


show_details("decorated_my_func", decorated_my_func)
decorated_my_func()
decorated_my_func("args to decorated", 4)

# functools provides a decorator, wraps(),
# that applies update_wrapper() to the decorated function.
