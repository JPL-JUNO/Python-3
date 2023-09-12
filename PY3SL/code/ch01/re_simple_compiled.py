"""
@Title: 编译表达式
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 09:48:17
@Description: 
"""

import re
# 直接使用已编译表达式可以避免与缓存查找相关的开销
# 通过在加载模块时预编译所有表达式，可以把编译工作转移到医用开始时
# 而不是当程序响应一个用户动作时才编译
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = "Does this text match the pattern?"
print("Text: {!r}\n".format(text))

for regex in regexes:
    print("Seeking '{}' ->".format(regex.pattern),
          end=' ')
    if regex.search(text):
        print("match!")
    else:
        print("no match!")
