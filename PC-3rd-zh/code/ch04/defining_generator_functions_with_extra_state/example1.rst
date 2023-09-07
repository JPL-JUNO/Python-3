上面所示的方法有一个潜在的微妙之处，那就是如果打算用除了 for 循环之外的技术来驱动迭代过程的话，可能需要额外调用一次 iter()。

>>> f = open("example1.txt")
>>> lines = LineHistory(f)
>>> next(lines)
>>> next(lines)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'LineHistory' object is not an iterator
>>> it = iter(lines)
>>> next(it)
'hello\n'
>>> next(it)
'world\n'
>>> next(it)
'cpp\n'
>>> next(it)
'python\n'
>>> next(it)
'R\n'
>>> next(it)
'visualization\n'
>>> next(it)
'python\n'
>>> next(it)
'deep learning\n'
>>> next(it)
'machine learning'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>