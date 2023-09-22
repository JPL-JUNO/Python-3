"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 21:48:25
@Description: 
"""

from itertools import product


def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=" ")
        if (i % 3) == 0:
            print()
    print()


print("Repeat 2:\n")
show(list(product(range(3), repeat=2)))

print("Repeat 3:\n")
show(list(product(range(3), repeat=3)))
