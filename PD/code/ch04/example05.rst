>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> str(d)
'2012-12-21'
>>>

要获取更多的信息，请使用``repr(x)``函数，该函数创建一个对象表示字符串。必须在源代码中输入该函数，才能创建对象表示字符串

>>> repr(d)
'datetime.date(2012, 12, 21)'
>>> print(repr(d))
datetime.date(2012, 12, 21)
>>> print(f"The date is: {d!r}")
The date is: datetime.date(2012, 12, 21)
>>>