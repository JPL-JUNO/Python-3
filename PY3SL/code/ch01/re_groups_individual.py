"""
@Title: 访问单个组的匹配
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 21:41:57
@Description: 
"""

import re
text = "This is some text -- with punctuation"

print("Input text            :", text)

# \b 单词开头或末尾的空串
# \w+ 匹配任意数字字母
# Word starting with 't' then another word
regex = re.compile(r"(\bt\w+)\W+(\w+)")
print("Pattern               :", regex.pattern)

match = regex.search(text)

print("Entire match          :", match.group(0))
print("Word starting with 't':", match.group(1))
print("Word after 't' word   :", match.group(2))
# 组 0 表示与整个表达式匹配的字符串，
# 子组按其左括号在表达式中出现的顺序编号
# 从 1 开始
