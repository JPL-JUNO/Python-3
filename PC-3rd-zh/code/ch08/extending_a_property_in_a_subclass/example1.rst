>>> s = SubPerson("Stephen")
Setting name to Stephen
>>> s.name = "CUI"
Setting name to CUI
>>> s.name = 42
Setting name to 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Extending a Property in a Subclass\example1.py", line 38, in name
    super(SubPerson, SubPerson).name.__set__(self, value)
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Extending a Property in a Subclass\example1.py", line 21, in name
    raise TypeError("Expected a string")
TypeError: Expected a string