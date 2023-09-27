"""
@Title: Creating decorators using classes
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 11:19:29
@Description: 
"""

import functools


class Debug(object):
    def __init__(self, function):
        self.function = function
        # the only notable difference between functions and classes
        # is that functools.wraps is now replaced with
        # functools.update_wrapper
        functools.update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        output = self.function(*args, **kwargs)
        name = self.function.__name__
        print(f"{name}({args!r}, {kwargs!r}): {output!r}")
        return output


@Debug
def add(a, b=0):
    return a + b
# def add(a, b=0):
#     return a + b
# add = Debug(add)


output = add(3)
output = add(10, b=2)
output = add(a=10, b=2)
