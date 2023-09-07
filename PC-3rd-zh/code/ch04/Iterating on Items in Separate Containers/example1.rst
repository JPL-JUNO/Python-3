>>> from itertools import chain
>>> a = [1, 2, 3, 4]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
...     print(x)
...
1
2
3
4
x
y
z
>>>

>>> active_items = set()
>>> inactive_items = set()
>>> for item in chain(active_items, inactive_items):
...     # Process item
...     pass
...
>>>

采用 chain() 的解决方案比下面这种写两个单独的循环要优雅得多：

>>> for item in active_items:
...     pass
...
>>> for item in inactive_items:
...     pass
...
>>>

.. inefficient
>>> for x in a + b
...     pass
...
>>>

.. better
>>> for x in chain(a, b):
...     pass
...
>>>