"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 21:32:23
@Description: 
"""

import datetime

min6 = datetime.timezone(datetime.timedelta(hours=-6))

plus6 = datetime.timezone(datetime.timedelta(hours=6))

d = datetime.datetime.now(min6)
print(min6, ':', d)

# 要把一个 datetime 值从一个时区转换为另一个时区，可以使用 astimezone()
print(datetime.timezone.utc, ':',
      d.astimezone(datetime.timezone.utc))
print(plus6, ':', d.astimezone(plus6))

d_system = d.astimezone()
print(d_system.tzinfo, ':', d_system)
