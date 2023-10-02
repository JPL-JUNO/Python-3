"""
@Title: getclasstree_unique.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 14:58:57
@Description: 
"""

import inspect
import example

from getclasstree import print_class_tree, C, D

print_class_tree(inspect.getclasstree(
    [example.A, example.B, C, D],
    unique=True,
))
