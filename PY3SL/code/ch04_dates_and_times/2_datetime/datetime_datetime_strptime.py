"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 21:10:31
@Description: 
"""

import datetime

format = '%a %b %d %H:%M:%S %Y'

today = datetime.datetime.today()
print('ISO', today)
s = today.strftime(format)
print('strftime:', s)

# datetime.datetime.strptime 可以将格式化字符串转为 datetime.datetime 实例
d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))
