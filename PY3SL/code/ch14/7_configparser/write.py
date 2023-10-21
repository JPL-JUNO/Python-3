"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 11:34:28
@Description: 
"""

import configparser
import sys
parser = configparser.ConfigParser()
parser.add_section('bug_tracker')
parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
parser.set('bug_tracker', 'username', 'stephen')
parser.set('bug_tracker', 'password', 'secret')


parser.write(sys.stdout)
