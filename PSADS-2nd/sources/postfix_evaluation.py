"""
@File         : postfix_evaluation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 15:24:38
@Email        : cuixuanstephen@gmail.com
@Description  : 计算后序表达式
"""

# 如果标记是操作数，将其转换成整数并且压入 operandStack 栈中。

# 如果标记是运算符，从 operandStack 栈中取出两个操作数。第一次取出右操作数，第
# 二次取出左操作数。进行相应的算术运算，然后将运算结果压入 operandStack 栈中。
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from sources.list03_01 import Stack


def postfix_eval(postfix_expr: str):
    operand_stack = Stack()

    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            result = do_math(token, operand1, operand2)
            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfix_eval("7 8 + 3 2 + /"))
