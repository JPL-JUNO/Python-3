"""
@Title: 创建一种新形式的类属性或实例属性
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 15:44:36
@Description: 想创建一种新形式的实例属性，它可以拥有一些额外的功能，比如说类型检查。
"""

# Descriptor attribute for an integer type-checked attribute


class Integer:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an integer")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer("x")
    y = Integer("y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
