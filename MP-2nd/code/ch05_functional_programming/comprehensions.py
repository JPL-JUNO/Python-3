"""
@Description: list, set, and dict comprehensions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 09:15:19
"""

# Basic list comprehensions
squares = [x ** 2 for x in range(10)]
print(squares)

odd_squares = [x ** 2 for x in range(10) if x % 2]
print(odd_squares)


def square(x):
    return x**2


def odd(x):
    return x % 2


# In particular, the version using both filter and map isn’t all that readable given
# the number of parentheses, unless you’re used to the Lisp programming language, that is.
squares = list(map(square, range(10)))
odd_squares = list(filter(odd, map(square, range(10))))


import os
directories = filter(os.path.isdir, os.listdir('.'))
# Versus
directories = [x for x in os.listdir('.') if os.path.isdir(x)]


odd_squares = []
for x in range(10):
    if x % 2:
        odd_squares.append(x ** 2)
print(odd_squares)
# set comprehensions


[x // 2 for x in range(3)]  # list comprehension
numbers = {x // 2 for x in range(3)}
print(numbers)  # dict
print(sorted(numbers))  # list

# dict comprehensions
{x: x**2 for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{x: x ** 2 for x in range(6) if x % 2}  # {1: 1, 3: 9, 5: 25}
