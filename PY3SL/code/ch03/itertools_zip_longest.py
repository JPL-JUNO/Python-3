"""
@Title: zip_longest
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:26:38
@Description: 
"""
from itertools import zip_longest

r1 = range(3)
r2 = range(2)

print("zip stop early:")
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)
print("\nzip_longest processes all of the values:")
print(list(zip_longest(r1, r2)))

print("\nchange default fill value:")
print(list(zip_longest(r1, r2, fillvalue="mis")))
