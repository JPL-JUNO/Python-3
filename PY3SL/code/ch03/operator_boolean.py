"""
@Title: 逻辑操作 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 22:22:00
@Description: 
"""

from operator import not_, truth, is_, is_not

a = -1
b = 5

print("a = ", a)
print("b = ", b)

print("not_(a)     :", not_(a))
print("truth(a)    :", truth(a))
print("is_(a, b)   :", is_(a, b))
print("is_not(a, b):", is_not(a, b))
