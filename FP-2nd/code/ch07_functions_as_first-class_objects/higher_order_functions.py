"""
@Title: 高阶函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 20:44:17
@Description: 
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


def example7_3():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    # 可选的 key 参数用于提供一个函数，它会应用到各个元素上进行排序
    print(sorted(fruits, key=len))


def example7_4():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

    def reverse(word):
        return word[::-1]

    print(reverse("testing"))
    # 任何单参数函数都能作为 key 参数的值
    print(sorted(fruits, key=reverse))  # 这个结果是按照尾字母进行排序


def example7_5():
    print(list(map(factorial, range(6))))
    print([factorial(n) for n in range(6)])

    print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
    print([factorial(n) for n in range(6) if n % 2])


def example7_6():
    from functools import reduce
    from operator import add

    assert reduce(add, range(100)) == 4950
    assert sum(range(100)) == 4950
