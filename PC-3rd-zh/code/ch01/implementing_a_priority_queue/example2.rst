>>> a = Item("foo")
>>> b = Item("bar")
>>> a < b
Traceback (most recent call last):
TypeError: '<' not supported between instances of 'Item' and 'Item'

>>> a = (1, Item("foo"))
>>> b = (5, Item("bar"))
>>> a < b
True
>>> c = (1, Item("grok"))
>>> a < c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'Item' and 'Item'