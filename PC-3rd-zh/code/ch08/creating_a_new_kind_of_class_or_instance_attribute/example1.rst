>>> p = Point(2, 3)
>>> p.x
>>> p.y = 5
>>> p.x = 2.3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Creating a New Kind of Class or Instance Attribute\example1.py", line 24, in __set__
    raise TypeError("Expected an integer")
TypeError: Expected an integer