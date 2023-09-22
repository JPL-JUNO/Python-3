"""
@Title: 简化数据结构的初始化过程
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 16:33:22
@Description: 倦了编写高度重复且样式相同的__init__()函数
"""
import math


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


if __name__ == "__main__":
    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    class Point(Structure):
        _fields = ['x', 'y']

    class Circle(Structure):
        _fields = ["radius"]

        def area(self):
            return math.pi * self.radius ** 2
