"""
@Title: 将多个映射合并为单个映射
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 16:13:39
@Description: 
"""

a = {'x': 1, 'y': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)

assert c['x'] == 1
assert c['y'] == 3
assert c['z'] == 4

assert len(c) == 3
list(c.keys())
list(c.values())

c["z"] = 10
c['w'] = 40
del c['x']
print(a)
# KeyError
# del c['y']
