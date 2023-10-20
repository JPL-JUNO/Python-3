"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 21:12:19
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('simple.ini')

print(parser.get('bug_tracker', 'url'))
