"""
@File         : item21.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-20 22:35:57
@Email        : cuixuanstephen@gmail.com
@Description  : 了解如何在闭包里面使用外层作用域中的元素
"""


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
