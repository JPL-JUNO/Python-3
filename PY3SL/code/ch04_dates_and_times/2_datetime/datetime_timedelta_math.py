"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 20:56:42
@Description: 
"""

import datetime

one_day = datetime.timedelta(days=1)

print('1 day   :', one_day)
print('5 days  :', one_day * 5)
print('1.5 days:', one_day * 1.5)
print('1/4 days:', one_day / 4)


work_day = datetime.timedelta(hours=7)
meeting_length = datetime.timedelta(hours=1)
print('meetings per day:', work_day / meeting_length)
