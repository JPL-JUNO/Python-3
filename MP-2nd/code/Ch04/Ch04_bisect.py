"""
@Description: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-22 22:56:28
"""

import bisect

sorted_list = []
sorted_list.append(5)  # O(1)
sorted_list.append(3)  # O(1)
sorted_list.append(1)  # O(1)
sorted_list.append(2)  # O(1)

sorted_list.sort()  # O(n*log(n))
print(sorted_list)


sorted_list = []
bisect.insort(sorted_list, 5)  # O(n) = 1
bisect.insort(sorted_list, 3)  # O(n) = 2
bisect.insort(sorted_list, 1)  # O(n) = 3
bisect.insort(sorted_list, 2)  # O(n) = 4
print(sorted_list)
# if we insert 1000, it would be 1000 + 1000 * log(1000) = 10966 versus (1+2+...+1000)=500500
# 排序的话普通的列表复杂度更低

sorted_list = [1, 2, 5]


def contains(sorted_list, value):
    for item in sorted_list:
        if item > value:
            break
        elif item == value:
            return True
    return False


assert contains(sorted_list, 2)
assert not contains(sorted_list, 4)
assert not contains(sorted_list, 6)

sorted_list = [1, 2, 5]


def contains(sorted_list, value):
    # 没找到的返回 False
    i = bisect.bisect_left(sorted_list, value)
    return i < len(sorted_list) and sorted_list[i] == value


# bisect does a binary search internally
assert contains(sorted_list, 2)  # O(log(n)) = 1, found it after the first step
assert not contains(sorted_list, 4)  # O(log(n)) = 1, no result after 2 steps
assert not contains(sorted_list, 6)  # O(log(n)) = 1, no result after 2 steps
# print(contains(sorted_list, 10))


# While very fast and efficient, the bisect module doesn’t feel Pythonic at all.
# fix that


class SortedList:
    def __init__(self, *values):
        self._list = sorted(values)

    def index(self, value):
        i = bisect.bisect_left(self._list, value)
        if i < len(self._list) and self._list[i] == value:
            return i

    def delete(self, value):
        del self._list[self.index(value)]

    def add(self, value):
        bisect.insort(self._list, value)

    def __iter__(self):
        for value in self._list:
            yield value

    def __exists__(self, value):
        return self.index(value) is not None


sorted_list = SortedList(1, 3, 6, 2)

assert 3 in sorted_list
assert 5 not in sorted_list

sorted_list.add(5)
assert 5 in sorted_list

print(list(sorted_list))
