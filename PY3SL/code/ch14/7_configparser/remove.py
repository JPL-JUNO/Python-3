"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 11:27:10
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('multisection.ini')


def print_ini():
    for section in parser.sections():
        print(section)
        for name, value in parser.items():
            print('  {} = {!r}'.format(name, value))


print('Read values:\n')
print_ini()


parser.remove_option('bug_tracker', 'password')
parser.remove_section('wiki')

print('\nModified values:\n')
print_ini()
