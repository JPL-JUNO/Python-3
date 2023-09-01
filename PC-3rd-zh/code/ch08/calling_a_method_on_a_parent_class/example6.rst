>>> a.spam()
A.spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Calling a Method on a Parent Class\example6.py", line 13, in spam
    super().spam()
    ^^^^^^^^^^^^
AttributeError: 'super' object has no attribute 'spam'
>>> c = C()
>>> c.spam()
A.spam
B.spam