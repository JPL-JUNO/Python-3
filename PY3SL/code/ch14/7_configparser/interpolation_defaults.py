"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 15:11:41
@Description: 
"""
from configparser import ConfigParser

parser = ConfigParser()

parser.read('interpolation_defaults.ini')

# 替换会从 bug_tracker 中开始查找，如果没有找到，那么会从 DEFAULT 中查找
print('URL:', parser.get('bug_tracker', 'url'))
