"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 20:06:59
@Description: 
"""

import datetime
import time

o = 739114
print('o               :', 0)
print('fromordinal(o)  :', datetime.date.fromordinal(o))

t = time.time()

print('t               :', t)
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))
