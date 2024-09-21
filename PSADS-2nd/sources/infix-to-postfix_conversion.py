"""
@File         : infix-to-postfix_conversion.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 13:49:55
@Email        : cuixuanstephen@gmail.com
@Description  : 从中序到后序的通用转换法
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from sources.list03_01 import Stack


def infix_2_postfix(infix_expr: str):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    op_stack = Stack()
    postfix_lst = []
    token_lst = infix_expr.split()

    for token in token_lst:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            # 如果标记是操作数，将其添加到结果列表的末尾。
            postfix_lst.append(token)
        elif token == "(":
            # 如果标记是左括号，将其压入 opstack 栈中。
            op_stack.push(token)
        elif token == ")":
            # 如果标记是右括号，反复从 opstack 栈中移除元素，直到移除对应的左括号。将从栈中
            # 取出的每一个运算符都添加到结果列表的末尾。
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_lst.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] > prec[token]):
                # 如果标记是运算符，将其压入 opstack 栈中。但是，在这之前，需要先从栈中取出优先
                # 级更高或相同的运算符，并将它们添加到结果列表的末尾。
                postfix_lst.append(op_stack.pop())

            op_stack.push(token)

    while not op_stack.is_empty():
        # 将其中所有残留的运算符全部添加到结果列
        # 表的末尾。
        postfix_lst.append(op_stack.pop())

    return "".join(postfix_lst)


print(infix_2_postfix("A * B + C * D"))
print(infix_2_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
