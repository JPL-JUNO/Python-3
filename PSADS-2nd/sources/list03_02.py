"""
@File         : List03_02.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-20 19:29:06
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# insert(0)和 pop(0)的时间
# 复杂度都是 O(n)，元素越多就越慢。显而易见，尽管两种实现在逻辑上是相等的，但是它们在
# 进行基准测试时耗费的时间会有很大的差异。
