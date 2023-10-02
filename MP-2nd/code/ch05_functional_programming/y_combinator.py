"""
@Title: Y combinator
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-22 19:11:40
@Description: 建议先跳过，是个复杂的递归问题
"""

# Y= lambda f: lambda *args: f(Y(f))(*args)


def Y(f): return lambda *args: f(Y(f))(*args)


def Y(f):
    def y(*args):
        y_functions = f(Y(f))
        return y_functions(*args)
    return y


def factorial(combinator):
    def _factorial(n):
        if n:
            return n * combinator(n - 1)
        else:
            return 1
    return _factorial


assert Y(factorial)(5) == 120
assert Y(lambda c: lambda n: n and n * c(n - 1) or 1)(5) == 120
assert Y(lambda c: lambda n: n * c(n - 1) if n else 1)(5) == 120

quicksort = Y(lambda f:
              lambda x: (
                  f([item for item in x if item < x[0]])
                  + [y for y in x if x[0] == y]
                  + f([item for item in x if item > x[0]])
              ) if x else [])
quicksort([1, 3, 5, 4, 1, 3, 2])
