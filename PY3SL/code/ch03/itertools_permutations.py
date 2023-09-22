"""
@Title: permutations
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 21:52:10
@Description: 
"""
from itertools import permutations


def show(iterable) -> None:
    first = None
    for _, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print("".join(item), end=" ")
    print()


print("All permutations:\n")
show(permutations("abcd"))

print("\nPairs:\n")
show(permutations("abcd", r=2))
