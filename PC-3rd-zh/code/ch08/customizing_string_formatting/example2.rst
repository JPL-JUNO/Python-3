>>> from datetime import date
>>> d = date(2023, 8, 31)
>>> format(d)
'2023-08-31'
>>> format(d, "%A, %B, %d, %Y")
'Thursday, August, 31, 2023'
>>> "The end is {:%d %b %Y}. Goodbye".format(d)
'The end is 31 Aug 2023. Goodbye'