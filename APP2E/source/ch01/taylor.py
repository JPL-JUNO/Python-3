"""
@File         : taylor.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-03 21:14:23
@Email        : cuixuanstephen@gmail.com
@Description  : 为了更好地展示 KCachegrind 的功能定义了一个递归函数阶乘，以及另外两个使用阶乘的函数
"""


def factorial(n):
    if n == 0:
        return 1.0
    else:
        return factorial(n - 1) * n


def taylor_exp(n) -> list:
    return [1.0 / factorial(i) for i in range(n)]


def taylor_sin(n) -> list:
    res = []
    for i in range(n):
        if i % 2 == 1:
            res.append((-1) ** ((i - 1) / 2) / float(factorial(i)))
        else:
            res.append(0.0)
    return res


def benchmark():
    taylor_exp(500)

    taylor_sin(500)


if __name__ == "__main__":
    benchmark()
