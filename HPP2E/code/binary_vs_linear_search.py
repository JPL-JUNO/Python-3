"""
@File         : binary_vs_linear_search.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-02 18:12:48
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import timeit
from binary_search import binary_search
from linear_search import linear_search


def time_and_log(function, needle, haystack):
    index = function(needle, haystack)

    t = timeit.timeit(
        stmt=f"{function.__name__}(needle, haystack)", setup=setup, number=iterations
    )
    print(
        f"[{function.__name__}] Value {needle:<8} found in haystack of "
        f"size {len(haystack):<8} at index "
        f"{index:<8} in {t/iterations:.5e} seconds"
    )


if __name__ == "__main__":
    setup = "from __main__ import binary_search, linear_search, haystack, needle"
    iterations = 1_000

    for haystack_size in (10_000, 100_000, 1_000_000):
        haystack = range(haystack_size)
        for needle in (1, 6_000, 9_000, 1_000_000):
            time_and_log(linear_search, needle, haystack)
            time_and_log(binary_search, needle, haystack)
