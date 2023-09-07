>>> def count(n):
...     while True:
...         yield n
...         n += 1
...
>>> c = count(0)
>>> c[10:20]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
>>>

迭代器和生成器是没法执行普通的切片操作的，这是因为不知道它们的长度是多少（而且它们也没有实现索引）。islice()产生的结果是一个迭代器，它可以产生出所需要的切片元素，但这是通过访问并丢弃所有起始索引之前的元素来实现的。之后的元素会由 islice 对象产生出来，直到到达结束索引为止。

需要重点强调的是 islice()会消耗掉所提供的迭代器中的数据。由于迭代器中的元素只能访问一次，没法倒回去，因此这里就需要引起我们的注意了。如果之后还需要倒回去访问前面的数据，那也许就应该先将数据转到列表中去。

>>> import itertools
>>> for x in itertools.islice(c, 10, 20):
...     print(x)
...
10
11
12
13
14
15
16
17
18
19
>>>