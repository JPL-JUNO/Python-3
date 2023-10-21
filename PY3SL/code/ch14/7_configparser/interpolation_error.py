"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 15:19:10
@Description: 
"""
import configparser
parser = configparser.ConfigParser()
parser.add_section('bug_tracker')

parser.set('bug_tracker', 'url',
           'http://%(server)s:%(port)s/bugs')

try:
    print(parser.get('bug_tracker', 'url'))
    # 缺少 Option 来做替换
except configparser.InterpolationMissingOptionError as err:
    print('ERROR:', err)
