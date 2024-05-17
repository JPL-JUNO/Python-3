# 比较协议

最基本的检查是 is 运算符进行同一性检查，同一性检查不考虑存储在对象中的值。

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> c = [1, 2, 3]
>>> c is a
False
>>>

如果 ``__bool__`` 未定义，则 ``__len__`` 将作为回退方案。如果 ``__bool__`` 和 ``__len__`` 都未定义，则将对象简单地视为 True

根据我的理解，（<、>、<=、>=运算符的逻辑是下面这样）

>>> a = 42
>>> b = 52.3
>>> a < b
True
>>> if isinstance(type(b), type(a)):
...     b.__gt__(a)
... else:
...     if a.__lt__(b) == NotImplemented:
...         b.__gt__(a)
...
True
>>>

