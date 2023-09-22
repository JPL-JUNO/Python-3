"""
@Title: 对迭代器的实现
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 19:38:20
@Description: 
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self) -> str:
        return "Node({!r})".format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator:
    def __init__(self, start_node) -> None:
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # return myself if just started;
        # create an iterator for children
        if self._child_iter is None:
            self._child_iter = iter(self._node)
            return self._node
        # if processing a child, return its next item
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)
        # advance to the next child and start its iteration
        else:
            self._child_iter = next(self._child_iter).depth_first()
            return next(self)
