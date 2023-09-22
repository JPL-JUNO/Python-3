"""
@Description: stdout check
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-09 13:09:39
"""

import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdout.encoding:', sys.stdout.encoding)
test_chars = [
    '\N{HORIZONTAL ELLIPSIS}',
    '\N{INFINITY}',
    '\N{CIRCLED NUMBER FORTY TWO}'
]

for char in test_chars:
    print(f'Trying to output {name(char)}')
    print(char)
