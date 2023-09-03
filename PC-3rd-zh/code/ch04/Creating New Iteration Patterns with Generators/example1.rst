>>> # Create the generator, notice no output appears
>>> def count_down(n):
...     print("Starting to count from", n)
...     while n > 0:
...         yield n
...         n -= 1
...     print("Done")
... 
>>> c = count_down(3)
>>> c
<generator object count_down at 0x000001FF2C92F2A0>
>>> # Run to first yield and emit a value
>>> next(c)
Starting to count from 3
3
>>> # Run to the next yield
>>> next(c)
2
>>> # Run to the next yield
>>> next(c)
1
>>> # Run to next yield (iteration stops)
>>> next(c)
Done
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

这里的核心特性是生成器函数只会在响应迭代过程中的“next”操作时才会运行。一旦生成器函数返回，迭代也就停止了。但是，通常用来处理迭代的 for 语句替我们处理了这些细节，因此一般情况下不必为此操心。