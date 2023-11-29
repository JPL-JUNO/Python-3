"""
@Title: time 的分辨率被限制为整微秒值
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 19:54:10
@Description: 
"""


import datetime
for m in [1, 0, .1, .6]:
    try:
        print('{:02.1f} :'.format(m),
              datetime.time(0, 0, 0, microsecond=m))
    except TypeError as err:
        print('Error:', err)
