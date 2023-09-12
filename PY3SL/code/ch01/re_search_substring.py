"""
@Title: search() 子串
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 21:02:06
@Description: 
"""

import re
text = "This is some text -- with punctuation"

# \b 单词开头或末尾空串
pattern = re.compile(r"\b\w*is\w*\b")

print("Text:", text)
pos = 0
while True:
    # 实现了 re.iterall() 的一种不太高效的形式
    match = pattern.search(text, pos)
    if not match:
        # 如果没匹配上则直接结束循环
        break
    s = match.start()
    e = match.end()
    print('  {:>2d}: {:>2d} = "{}"'.format(
        s, e - 1, text[s:e]
    ))
    # 每找到一个匹配时，这个匹配的结束位置将用于下一个搜索
    pos = e
