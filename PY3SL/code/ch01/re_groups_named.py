"""
@Title: 命名组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 21:57:03
@Description: 
"""

import re

# 要设置一个组的名字，
# 可以使用语法
# (?P<name>pattern)
text = "This is some text -- with punctuation"
print(text)
print()

patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\w+)\S*$',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\w+t)\b',
]

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('  ', match.groups())
    print('  ', match.groupdict())
    print()

# 可以使用 groupdict() 获取一个字典
# 它将组名映射为匹配的子串
