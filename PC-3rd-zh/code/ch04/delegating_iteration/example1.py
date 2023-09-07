"""
@Title: 委托迭代
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 17:31:18
@Description: 
"""


class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        # __iter__()方法只是简单地将迭代请求转发给对象内部持有的 _children 属性上。
        # _children 是列表，内置的类型，满足迭代协议的
        return iter(self._children)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)
    for ch in root._children:
        print(ch)
    # Node(1)
    # Node(2)
