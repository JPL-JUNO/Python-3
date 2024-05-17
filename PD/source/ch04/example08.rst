大多数 Python 语言特性都是由协议（Protocol）定义的

>>> def compute_cost(unit_price, num_units):
...     return unit_price * num_units
... 
>>> compute_cost(1.25, 50)
62.5

>>> from fractions import Fraction
>>> compute_cost(Fraction(5, 4), 50)
Fraction(125, 2)
>>>

>>> from decimal import Decimal
>>> compute_cost(Decimal("1.25"), Decimal("50"))
Decimal('62.50')
>>>

>>> import numpy as np
>>> prices = np.array([1.25, 2.10, 3.05])
>>> units = np.array([50, 20, 25])
>>> compute_cost(prices, units)
array([62.5 , 42.  , 76.25])
>>>

>>> compute_cost("a lot", 10)
'a lota lota lota lota lota lota lota lota lota lot'
>>>

>>> compute_cost(Fraction(5, 4), Decimal("50"))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in compute_cost
TypeError: unsupported operand type(s) for *: 'Fraction' and 'decimal.Decimal'
>>>

与静态语言的编译器不同， Python 不会视线验证程序的正确行为。相反，对象的行为是由一个动态过程决定的，这个过程涉及所谓的特殊方法或魔法方法的分派。任何给定对象的行为完全取决于它实现的一组特殊方法。