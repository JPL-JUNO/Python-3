"""
@Title: Singletons – Classes with a single instance
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-27 17:31:42
@Description: 实现一种 单一模式的设计模式，每个类只能有一个对象
"""
# DecoratedClass = decorator(RegularClass)

import functools


def singleton(cls):
    instances = dict()

    @functools.wraps(cls)
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class SomeSingleton(object):
    def __init__(self):
        print("Executing init")
# SomeSingleton = singleton(SomeSingleton)
# SomeSingleton = _singleton()
# 非第一个实例
# SomeSingleton = instances[cls]
# 如果是第一个实例
# SomeSingleton = cls(*args, **kwargs)
# SomeSingleton = SomeSingleton(*args, **kwargs)
# 初始化没有变化，只是添加了一些判断


a = SomeSingleton()
b = SomeSingleton()
assert a is b

a.x = 123
assert b.x == 123
