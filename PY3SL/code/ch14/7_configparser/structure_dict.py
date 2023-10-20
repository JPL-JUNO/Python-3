"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 21:49:02
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('multisection.ini')

for section_name in parser:
    # 会多打印一个默认的 DEFAULT 节
    print('Section:', section_name)
    section = parser[section_name]
    print('  Options:', list(section.keys()))
    for name in section:
        print('  {} = {}'.format(name, section[name]))
    print()
