"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 14:55:22
@Description: 
"""

from configparser import ConfigParser

parser = ConfigParser()

parser.read('interpolation.ini')
print('Original value       :', parser.get('bug_tracker', 'url'))

# 每次调用 get() 时会默认地完成拼接，通过传递 raw 参数可以获取未拼接的原值
parser.set('bug_tracker', 'port', '9090')


# 由于值由 get 计算，所以改变 url 值所用的某个设置也会改变返回值
print('Altered port value   :', parser.get('bug_tracker', 'url'))

print('without interpolation:', parser.get('bug_tracker', 'url', raw=True))
