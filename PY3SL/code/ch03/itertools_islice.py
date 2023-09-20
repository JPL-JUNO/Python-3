"""
@Title: islice
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:31:47
@Description: 
"""
from itertools import islice
print("stop at 5:")
for i in islice(range(100), 5):
    print(i, end=" ")
print('\n')

print("Start at 5, Stop at 10:")
for i in islice(range(100), 5, 10):
    print(i, end=" ")
print('\n')


print("By tens to 100:")
for i in islice(range(100), 0, 100, 10):
    print(i, end=" ")
print('\n')
