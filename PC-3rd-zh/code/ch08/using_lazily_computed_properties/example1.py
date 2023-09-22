"""
@Title: 让属性具有惰性求值的能力
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 16:15:45
@Description: 我们想将一个只读的属性定义为 property 属性方法，只有在访问它时才参与计算。但是，一旦访问了该属性，我们希望把计算出的值缓存起来，不要每次访问它时都重新计算。
"""


class LazyProperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


# def lazy_property(func):
#     # 如果使用这个版本的实现，就会发现 set 操作是不允许执行的。
#     name = '_lazy_' + func.__name__

#     @property
#     def lazy(self):
#         if hasattr(self, name):
#             return getattr(self, name)
#         else:
#             value = func(self)
#             setattr(self, name, value)
#             return value
#     return lazy


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print("Computing perimeter")
        return 2 * math.pi * self.radius
