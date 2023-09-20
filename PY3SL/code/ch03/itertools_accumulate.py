"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 17:25:15
@Description: 
"""

from itertools import accumulate

print(list(accumulate(range(5))))
print(list(accumulate("abcde")))
print()

# accumulate() 可以与任何取两个输入值得函数结合来得到不同得结果


def f(a, b):
    print(a, b)
    return b + a + b


# 这种例子可以生成一系列（无意义）的回文数
print(list(accumulate("abcde", f)))
