"""
@Title: Treating a Function Like an Object
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 20:34:11
@Description: 
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def example7_1():
    assert factorial(
        42) == 1405006117752879898543142606244511569936384000000000
    print(factorial.__doc__)
    print(type(factorial))


def example7_2():
    # 我们可以把 factorial 函数赋值给变量 fact，
    # 然后通过变量名调用。
    fact = factorial
    print(fact)
    assert fact(5) == 120
    # 还能把它作为参数传给 map 函数
    # map(factorial, range(11))
    print(list(map(factorial, range(11))))


if __name__ == '__main__':
    # Create and test a function, then read its __doc__ and check its type
    example7_1()
