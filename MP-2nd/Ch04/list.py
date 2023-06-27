"""
@Description: list - a mutable list of items
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-27 22:17:46
"""


def remove(items, value):
    new_items = []
    found = False
    for item in items:
        # skip the first item which is equal to value
        if not found and item == value:
            found = True
            continue
        new_items.append(item)
    if not found:
        raise ValueError('list.remove(x): x not in list')
    return new_items


def insert(items, index, value):
    new_items = []
    for i, item in enumerate(items):
        if i == index:
            new_items.append(value)
        new_items.append(item)
    return new_items


items = list(range(10))
print(items)

items = remove(items, 5)
print(items)

items = insert(items, 2, 5)
print(items)


primes = set((1, 2, 3, 5, 7))
items = list(range(10))
for prime in primes:
    items.remove(prime)
print(items)

items = list(range(10))
print([item for item in items if item not in primes])

items = list(range(10))
list(filter(lambda item: item not in primes, items))


def in_(items, value):
    for item in items:
        if item == value:
            return True
    return False


def min_(items):
    current_min = items[0]
    for item in items[1:]:
        if current_min > item:
            current_min = item
    return current_min


def max_(items):
    current_max = items[0]
    for item in items[1:]:
        if current_max < item:
            current_max = item
    return current_max


items = range(5)
print(in_(items, 3))
print(max_(items))
print(min_(items))
