"""
@File         : 3_3_the_map_zip_and_filter_iterables.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-25 20:27:02
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

M = map(abs, (-1, 0, 1))
print(M)

assert next(M) == 1
assert next(M) == 0
assert next(M) == 1
try:
    next(M)
except StopIteration:
    pass

for x in M:
    print(x)

M = map(abs, (-1, 0, 1))
for x in M:
    print(x)

list(map(abs, (-1, 0, 1)))

Z = zip((1, 2, 3), (10, 20, 30))
print(Z)
list(Z)
for pair in Z:
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))
for pair in Z:
    print(pair)

filter(bool, ["spam", "", "ni"])
list(filter(bool, ["spam", "", "ni"]))
# 等价于
[x for x in ["spam", "", "ni"] if bool(x)]
[x for x in ["spam", "", "ni"] if x]
