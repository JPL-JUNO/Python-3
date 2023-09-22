"""
@Title: 结合操作符和定制类
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 16:35:34
@Description: 
"""
from operator import lt, add


class MyObj:
    """Example for operator overloading"""

    def __init__(self, val):
        super(MyObj, self).__init__()
        self.val = val

    def __str__(self):
        return "MyObj({})".format(self.val)

    def __lt__(self, other):
        """compare for less than"""
        print("Testing {} < {}".format(self, other))
        return self.val < other.val

    def __add__(self, other):
        """Add values"""
        print("Adding {} + {}".format(self, other))
        return MyObj(self.val + other.val)


a = MyObj(1)
b = MyObj(2)

print("Comparison:")
print(lt(a, b))

print("\nArithmetic:")
print(add(a, b))
