"""
@File         : item21.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-20 22:35:57
@Email        : cuixuanstephen@gmail.com
@Description  : 了解如何在闭包里面使用外层作用域中的元素
"""

from typing import Any


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


def sort_priority2(numbers, group):
    found = False  # Scope: 'sort_priority2'

    def helper(x):
        if x in group:
            found = True  # Scope: 'helper' -- Bad!
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


found = sort_priority2(numbers, group)
assert not found
print(numbers)


def sort_priority3(numbers, group):
    found = False

    def helper(x):
        nonlocal found  # Added
        if x in group:
            found = True
            return (0, x)
        return (1, x)

    numbers.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group) -> None:
        self.group = group
        self.found = False

    def __call__(self, x) -> Any:
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
# 有个问题，找到一次之后，就一直是 True
# 对不同的 numbers，每次都需要实例 Sorter
assert sorter.found is True
