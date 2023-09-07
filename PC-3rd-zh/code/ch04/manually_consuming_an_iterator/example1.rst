>>> items = [1, 2, 3]
>>> # 获取迭代器
>>> it = iter(items) # invokes items.__iter__
>>> # run the iterator
>>> next(it)         # invokes it.__next__
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration