"""
@Title: Total ordering – Making classes sortable 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-27 20:57:48
@Description: 需要实现类比较时候，提供一种简洁的写法，必须实现__eq__和一个不等方法
"""

import functools


class Value(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.value}>"


class Spam(Value):
    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value


@functools.total_ordering
class Egg(Value):
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


numbers = [4, 2, 3, 4]
spams = [Spam(n) for n in numbers]
eggs = [Egg(n) for n in numbers]
sorted(spams)
sorted(eggs)

values = [Value(n) for n in numbers]
sorted(values, key=lambda v: v.value)


# def sort_by_attribute(attr, key_func=getattr):
#     def _sort_by_attribute(cls):
#         def __lt__(self, other):
#             return getattr(self, attr) < getattr(other, attr)

#         def __eq__(self, other):
#             return getattr(self, attr) <= getattr(other, attr)
#         # 有些问题，有些类的双下函数是只读的❌
#         cls.__lt__ = __lt__
#         cls.__eq__ = __eq__
#         return functools.total_ordering(cls)
#     return _sort_by_attribute


# @sort_by_attribute
# class Spam(Value):
#     pass


# spams = [Spam(n) for n in numbers]
# sorted(spams)
