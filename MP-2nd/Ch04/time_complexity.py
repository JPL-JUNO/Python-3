"""
@Description: Time Complexity
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-27 14:10:55
"""

n = 1_000
a = list(range(n))
b = dict.fromkeys(range(n))

for i in range(100):
    assert i in a  # takes n=1000 steps
    assert i in b  # takes 1 step


def o_one(items):
    return 1  # 1 operation so O(1)


def o_n(items):
    total = 0
    # walks through all item once as O(n)
    for item in items:
        total += item
    return total


def o_n_squared(items):
    total = 0
    # warks through all items n*n times so O(n**2)
    for a in items:
        for b in items:
            total += a * b
    return total


n = 10
items = range(n)
print(o_one(items))
print(o_n(items))
print(o_n_squared(items))
