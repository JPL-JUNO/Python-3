"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 20:48:21
@Description: 
"""

import datetime

today = datetime.date.today()
print('Today     :', today)

one_day = datetime.timedelta(days=1)
print('One Day   :', one_day)

yesterday = today - one_day
print('Yesterday :', yesterday)

tomorrow = today + one_day
print('Tomorrow  :', tomorrow)

print()

print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)
