"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 22:27:54
@Description: 
"""

from operator import lt, le, eq, ne, ge, gt
a = 1
b = 5.0

print("a = ", a)
print("b = ", b)

for func in (lt, le, eq, ne, ge, gt):
    print("{}(a, b): {}".format(func.__name__, func(a, b)))
