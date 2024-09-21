"""
@File         : divide_by_2.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 11:00:49
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

# 除以 2”算法假设待处理的整数大于 0。它用一个简单的循环不停地将十进制数除以 2，并
# 且记录余数。第一次除以 2 的结果能够用于区分偶数和奇数。如果是偶数，则余数为 0，因此个
# 位上的数字为 0；如果是奇数，则余数为 1，因此个位上的数字为 1。可以将要构建的二进制数
# 看成一系列数字；计算出的第一个余数是最后一位。
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from sources.list03_01 import Stack


def divide_by_2(dec_number):
    rem_stack = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)

        dec_number = dec_number // 2

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())

    return bin_string


print(divide_by_2(42))
