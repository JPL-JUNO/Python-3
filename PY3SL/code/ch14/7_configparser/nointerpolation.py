"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 15:45:49
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser(interpolation=None)

parser.read('interpolation.ini')

print('Without interpolation:', parser.get('bug_tracker', 'url'))
