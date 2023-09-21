"""
@Title: 方法和函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 17:34:50
@Description: 
"""
# While partial() returns a callable ready to be used directly, partialmethod() returns a
# callable ready to be used as an unbound method of an object.

from functools import partial, partialmethod


def standalone(self, a=1, b=2):
    """Standalone function"""
    print("  called standalone with:", (self, a, b))
    if self is not None:
        print("  self.attr = ", self.attr)


class MyClass:
    """Demonstration class for functools"""

    def __init__(self):
        self.attr = "instance attribute"

    method1 = partialmethod(standalone)
    method2 = partial(standalone)


o = MyClass()
standalone(None)
print()

print("method1 as partialmethod")
# method1() 可以从 MyClass 的一个实例中调用，
# 这个实例作为第一个参数传入，这与采用通常方式定义的方法是一样的
o.method1()
print()

print("method2 as partial")
try:
    # method2() 未被定义绑定方法，所以必须显示传入 self 参数
    # 否则，这个调用会导致 TypeError
    o.method2()
except TypeError as err:
    print("ERROR: {}".format(err))
