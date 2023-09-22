>>> a = Person("Stephen")
>>> a.first_name        # calls the getter
'Stephen'
>>> a.first_name = 42   # calls the setter
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Creating Managed Attributes\example1.py", line 27, in first_name
    raise TypeError("Expected a string")
TypeError: Expected a string


.. property 属性实际上就是把一系列的方法绑定到一起。如果检查类的 property 属性，就
.. 会发现 property 自身所持有的属性 fget、fset 和 fdel 所代表的原始方法。
>>> Person.first_name.fget
<function Person.first_name at 0x0000013E787B7240>
>>> Person.first_name.fset
<function Person.first_name at 0x0000013E787B72E0>
>>> Person.first_name.fdel
<function Person.first_name at 0x0000013E787B7380>