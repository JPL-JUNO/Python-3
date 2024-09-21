"""
@File         : List03_01.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-19 23:00:22
@Email        : cuixuanstephen@gmail.com
@Description  : 用 Python 实现栈
"""


class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # 空栈怎么办？
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(4)
    s.push("dog")
    assert s.peek() == "dog"
    s.push(True)
    assert s.size() == 3
    assert not s.is_empty()

    s.push(8.4)
    assert s.pop() == 8.4
    assert s.pop() == True
    assert s.size() == 2
