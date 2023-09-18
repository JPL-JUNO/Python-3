"""
@Title: 无穷数列的迭代器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 11:23:18
@Description: 
"""


def fibonacci():
    """
    这没有指定迭代的数量，我们可以进行任意次的迭代
    """
    i, j = 0, 1
    while True:
        yield j
        i, j = j, i + j


# 生成器并没有想象中使用的那么广泛的一个原因
# 是它们的逻辑可以被包含在你的代码中。
# 在代码内部使用生成器，而不是说单独拎出来使用
def fibonacci_naive():
    i, j = 0, 1
    count = 0
    while j <= 5000:
        if j % 2:
            count += 1
        i, j = j, i + j
    return count


def fibonacci_transform():
    """
    这个函数的好处在于不需要计算 fibonacci 序列，
    而且可以任意长度，
    展示了两个阶段的处理：生成数据和转换数据
    """
    count = 0
    for f in fibonacci():
        if f > 5_000:
            break
        if f % 2 == 0:
            count += 1
    return count


from itertools import takewhile


def fibonacci_succinct():
    first_5_000 = takewhile(lambda x: x < 5_000,
                            fibonacci())
    return sum(1 for x in first_5_000 if x % 2)
