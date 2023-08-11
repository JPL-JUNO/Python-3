"""
@Description: 字符的数值意义
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-11 13:58:15
"""

import unicodedata
import re

re_digit = re.compile(r'\d')
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print(f'U+{ord(char):04x}',
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          f'{unicodedata.numeric(char):5.2f}',
          unicodedata.name(char),
          sep='\t')
# 正则表达式 r'\d' 能匹配数字“1”和梵文数字 3，但是不能匹配 isdigit
# 方法判断为数字的其他字符。re 模块对 Unicode 的支持并不充分。PyPI 中有个新开发的
# regex 模块，它的最终目的是取代 re 模块，以提供更好的 Unicode 支持。
