"""
@Title: 同时迭代多个序列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 10:33:34
@Description: 
"""

x_pts = [1, 5, 4, 2, 10, 7]
y_pts = [101, 78, 37, 15, 62, 99]
for x, y in zip(x_pts, y_pts):
    print(x, y)
# 1 101
# 5 78
# 4 37
# 2 15
# 10 62
# 7 99
