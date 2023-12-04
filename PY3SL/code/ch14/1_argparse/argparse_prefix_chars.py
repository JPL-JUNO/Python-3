"""
@Title: 选项前缀
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-12-04 21:46:52
@Description: 
"""

import argparse

parser = argparse.ArgumentParser(description='Change the option prefix characters',
                                 prefix_chars='-+/')
parser.add_argument('-a', action="store_false",
                    default=None,
                    help='Turn A off',
                    )
parser.add_argument('+a', action="store_true",
                    default=None,
                    help='Turn A on',
                    )
parser.add_argument('//noarg', '++noarg',
                    action="store_true",
                    default=False)
print(parser.parse_args())
