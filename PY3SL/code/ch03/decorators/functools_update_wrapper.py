"""
@Title: 获取函数属性
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 17:09:26
@Description: partial 对象会丢失原函数的元数据
"""
# The partial object does not have __name__ or __doc__ attributes by default, and without
# those attributes, decorated functions are more difficult to debug. update_wrapper() can be
# used to copy or add attributes from the original function to the partial object.

from functools import partial, update_wrapper
from typing import Iterable
import functools


def my_func(a, b=2):
    """Docstring for my_func()."""

    print("  called my_func with:", (a, b))


def show_details(name, f: Iterable):
    """Show details of a callable object."""
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print("(no __name__)")
    print("  __doc__:", repr(f.__doc__))
    print()


# 这可以表明函数在这里是有 __name__ 与 __doc__
show_details("my_func", my_func)

p1 = partial(my_func, b=4)
show_details("raw wrapper", p1)

# 增加到包装器的属性在 WRAPPER_ASSIGNMENTS 种定义
# 另外 WRAPPER_UPDATES 列出来要修改的值
print("Updating wrapper:")
print("  assign:", functools.WRAPPER_ASSIGNMENTS)
print("  update:", functools.WRAPPER_UPDATES)
print()

# 更新了 p1 的函数名的函数文档，从 my_func 中复制的
update_wrapper(p1, my_func)
show_details("update wrapper", p1)
