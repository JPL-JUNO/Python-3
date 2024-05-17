"""
@File         : operators_expressions_and_data_manipulation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-30 16:13:08
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

42  # 十进制整数
0b101010  # 二进制整数
0o52  # 八进制整数
0x2A  # 十六进制整数

4.2
42.0
0.42
4.2e2
4.2e2
-4.2e-2

123_456_789
0x1234_5678
0b111_00_101
123.789_012

"hello world"
"hello world"
"""hello world"""
"""hello world"""

(1, 2, 3)
[1, 2, 3]
{1, 2, 3}
{"x": 1, "y": 2, "z": 3}

from math import sqrt

value = 2 + 3 + 5 + sqrt(6 + 7)


[1, 2, 3] + [4, 5]
[1, 2, 3] * 4
"%s has %d messages" % ("Dave", 37)

from fractions import Fraction

a = Fraction(2, 3)
b = 5
a + b

from decimal import Decimal

a = Fraction(2, 3)
b = Decimal("5")
a + b


a = 3
a = a + 1
a += 1

a = [1, 2, 3]
b = a
a += [4, 5]
a
b


def foo(x, items=None):
    if not items:
        items = []
    items.append(x)
    return items


foo(4)

a = []
foo(3, a)
a


def f(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


f(3, a)
a

if a <= b:
    min_value = a
else:
    min_value = b

min_value = a if a <= b else b

items = [3, 4, 5]
x, y, z = items

letters = "abc"
x, y, z = letters

items = [3, 4, 5]
d = {}
d["x"], d["y"], d["z"] = items

datetime = ((5, 9, 2008), (10, "30", "am"))
(month, day, year), (hour, minute, am_pm) = datetime

(_, day, _), (hour, _, _) = datetime

items = [1, 2, 3, 4, 5]
a, b, *extra = items
*extra, a, b = items
a, *extra, b = items

(month, *_), (hour, *_) = datetime

items = [1, 2, 3]
a = [10, *items, 11]
b = (*items, 10, *items)
c = {10, 11, *items}

a = [1, 2, 3]
b = [4, 5]
a + b

a = [3, 4, 5]
b = [a]
c = 4 * b
c
a[0] = -7
c


a = [3, 4, 5]
c = [list(a) for _ in range(4)]

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5]
a[:3]
a[-3:]
a[::2]
a[::-2]
a[0:5:2]
a[5:0:-2]
a[:5:1]
a[:5:-1]
a[5::1]
a[5::-1]
a[5:0:-1]


first_five = slice(0, 5)
s = "hello world"
print(s[first_five])

a = [1, 2, 3, 4, 5]
a[1] = 6
a
a[2:4] = [10, 11]
a
a[3:4] = [-1, -2, -3]
a
a[2:] = [0]
a

a = [1, 2, 3, 4, 5]
a[1::2] = [10, 11]
a[1::2] = [30, 40, 50]
