# 循环和迭代

可以使用 for 和 while 语句来实现循环。

while 语句执行语句，直到关联表达式的计算结果为 false。for 语句迭代所有元素，直到没有更多元素可用。for 语句适用于任何支持迭代的对象。这包括内置序列类型（例如列表、元组和字符串），也包括任何实现迭代器协议的对象。

在语句 `for i in s` 中，变量 `i` 称为迭代变量。在每个循环迭代时，它从 s 接收一个新值。**迭代变量的范围不是 for 语句私有的**。如果先前定义的变量具有相同的名称，则该值将被覆盖。此外，**迭代变量在循环完成后保留最后的值**。

如果迭代产生的元素是大小相同的可迭代对象，则可以使用如下语句将它们的值解包到单独的迭代变量中：

```python
s = [(1, 2, 3), (4, 5, 6)]
for x, y, z in s:
    pass
```

如果可迭代生成的项具有不同的大小，则可以使用通配符解包将多个值放入变量中。

```python
s = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
for x, y, *extra in s:
    pass
```

循环时，除了数据值之外，有时还需要跟踪数字索引，Python 提供了一个内置函数 `enumerate()`，可用于简化此代码。

```python
for i, x in enumerate(s):
    pass
```

`enumerate(s)` 创建一个迭代器，生成元组 (0, s[0])、 (1, s[1])、 (2, s[2])等。可以通过 `enumerate()` 的 `start` 关键字参数提供不同的计数起始值。

另一个常见的循环问题是对两个或多个可迭代对象进行并行迭代，可以使 `zip()` 函数。`zip(s, t)` 将可迭代对象 s 和 t 组合成可迭代元组 (s[0], t[0]), (s[1], t[1]), (s[2], t[2])，依此类推，如果 s 和 t 的长度不等，则以最短的 s 和 t 停止。`zip()` 的结果是一个迭代器，它在迭代时产生结果。如果希望将结果转换为列表，请使用 `list(zip(s, t))`。

要跳出循环，请使用 `break` 语句。要跳转到循环的下一次迭代（跳过循环体的其余部分），请使用 `continue` 语句。

```python
with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            break  # A blank line, stop reading
        # process the stripped line
        pass

with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            continue  # Skip the blank line
        # process the stripped line
        pass
```

break 和 continue 语句仅适用于正在执行的最内层循环。如果需要跳出深度嵌套的循环结构，可以使用异常。Python 不提供“goto”语句。

还可以将 else 语句附加到循环结构中。循环的 else 子句仅在循环运行完成时执行。这要么立即发生（如果循环根本不执行）要么在最后一次迭代之后发生。如果使用 break 语句提前终止循环，则将跳过 else 子句。

```python
with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            break
        # process the stripped line
        pass
    else:
        raise RuntimeError("Missing section separator")
```

循环 else 子句的主要用例是在迭代数据的代码中，但如果循环过早中断，则需要设置或检查某种标志或条件。例如，如果没有使用 else，则之前的代码可能必须使用标志变量重写，如下所示：

```python
found_separator = False
with open("foo.txt") as file:
    for line in file:
        stripped = line.strip()
        if not stripped:
            found_separator = True
            break
    if not found_separator:
        raise RuntimeError("Missing section separator")
```
