"""
@File         : Other Built-in Type Iterables.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 18:44:40
@Email        : cuixuanstephen@gmail.com
@Description  : 其他内置的迭代类型
"""
import sys
import os

sys.path.append(os.path.dirname("../"))
from funcs import info

D = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for key in D.keys():
    print(key, D[key])

I = iter(D)
assert next(I) == "a"
assert next(I) == "b"
assert next(I) == "c"
try:
    next(I)
except StopIteration:
    info("迭代结束")

for key in D:
    print(key, D[key])

P = os.popen("dir")
P.__next__()
P.__next__()
try:
    next(P)
except TypeError as e:
    print(e)

R = range(5)
print(R)

I = iter(R)
assert next(I) == 0
assert next(I) == 1

list(range(5))


E = enumerate("spam")
I = iter(E)
assert next(I) == (0, "s")
assert next(I) == (1, "p")

list(enumerate("spam"))
