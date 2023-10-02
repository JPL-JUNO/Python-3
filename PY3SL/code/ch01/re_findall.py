"""
@Title: 多重匹配
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 09:54:38
@Description: 
"""
# findall() 函数会返回输入中与模式匹配而且不重叠的所有子串
# 列表
import re

text = "abbaaabbbaaaaa"

pattern = "ab"

for match in re.findall(pattern, text):
    print("Found {!r}".format(match))
