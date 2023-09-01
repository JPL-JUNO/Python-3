"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 10:30:36
@Description: 
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 队列以元组(-priority, index, item)的形式组成。把 priority 取负值是为了
        # 让队列能够按元素的优先级从高到低的顺序排列。这和正常的堆排列顺序相反，一般
        # 情况下堆是按从小到大的顺序排序的。
        # 变量 index 的作用是为了将具有相同优先级的元素以适当的顺序排列。通过维护一个不
        # 断递增的索引，元素将以它们入队列时的顺序来排列。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # heappop()方法总是返回“最小”的元素
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return "Item({!r})".format(self.name)
