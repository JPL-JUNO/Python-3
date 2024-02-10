"""
@File         : 2 List Comprehensions A First Detailed Look.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 19:07:21
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10

print(L)

L = [x + 10 for x in L]
print(L)
