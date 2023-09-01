"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 16:19:33
@Description: ChainMap 与带有作用域的值，比如编程语言中的变量（即全局变量、局部变量等）一起工作时特别有用。
"""

from collections import ChainMap
values = ChainMap()
values['x'] = 1

# Add a new mapping
values = values.new_child()
values['x'] = 2

# Add a new mapping
values = values.new_child()
values['x'] = 3

assert values['x'] == 3

values = values.parents
assert values['x'] == 2

values = values.parents
assert values['x'] == 1

# 作为 ChainMap 的替代方案，我们可能会考虑利用字典的 update()方法将多个字典合并在一起。
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
