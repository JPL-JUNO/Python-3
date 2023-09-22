>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2:4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [999, 998]
>>> items
[0, 1, 999, 998, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]

>>> a = slice(10, 50, 2)
>>> a.start
10
>>> a.stop
50
>>> a.step
2

>>> s = "helloworld"
>>> a = slice(5, 100, 2)
>>> a.indices(len(s))
(5, 10, 2)
>>> for i in range(*a.indices(len(s))): # 把 a.indices(len(s)) 的三个参数赋值给 range 的三个参数
...     print(s[i])
...
w
r
d