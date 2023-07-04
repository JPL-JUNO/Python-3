"""
@Description: collections.ChainMap
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-04 13:22:10
"""

d1 = dict(a=1, b=2)
d2 = dict(a=2, b=4, c=6)
from collections import ChainMap
# ChainMap不复制输入映射，只存放映射的引用
chain = ChainMap(d1, d2)
assert chain['a'] == 1
assert chain['c'] == 6

chain['c'] = -1
print(d1)
print(d2)

import builtins
# 可用于是新支持嵌套作用域的语言解释器
# 模仿Python查找变量的基本规则
py_lookup = ChainMap(locals(), globals(), vars(builtins))
