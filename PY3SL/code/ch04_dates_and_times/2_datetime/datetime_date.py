"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 19:58:10
@Description: 
"""

import datetime

today = datetime.date.today()
print(today)
print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year   =', tt.tm_year)
print('         tm_mon    =', tt.tm_mon)
print('         tm_mday   =', tt.tm_mday)
print('         tm_hour   =', tt.tm_hour)
print('         tm_minute =', tt.tm_min)
print('         tm_second =', tt.tm_sec)
print('         tm_wday   =', tt.tm_wday)
print('         tm_yday   =', tt.tm_yday)
print('         tm_isdst  =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)
