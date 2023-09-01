>>> my_list = [1, 4, -5, 10, -7, 2, 3, -1]
>>> [n for n in my_list if n > 0]
[1, 4, 10, 2, 3]
>>> [n for n in my_list if n < 0]
[-5, -7, -1]
>>> pos = (n for n in my_list if n > 0)
>>> pos
<generator object <genexpr> at 0x000001A21FC0B1D0>
>>> for x in pos:
...     print(x)
...
1
4
10
2
3


>>> my_list = [1, 4, -5, 10, -7, 2, 3, -1]
>>> import math
>>> [math.sqrt(n) for n in my_list if n > 0]
[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]

>>> clip_neg = [n if n > 0 else 0 for n in my_list]
>>> clip_neg
[1, 4, 0, 10, 0, 2, 3, 0]
>>> clip_pos = [n if n < 0 else 0 for n in my_list]
>>> clip_pos
[0, 0, -5, 0, -7, 0, 0, -1]