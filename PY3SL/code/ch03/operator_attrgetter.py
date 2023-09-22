"""
@Title: 属性和元素 “获取方法”
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 16:21:11
@Description: 
"""
from operator import attrgetter


class MyObj:
    """"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return "MyObj({})".format(self.arg)


l = [MyObj(i) for i in range(5)]
print("objects   : ", l)


# Extract the 'arg' value from each object.
g = attrgetter('arg')
vals = [g(i) for i in l]
print("arg values:", vals)

# Sort using arg.
l.reverse()
print("reversed  :", l)
print("sorted    :", sorted(l, key=g))
# Attribute getters work like
# lambda x,n='arg': getattr(x,n)

# print("sorted    :", sorted(l, key=lambda x, n="arg": getattr(x, n)))

# Item getters work like
# lambda x,y=5: x[y]
