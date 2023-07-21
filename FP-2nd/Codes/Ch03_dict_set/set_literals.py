"""
@Description: set 字面量
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-21 12:40:05
"""

s = {1}
print(type(s))
s.pop()
# 空集合必须使用不带参数的构造函数来创建，否则表示空字典
print(s)

# frozenset 没有字面量句法，必须调用构造函数创建
print(frozenset(range(10)))

from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

s = {1, 2, 3}
s.discard(1)
print(s)
s.discard(10)
print(s)
