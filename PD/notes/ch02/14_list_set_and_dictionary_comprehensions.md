# 列表、Set 与字典解析式

涉及数据的最常见操作之一是将数据集合转换为另一种数据结构。例如，这里我们获取列表中的所有项目，应用操作并创建一个新列表：

```python
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)
```

由于这种操作非常常见，因此可以将其用作列表推导式运算符。以下是此代码的更紧凑版本：

```python
squares = [n * n for n in nums]
```

还可以对操作应用过滤器：

```python
squares = [n * n for n in nums if n > 2]
```

列表推导的一般语法如下：

```python
[
    expression
    for item1 in iterable1
    if condition1
    for item2 in iterable2
    if condition2
    ...
    for itemN in iterableN
    if conditionN
]
```

此语法等效于以下代码：

```python
result = []
for item1 in iterable1:
    if condition1:
        for item2 in iterable2:
            if condition2:
                ...
                for itemN in iterableN:
                    if conditionN:
                        result.append(expression)
```

不建议嵌套过长的解析式，否则难以看懂。

```python
>>> portfolio = [
...     {"name": "IBM", "shares": 100, "price": 91.1},
...     {"name": "MSFT", "shares": 50, "price": 45.67},
...     {"name": "HPE", "shares": 75, "price": 34.51},
...     {"name": "CAT", "shares": 60, "price": 67.89},
...     {"name": "IBM", "shares": 200, "price": 95.25},
... ]
>>>
>>> names = [s["name"] for s in portfolio]
>>>
>>> more100 = [s["name"] for s in portfolio if s["shares"] > 100]
>>>
>>> cost = sum([s["shares"] * s["price"] for s in portfolio])
>>>
>>> names_shares = [(s["name"], s["shares"]) for s in portfolio]
>>>
```

列表推导中使用的所有变量都是列表推导私有的。不必担心此类变量会覆盖其他同名变量。例如：

```python
>>> x = 42
>>> squares = [x * x for x in [1, 2, 3]]
>>> squares
[1, 4, 9]
>>> x
42
>>>
```

除了创建列表，还可以通过将括号改为花括号来创建 Set。这称为集合推导。集合推导将提供一组不同的值。

```python
>>> names = {s["name"] for s in portfolio}
>>> names
{'IBM', 'HPE', 'CAT', 'MSFT'}
>>>
```

如果指定键：值对，将创建一个字典。这被称为字典推导。

```python
>>> prices = {s["name"]: s["price"] for s in portfolio}
>>> prices
{'IBM': 95.25, 'MSFT': 45.67, 'HPE': 34.51, 'CAT': 67.89}
>>>
```

**创建集合和字典时，请注意后面的条目可能会覆盖前面的条目**。例如，在价格字典中，可以获得“IBM”的最新价格。第一个价格会丢失。

在一个解析式中，不可能包含任何类型的异常处理。如果这是一个问题，请考虑用函数包装异常，如下所示：

```python
>>> def to_int(x):
...     try:
...         return int(x)
...     except ValueError:
...         return None
... 
>>> 
>>> values = ["1", "2", "-4", "n/a", "-3", "5"]
>>> data1 = [to_int(x) for x in values]
>>> data1
[1, 2, -4, None, -3, 5]
>>> # 需要两次调用函数
>>> data2 = [to_int(x) for x in values if to_int(x) is not None]
>>> data2
[1, 2, -4, -3, 5]
>>>
```

通过使用 `:=` 可以避免上一个示例中 `to_int(x)` 的双重计算：

```python
>>> data3 = [v for x in values if (v := to_int(x)) is not None]
>>> data3
[1, 2, -4, -3, 5]
>>> data4 = [v for x in values if (v := to_int(x)) is not None and v >= 0]
>>> data4
[1, 2, 5]
>>>
```
