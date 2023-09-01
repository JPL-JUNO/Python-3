>>> s = Stock("ACME", 50, 91.1)
>>> p = Point(2, 3)
>>> c = Circle(4.5)
>>> s2 = Stock("ACME", 50)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Notes\Python-3\PC-3rd-zh\code\ch08\Simplifying the Initialization of Data Structures\example1.py", line 17, in __init__
    raise TypeError("Expected {} arguments".format(len(self._fields)))
TypeError: Expected 3 arguments