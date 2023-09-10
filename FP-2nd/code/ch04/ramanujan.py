"""
@Title: 比较简单的字符串正则表达式和字节序列正则表达式的行为
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 11:42:12
@Description: 
"""

import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r"\w+")
re_numbers_bytes = re.compile(rb"\d+")
re_words_bytes = re.compile(rb"\w+")

# 1729的泰米尔数字
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode("utf_8")

print(f"Text\n {text_str!r}")
print("Numbers")
# 字符串模式 r'\d+' 能匹配泰米尔数字和 ASCII 数字。
print("  str  :", re_numbers_str.findall(text_str))
# 字节序列模式 rb'\d+' 只能匹配 ASCII 字节中的数字。
print("  bytes  ", re_numbers_bytes.findall(text_bytes))

print("Words")
# 字符串模式 r'\w+' 能匹配字母、上标、泰米尔数字和 ASCII 数字。
print("  str  :", re_words_str.findall(text_str))
# 字节序列模式 rb'\w+' 只能匹配 ASCII 字节中的字母和数字。
print("  bytes  ", re_words_bytes.findall(text_bytes))

# 为的是说明一个问题：可以使用正则表达式搜索字符串和字节
# 序列，但是在后一种情况中，ASCII 范围外的字节不会当成数字和组成单词的字母。
