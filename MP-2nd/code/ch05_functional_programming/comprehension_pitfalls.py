"""
@Description: Comprehension pitfalls
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 09:26:33
"""

import random
# This happens because the first and the last random
# calls are actually separate calls and return different results.
rand_nums = [random.random() for _ in range(10) if random.random() > .5]
print(rand_nums)
# One way to counter is:
numbers = [random.random() for _ in range(10)]
print([x for x in numbers if x > .5])

equivalent_1 = [x for x in [random.random() for _ in range(10)] if x > .5]
print(equivalent_1)
equivalent_2 = [x for _ in range(10) for x in [random.random()] if x > .5]
print(equivalent_2)

nested_list_comprehension = [(x, y) for x in range(3) for y in range(3, 5)]
print(nested_list_comprehension)
# This effectively does the following:
results = []
for x in range(3):
    for y in range(3, 5):
        results.append((x, y))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 实现转置
reshaped_matrix = [
    [
        [y for x in matrix for y in x][i * len(matrix) + j]
        for j in range(len(matrix))
    ]
    for i in range(len(matrix[0]))
]

import pprint
pprint.pprint(reshaped_matrix, width=40)
# 非常不推荐使用嵌套的 list comprehensions
