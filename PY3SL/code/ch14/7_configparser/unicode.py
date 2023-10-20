"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 21:23:35
@Description: 
"""

from configparser import ConfigParser
import codecs

parser = ConfigParser()

parser.read('unicode.ini', encoding='utf-8')
password = parser.get('bug_tracker', 'password')

print('Password:', password.encode('utf-8'))
print('Type    :', type(password))
print('repr()  :', repr(password))
