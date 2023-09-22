"""
@Title: 实现迭代协议
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 19:22:27
@Description: 
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        # 首先产生出自身
        yield self
        # 迭代每个子节点，子节点在重复这个操作

        for c in self:
            yield from c.depth_first()


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)

    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)
