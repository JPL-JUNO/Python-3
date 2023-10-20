"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-20 22:01:17
@Description: 
"""

from configparser import ConfigParser
parser = ConfigParser()
parser.read('multisection.ini')

for candidate in ['wiki', 'bug_tracker', 'dvcs',]:
    print('{:<12}: {}'.format(candidate, parser.has_section(candidate)))
