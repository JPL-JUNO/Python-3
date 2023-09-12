"""
@Title: 查找文本中的模式
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 23:21:16
@Description: 
"""

# search 函数取模式和扫描的文本作为输入，找到这个模式时，就返回一个 Match 对象
# 如果没有找到模式，search() 就返回 None
# 每个 Match 对象包含有关匹配性质的信息，包括原输入字符串、所使用的正则表达式以及模式在源字符串中出现的位置

import re

pattern = "this"
text = "Does this text match the pattern?"

match = re.search(pattern, text)

# 提供字符串中的相应索引，指示与模式匹配的文本在字符串中出现的位置
s = match.start()
e = match.end()

print("Found '{}'\nin '{}'\nfrom {} to {} ('{}')".format(
    match.re.pattern, match.string, s, e, text[s:e]
))
