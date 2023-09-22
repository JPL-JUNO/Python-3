>>> x = 10
>>> a = lambda y: x + y
>>> x = 20
>>> b = lambda y: x + y
>>> a(10)
30
>>> b(10)
30

这里的问题在于 lambda 表达式中用到的 x 是一个自由变量，在运行时才进行绑定而不是定义的时候绑定。因此，lambda 表达式中 x 的值应该是在执行时确定的，执行时 x的值是多少就是多少。

>>> x = 15
>>> a(10)
25
>>> x = 3
>>> a(10)
13
>>>

如果希望匿名函数可以在定义的时候绑定变量，并保持值不变，那么可以将那个值作为默认参数实现：

>>> x = 10
>>> a = lambda y, x=x: x + y
>>> x = 20
>>> b = lambda y, x=x: x + y
>>> a(10)
20
>>> b(10)
30

提到的问题一般比较容易出现在那些对 lambda 函数过于“聪明”的应用上。比方说，通过列表推导来创建一列 lambda 表达式，或者在一个循环中期望 lambda 表达式能够在定义的时候记住迭代变量。

>>> funcs = [lambda x: x+n for n in range(5)]
>>> for f in funcs:
...     print(f(0))
...
4
4
4
4
4
>>>
>>> funcs = [lambda x, n=n: x+n for n in range(5)]
>>> for f in funcs:
...     print(f(0))
...
0
1
2
3
4
>>>
