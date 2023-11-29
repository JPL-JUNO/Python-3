"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 21:00:57
@Description: 
"""

import datetime
import time

print('Times:')
t1 = datetime.time(12, 55, 0)
print('t1:', t1)

t2 = datetime.time(13, 5, 0)
print('t2:', t2)
print('t1 < t2:', t1 < t2)

print('Dates:')
d1 = datetime.date.today()
print('d1:', d1)
d2 = d1 + datetime.timedelta(days=1)
print('d2:', d2)
print('d1 > d2:', d1 > d2)
