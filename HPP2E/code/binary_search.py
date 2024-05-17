"""
@File         : binary_search.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-01 21:20:54
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import timeit


def binary_search(needle, haystack):
    i_min, i_max = 0, len(haystack)
    while True:
        if i_min >= i_max:
            return -1
        mid_point = (i_min + i_max) // 2
        if haystack[mid_point] > needle:
            i_max = mid_point
        elif haystack[mid_point] < needle:
            i_min = mid_point + 1
        else:
            return mid_point


if __name__ == "__main__":
    setup = "from __main__ import (binary_search, haystack, needle)"
    iterations = 10_000

    for haystack_size in (10_000, 100_000, 1_000_000):
        haystack = range(haystack_size)
        for needle in (1, 6_000, 9_000, 1_000_000):
            index = binary_search(needle, haystack)
            t = timeit.timeit(
                stmt="binary_search(needle, haystack)", setup=setup, number=iterations
            )
            print(
                f"Value {needle:<8} found in haystack of "
                f"size {len(haystack):<8} at index "
                f"{index:<8} in {t/iterations:.5e} seconds"
            )
