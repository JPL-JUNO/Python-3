"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 20:59:12
@Description: 
"""
import re
text = 'This is some text -- with punctuation.'
pattern = 'is'
print('Text       :', text)
print('Pattern    :', pattern)
# re.search() 仅返回第一个
m = re.search(pattern, text)
print('Search     :', m)

s = re.fullmatch(pattern, text)
print("Full match :", s)
