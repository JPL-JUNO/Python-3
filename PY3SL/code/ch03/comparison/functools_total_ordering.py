"""
@Title: 富比较
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 18:20:48
@Description: 
"""

# The rich comparison API is designed to allow classes with complex comparisons to implement
# each test in the most efficient way possible. However, for classes where comparison is
# relatively simple, there is no point in manually creating each of the rich comparison meth-
# ods. The total_ordering() class decorator takes a class that provides some of the methods,
# and adds the rest of them.


import functools
import inspect
from pprint import pprint

# 补齐了其他没有实现的比较方法，至少要一个不等比较，相同比较要自己实现


@functools.total_ordering
class MyObject:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other: 'MyObject') -> bool:
        print("  testing __eq__({}, {})".format(self.val, other.val))
        return self.val == other.val

    def __gt__(self, other: 'MyObject') -> bool:
        print("  testing __gt__({}, {})".format(self.val, other.val))
        return self.val > other.val


print("Methods:\n")
# 获取 MyObject 的全部函数
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print("\nComparisons:")
for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
    # 'a < b' 因为没有实现，测试的是大于和等于？
    print("\n{:<6}:".format(expr))
    result = eval(expr)
    print("  result of {}: {}".format(expr, result))
