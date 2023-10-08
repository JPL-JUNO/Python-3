"""
@Title: 时间组成
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 22:45:21
@Description: 有些情况下，程序需要访问一个日期的各个字段（例如，年和月）
"""

import time


def show_struct(s):
    print('tm_year :', s.tm_year)
    print('tm_mon  :', s.tm_mon)
    print('tm_mday :', s.tm_mday)
    print('tm_hour :', s.tm_hour)
    print('tm_min  :', s.tm_min)
    print('tm_sec  :', s.tm_sec)
    print('tm_wday :', s.tm_wday)
    print('tm_yday :', s.tm_yday)
    print('tm_isdst:', s.tm_isdst)


print('gmtime(以 UTC 格式返回当前时间):')
show_struct(time.gmtime())

print('\nlocal time(当前时区的当前时间):')
show_struct(time.localtime())

print('\nmktime(取一个 struct_time 实例，将它转换为浮点数表示):', time.mktime(time.localtime()))
