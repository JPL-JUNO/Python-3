# 求值顺序

下表列出了 Python 运算符的运算顺序（优先规则）。除幂(`**`)运算符之外的所有运算符均按从左到右的顺序进行计算，并在表中按优先级从最高到最低的顺序列出。也就是说，表中首先列出的运算符先于稍后列出的运算符进行计算。包含在一起的运算符（例如 `x * y`、 `x / y`、 `x // y`、 `x @ y` 和 `x % y`）具有相同的优先级。

表中的求值顺序与x和y的类型无关。因此，即使尽管用户定义的对象可以重新定义各个运算符，但无法自定义基础计算顺序、优先级和关联性规则。

|Operator|Name
|---|---
|`(...), [...], {...}`|元组、列表和字典的创建
|`s[i], s[i:j]`|索引和切片
|`s.attr`|属性查找
|`f(...)`|函数调用
|`+x`, `-x`, `~x`|一元运算符
|`x ** y`|幂 (右结合)
|`x * y`,`x / y`, `x // y`, `x % y`, `x @ y`|乘法、除法、整数除法、取模、矩阵乘法
|`x + y`, `x - y`|加法、减法
|`x << y`, `x >> y`|位移
|`x & y`|位与
|`x ^ y`|位异或
|`x \| y`|位或
|`x < y`, `x <= y`, `x > y`, `x >= y`, `x == y`, `x !=y`, `x is y`, `x is not y`, `x in y`, `x not in y`|比较、同一性与序列成员测试
|`not x`|逻辑非
|`x and y`|逻辑与
|`x or y`|逻辑或
|`lambda args: expr`|匿名函数
|`expr if expr else expr`|条件表达式
|`name := expr`|赋值表达式

优先级规则的一个常见混淆是按位与(`&`)和按位或(`|`)来运算符用于表示逻辑与（`and`）和逻辑或（`or`）：

```python
>>> a = 10
>>> a <= 10 and 1 < a
True
>>> a <= 10 & 1 < a
False
>>>
```

后一个表达式被计算为：`a <= (10 & 1) < a`，即 `a <= 0 < a`

这可能看起来像是一个生僻的边缘情况，但它在面向数据的包（例如 numpy 和 pandas）中经常出现。逻辑运算符 `and` 和 `or`无法自定义，因此只能使用按位运算符，尽管它们具有更高的优先级并且在布尔关系中使用时计算结果不同。

## 最后的话：数据的秘密生活

Python 最常见的用途之一是涉及数据操作和分析的应用程序。在这里，Python 提供了一种“领域语言”来思考你的问题。内置运算符和表达式是该语言的核心，其他所有内容都基于它构建。因此，一旦你围绕 Python 的内置对象和操作建立了一种直觉，你就会发现你的直觉适用于任何地方。

举个例子，假设你正在使用数据库，并且想要迭代查询返回的记录。很可能会使用 `for` 语句来做到这一点。或者，假设正在处理数字数组，并希望对数组执行逐个元素的数学运算。您可能认为标准数学运算符会起作用，而且直觉是正确的。或者，假设正在使用库通过 HTTP 获取数据，并且想要访问 HTTP 标头的内容。数据很有可能以类似字典的方式呈现。