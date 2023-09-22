"""
@Title: Partials work with any callable object, not just with stand-alone functions.
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 17:26:18
@Description: 
"""

import functools
from typing import Iterable


class MyClass:
    """Demonstration class for functools"""

    def __call__(self, e, f=6):
        """Docstring for MyClass.__call__"""
        print("  called object with:", (self, e, f))


def show_details(name: str, f: Iterable) -> None:
    """"""
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=' ')
    try:
        print(f.__name__)
    except AttributeError:
        print('(no __name__)')
    print("  __doc__", repr(f.__doc__))
    return


o = MyClass()
show_details("instance", o)
o("e goes here")
# 该对象确实可以调用，因为实现了 __call__ 协议，但是是没有 __name__ 的
print()

p = functools.partial(o, e="default for e", f=8)
functools.update_wrapper(p, o)
show_details("instance wrapper", p)
p()
