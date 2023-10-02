"""
@Title: 算术运算符 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 22:30:44
@Description: 
"""

from operator import abs, neg, pos, add, floordiv, mod, mul, pow, sub, truediv
from operator import and_, invert, lshift, or_, rshift, xor
a = -1
b = 5.0
c = 2
d = 6

print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)

print("\nPositive/Negative:")
print("abs(a):", abs(a))
print("neg(a):", neg(a))
print("neg(b):", neg(b))
print('pos(a):', pos(a))
print('pos(b):', pos(b))


print("\nArithmetic:")
print("add(a, b)     :", add(a, b))
# 3.0 之前的整数除法
print("floordiv(a, b):", floordiv(a, b))
print("floordiv(d, c):", floordiv(d, c))
print("mod(a, b)     :", mod(a, b))
print("mul(a, b)     :", mul(a, b))
print("pow(c, d)     :", pow(c, d))
print("sub(b, a)     :", sub(b, a))
# 浮点数除法
print("truediv(a, b) :", truediv(a, b))
print("truediv(d, c) :", truediv(d, c))

print('\nBitwise:')
print('and_(c, d)  :', and_(c, d))
print('invert(c)   :', invert(c))
print('lshift(c, d):', lshift(c, d))
print('or_(c, d)   :', or_(c, d))
print('rshift(d, c):', rshift(d, c))
print('xor(c, d)   :', xor(c, d))
