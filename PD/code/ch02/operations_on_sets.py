"""
@File         : Operations on Sets.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-01 23:47:30
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

a = {"a", "b", "c"}
b = {"c", "d"}
a | b
a & b
a - b
b - a
a ^ b

a = {"x": 1, "y": 2, "z": 3}
b = {"z": 3, "w": 4, "q": 5}
a.keys() & b.keys()
