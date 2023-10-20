"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 21:17:14
@Description: 
"""

from configparser import ConfigParser

parser = ConfigParser()
candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
              'simple.ini', 'multisection.ini']
found = parser.read(candidates)
missing = set(candidates)-set(found)


print('Found config files:', sorted(found))
print('Missing files     :', sorted(missing))
