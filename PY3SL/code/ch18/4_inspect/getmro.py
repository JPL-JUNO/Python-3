"""
@Title: getmro.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 15:01:24
@Description: 
"""

import inspect
import example


class C(object):
    pass


class C_First(C, example.B):
    pass


class B_First(example.B, C):
    pass


# 展示了 MRO 的深度优先特性
print("B_First:")
for c in inspect.getmro(B_First):
    # 因为 B 派生自 A，因此 A 的解析顺序在 C 之前
    print("  {}".format(c.__name__))
print()
print("C_First:")
for c in inspect.getmro(C_First):
    print("  {}".format(c.__name__))
