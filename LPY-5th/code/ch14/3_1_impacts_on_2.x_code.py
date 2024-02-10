"""
@File         : 3_1_impacts_on_2.x_code.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 22:35:15
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

zip("abc", "xyz")

list(zip("abc", "xyz"))

M = map(lambda x: 2**x, range(3))
for i in M:
    print(i)

for i in M:
    # 没有任何东西，迭代支持单遍
    print(i)  # Unlike 2.X lists, one pass only (zip too)
