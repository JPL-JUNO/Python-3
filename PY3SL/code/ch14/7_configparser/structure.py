"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 21:42:34
@Description: 
"""

from configparser import ConfigParser

parser = ConfigParser()
parser.read('multisection.ini')

for section_name in parser.sections():
    print('Section:', section_name)
    print('  Options:', parser.options(section=section_name))
    for name, value in parser.items(section=section_name):
        print('  {} = {}'.format(name, value))
    print()
