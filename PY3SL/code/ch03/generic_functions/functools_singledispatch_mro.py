"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 21:39:41
@Description: 没有找到这个类型的完全匹配时，会计算继承顺序，并使用最接近的匹配类型
"""

import functools


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(C, D):
    pass


@functools.singledispatch
def my_func(arg):
    print("default my_func({})".format(arg.__class__.__name__))


@my_func.register(A)
def my_func_A(arg):
    # 如果第一个参数的类型是 A，那么调用这个方法
    print("my_func_A({})".format(arg.__class__.__name__))


@my_func.register(B)
def my_func_B(arg):
    print("my_func_B({})".format(arg.__class__.__name__))


@my_func.register(C)
def my_func_C(arg):
    print("my_func_C({})".format(arg.__class__.__name__))


my_func(A())
my_func(B())
my_func(C())
my_func(D())
my_func(E())

# 类 D 和 E 与已注册的任何泛型函数都不完全匹配，
# 所选择的函数取决于类层级结构（MRO）
