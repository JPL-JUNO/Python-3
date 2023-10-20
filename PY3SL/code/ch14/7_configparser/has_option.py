"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 22:15:01
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('multisection.ini')

SECTIONS = ['wiki', 'none']
OPTIONS = ['username', 'password', 'url', 'description']

for section in SECTIONS:
    has_section = parser.has_section(section)
    print('{} section exists: {}'.format(section, has_section))

    for candidate in OPTIONS:
        has_option = parser.has_option(section, candidate)
        print('{}.{:12}  : {}'.format(section, candidate, has_option))
    print()
