"""
@Title: 就地操作
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 16:17:21
@Description: 
"""

from operator import iadd, iconcat

a = -1
b = 5.0
c = [1, 2, 3]
d = ['a', 'b', 'c']
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

a = iadd(a, b)
print("a = iadd(a, b) =>", a)
print()

c = iconcat(c, d)
print("c = iconcat(c, d) =>", c)
