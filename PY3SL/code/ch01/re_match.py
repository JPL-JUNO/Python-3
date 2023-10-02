"""
@Title: 限制搜索
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 20:46:53
@Description: 
"""
# 如果模式必须出现在输入开头
# 那么使用 match() 而不是 search() 会锚定搜索，而不必显式地在搜索模式中包含一个锚

import re

text = "This is some text -- with punctuation"
pattern = "is"

print("Text   :", text)
print("Pattern:", pattern)

# 因为 is 不在开头，因此 match() 没有匹配到
m = re.match(pattern, text)
print("Match  :", m)

s = re.search(pattern, text)
print("Search :", s)
