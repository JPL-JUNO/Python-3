"""
@Title: 让字典保持有序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 11:02:25
@Description: 
"""
from collections import OrderedDict
d = OrderedDict()
d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key in d:
    print(key, d[key])

import json
json.dumps(d)
