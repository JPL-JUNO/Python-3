"""
@Description: dict - A map of items
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-27 22:36:58
"""


def most_significant(value: int) -> int:
    while value >= 10:
        value //= 10
    return value


print(most_significant(12345))
print(most_significant(98))
print(most_significant(0))


def add(collection, key, value):
    index = most_significant(key)
    collection[index].append((key, value))


def contains(collection, key) -> bool:
    index = most_significant(key)
    for k, _ in collection[index]:
        if k == key:
            return True
    return False


# This code is obviously not identical to the dict implementation,
# but it is similar. Since we can just get item 1 for a value of 123 by simple indexing,
# we have only O(1) lookup costs in the general case.
# However, since both keys, 123 and 101, are within the 1 bucket,
# the runtime can actually increase to O(n) in the worst case,
# where all keys have the same hash.
collection = [[], [], [], [], [], [], [], [], [], []]
add(collection, 123, 'a')
add(collection, 456, 'b')
add(collection, 789, 'c')
add(collection, 101, 'c')
print(collection)
print(contains(collection, 123))
print(contains(collection, 1))
