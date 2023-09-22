>>> d = Date(2023, 8, 31)
>>> format(d)
'2023-8-31'
>>> format(d, 'mdy')
'8/31/2023'
>>> "The date is {:ymd}".format(d)
'The date is 2023-8-31'
>>> "The date is {:mdy}".format(d)
'The date is 8/31/2023'