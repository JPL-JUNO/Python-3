"""
@File         : 2 3 Extended List Comprehension Syntax.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 19:39:41
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
import sys
import os

sys.path.append(os.path.dirname("../"))
from funcs import info

info("筛选分句：if")
lines = [line.rstrip() for line in open("./script2.py") if line.startswith("p")]
print(lines)

info("等价形式")
res = []
for line in open("./script2.py"):
    if line.startswith("p"):
        res.append(line.rstrip())
print(res)

# 为啥要写 -1:？
# 否则遇见空行将导致 IndexError
# 但是 -1: 超过范围则显示在范围之内的内容
[line.rstrip() for line in open("./script2.py") if line.rstrip()[-1:].isdigit()]

info("嵌套循环：for")
[x + y for x in "abc" for y in "lmn"]
res = []
for x in "abc":
    for y in "lmn":
        res.append(x + y)
print(res)
