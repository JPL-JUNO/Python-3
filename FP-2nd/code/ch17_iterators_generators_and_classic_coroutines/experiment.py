"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-11 22:00:36
@Description: 降低浮点数累加效应致错的风险
"""

print(100*1.1)
print(sum(1.1 for _ in range(100)))

print(10000*1.1)
print(sum(1.1 for _ in range(10000)))
