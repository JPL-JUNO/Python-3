"""
@File         : bisect_example.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-01 22:25:13
@Email        : cuixuanstephen@gmail.com
@Description  : 用 bisect 模块在列表中查询最接近目标的值
"""

import bisect, random


def find_closest(haystack, needle):
    # bisect.bisect_left will return the first value in the haystack
    # that is greater than the needle
    # i 可以立即为如果将该数字加入 haystack，那么它排第几
    i = bisect.bisect_left(haystack, needle)
    if i == len(haystack):
        return i - 1
    elif haystack[i] == needle:
        return i
    elif i > 0:
        j = i - 1
        # since we know the value is larger than needle (and vice versa for the
        # value at j), we don't need to use absolute values here
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i


if __name__ == "__main__":
    important_numbers = []
    for i in range(10):
        new_number = random.randint(0, 1_000)
        bisect.insort(important_numbers, new_number)
    print(important_numbers)

    closest_index = find_closest(important_numbers, -250)
    print(f"Closest value to -250: {important_numbers[closest_index]}")

    closest_index = find_closest(important_numbers, 500)
    print(f"Closest value to 500: {important_numbers[closest_index]}")

    closest_index = find_closest(important_numbers, 1100)
    print(f"Closest value to 1100: {important_numbers[closest_index]}")
