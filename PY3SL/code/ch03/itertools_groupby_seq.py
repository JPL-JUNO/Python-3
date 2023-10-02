"""
@Title: 分组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 17:03:40
@Description: 
"""

import functools
from itertools import groupby, count, cycle, islice
import operator
import pprint


@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    # 要实现比较功能

    def __gt__(self, other):
        return (self.x, self.y) >= (other.x, other.y)


# Create a data set of Point instances
data = list(map(Point,
                cycle(islice(count(), 3)),
                islice(count(), 7)))
print("Data:")
pprint.pprint(data, width=35)
print()

print("Grouped, unsorted:")
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
print()

# sort the data
data.sort()
print("Sorted:")
pprint.pprint(data, width=35)
print()

print("Grouped, sorted:")
for k, g in groupby(data, operator.attrgetter('x')):
    print(k, list(g))
# 输入的序列要根据键值排序，以保证得到预期的分组
