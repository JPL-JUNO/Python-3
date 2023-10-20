"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 23:25:42
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('multiline.ini')

print(parser.get('example', 'message'))
