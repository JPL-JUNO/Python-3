"""
@Title: 处理时区
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 22:52:41
@Description: 
"""

import time
import os


def show_zone_info():
    print('  TZ:', os.environ.get('TZ', '(not set)'))
    print('  tzname:', time.tzname)
    print('  Zone:{} {}'.format(
        time.timezone, (time.timezone / 3600)
    ))
    print('  DST', time.daylight)
    print('  Time', time.ctime())


print('Default :')
show_zone_info()
ZONES = [
    'GMT',
    'Europe/Amsterdam',
]

for zone in ZONES:
    os.environ['TZ'] = zone
    # Windows 上面不能使用该函数
    # time.tzset()
    print(zone, ':')
    show_zone_info()
