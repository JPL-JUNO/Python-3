"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 21:08:08
@Description: 
"""

import datetime

t = datetime.time(1, 2, 3)
print('t :', t)
d = datetime.date.today()
print('d :', d)

dt = datetime.datetime.combine(d, t)
print('dt:', dt)
