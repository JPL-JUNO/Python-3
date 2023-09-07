"""
@Title: 迭代所有可能的组合或排列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 10:16:01
@Description: 
"""
items = ['A', 'B', "C"]
from itertools import permutations
for p in permutations(items):
    print(p)
# ('A', 'B', 'C')
# ('A', 'C', 'B')
# ('B', 'A', 'C')
# ('B', 'C', 'A')
# ('C', 'A', 'B')
# ('C', 'B', 'A')

for p in permutations(items, 2):
    print(p)
# ('A', 'B')
# ('A', 'C')
# ('B', 'A')
# ('B', 'C')
# ('C', 'A')
# ('C', 'B')

from itertools import combinations
for c in combinations(items, 3):
    print(c)
# ('A', 'B', 'C')

for c in combinations(items, 2):
    print(c)
# ('A', 'B')
# ('A', 'C')
# ('B', 'C')


from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)
# ('A', 'A', 'A')
# ('A', 'A', 'B')
# ('A', 'A', 'C')
# ('A', 'B', 'B')
# ('A', 'B', 'C')
# ('A', 'C', 'C')
# ('B', 'B', 'B')
# ('B', 'B', 'C')
# ('B', 'C', 'C')
# ('C', 'C', 'C')
