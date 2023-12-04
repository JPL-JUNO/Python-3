"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-12-04 21:15:02
@Description: 
"""

import argparse

parser = argparse.ArgumentParser(description='Example with long option names')

parser.add_argument('--noarg', action='store_true',
                    default=False)
parser.add_argument('--witharg', action='store',
                    dest='witharg')
parser.add_argument('--witharg2', action='store', dest='witharg2', type=int)

print(parser.parse_args(
    ['--noarg', '--witharg', 'val', '--witharg2=3']
))
