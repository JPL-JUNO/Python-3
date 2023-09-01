>>> c = Circle(4.0)
>>> # Get instance variables
>>> vars(c)
{'radius': 4.0}
>>> # Compute area and observe variables afterward
>>> c.area
Computing area
50.26548245743669
>>> vars(c)
{'radius': 4.0, 'area': 50.26548245743669}

>>> # Notice access doesn't invoke property anymore
>>> c.area
50.26548245743669
>>> del c.area
>>> vars(c)
{'radius': 4.0}

.. 该技术有一个潜在的缺点，即，计算出的值在创建之后就变成可变的（mutable）了。

>>> c.area
Computing area
50.26548245743669
>>> c.area = 25
>>> c.area
25