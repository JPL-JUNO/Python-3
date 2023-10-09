"""
@Title: abc.Iterator 类，摘自 Lib/_collections_abc.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-06 00:47:09
@Description: https://github.com/python/cpython/blob/3.11/Lib/_collections_abc.py#L271
"""


class Iterable:
    pass


class Iterator(Iterable):
    __slots__ = {}

    @abstractmethod
    def __next__(self):
        'return the next item from the iterator, when exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        # 为 isinstance 和 issubclass 所作的结构类型检查提供支持
        if cls is Iterator:
            # _check_methods() 遍历类的 __mro__ 属性，检查积累有没有实现指定的方法
            return _check_methods(C, '__iter__', '__next__')
        return NotImplemented
