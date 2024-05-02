# 生成器表达式

生成器表达式是一个对象，它执行与列表推导相同的计算，但迭代地产生结果。语法与列表推导相同，只是使用圆括号而不是方括号。与列表推导式不同，生成器表达式实际上并不创建列表或立即计算括号内的表达式。相反，它创建一个生成器对象，**通过迭代按需生成值**。

```python
>>> nums = [1, 2, 3, 4]
>>> squares = (x * x for x in nums)
>>> squares
<generator object <genexpr> at 0x000001E74972C790>
>>>
```

生成器表达式只能使用一次。如果你尝试第二次迭代，你将一无所获：

```python
>>> next(squares)
1
>>> next(squares)
4
>>>
>>> for n in squares:
...     print(n)
...
9
16
>>> for n in squares:
...     print(n)
...
>>>
```

列表推导和生成器表达式之间的区别很重要，但也很微妙。使用列表推导，Python 实际上会创建一个包含结果数据的列表。使用生成器表达式，Python 会创建一个只知道如何按需生成数据的生成器。在某些应用程序中，这可以大大提高性能和内存使用率。以下是一个例子：

```python
f = open("data.txt")  # Open a file
lines = (t.strip() for t in f)  # Read lines, strip trailing/leading whitespace
comments = (t for t in lines if t[0] == "#")  # All comments
for c in comments:
    print(c)
```

在此示例中，提取行并去除空格的生成器表达式实际上并未读取整个文件并将其保存在内存中。提取注释的表达式也是如此。相反，当程序开始在随后的 for 循环中迭代时，会逐一读取文件的行。在此迭代期间，文件的行根据需要生成并进行相应的过滤。事实上，在此过程中，整个文件都不会被加载到内存中。因此，这是从 GB 大小的 Python 源文件中提取注释的高效方法。

与列表推导不同，生成器表达式不会创建像序列一样工作的对象。它无法建立索引，并且通常的列表操作（例如 `append()`）都不起作用。但是，可以使用 `list()` 将生成器表达式生成的项目转换为列表：

```python
clist = list(comments)
```

当生成器表达式作为单个函数参数传递时，可以删除一组括号。

```python
sum((x * x for x in values))
sum(x * x for x in values)
```

在这两种情况下，都会创建一个生成器 `(x * x for x in values)` 并将其传递给 `sum()` 函数。
