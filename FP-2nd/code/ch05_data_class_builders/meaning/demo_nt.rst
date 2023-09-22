>>> from demo_nt import DemoNTClass
>>> DemoNTClass.__annotations__
{'a': <class 'int'>, 'b': <class 'float'>}
>>> DemoNTClass.a
_tuplegetter(0, 'Alias for field number 0')
>>> DemoNTClass.b
_tuplegetter(1, 'Alias for field number 1')
>>> DemoNTClass.c
'spam'
>>> DemoNTClass.__doc__
'DemoNTClass(a, b)'
>>> nt = DemoNTClass(8)
>>> nt.a
8
>>> nt.b
1.1
>>> nt.c
'spam'
>>>