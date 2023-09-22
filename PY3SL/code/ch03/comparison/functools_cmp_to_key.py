"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 20:04:02
@Description: 
"""

import functools
from functools import cmp_to_key


class MyObject:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "MyObject({})".format(self.val)


def compare_obj(a, b) -> int:
    """
    Old-style comparison function.
    """
    print("comparing {} and {}".format(a, b))
    if a.val < b.val:
        return -1
    elif a.val > b.val:
        return 1
    return 0


# 可以用 cmp_to_key() 将比较函数转换为一个返回比对键的函数，
# 这个键用于确定元素在最终序列中的位置
get_key = cmp_to_key(compare_obj)


def get_key_wrapper(o):
    """
    Wrapper function for get_key to allow for print statements.
    """
    new_key = get_key(o)
    print("key_wrapper({})->{!r}".format(o, new_key))
    return new_key


objs = [MyObject(x) for x in range(5, 0, -1)]

for o in sorted(objs, key=get_key_wrapper):
    # sorted() 首先对序列中的每一个元素调用 get_key_wrapper() 以生成一个键
    # cmp_to_key() 返回的键是 functools 中定义的一个类的实例
    # 这个类使用传入的老式比较函数实现富比较 API
    # 所有键都创建之后，通过比较这些键来对序列排序
    print(o)
