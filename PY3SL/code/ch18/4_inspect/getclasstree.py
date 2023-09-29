"""
@Title: 类层级体系
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 14:52:55
@Description: 
"""

import inspect
import example


class C(example.B):
    pass


class D(C, example.A):
    pass


def print_class_tree(tree, indent=1):
    if isinstance(tree, list):
        for node in tree:
            print_class_tree(node, indent=indent + 1)
    else:
        print("  " * indent, tree[0].__name__)
    return None


if __name__ == "__main__":
    print("A, B, C, D:")
    print_class_tree(inspect.getclasstree(
        [example.A, example.B, C, D]
    ))
