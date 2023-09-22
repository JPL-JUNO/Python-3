"""
@Title: 泛型函数 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 21:30:51
@Description: 
"""

import functools


@functools.singledispatch
def my_func(arg):
    print("default my_func({!r})".format(arg))
# 用 functools.singledispatch() 包装的第一个函数是默认实现
# 在未指定其他类型特定函数时就使用这个默认实现


@my_func.register(int)
def my_func_int(arg):
    print("my_func_int({})".format(arg))


@my_func.register(list)
def my_func_list(arg):
    print("my_func_list()")
    for item in arg:
        print("  {}".format(item))
# 新函数的 register() 属性相当于另一个修饰符，用于注册替代实现


my_func("string argument")
my_func(1)
my_func(2.3)
my_func(['a', 'b', 'c'])
