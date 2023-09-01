"""
@Title: 在字典中将键映射到多个值上
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 10:46:13
@Description: 
"""

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)


d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

# ❌
pairs = [('a', 1), ('a', 2), ('b', 4)]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# ✅
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
