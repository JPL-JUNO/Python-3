"""
@Title: Combining multiple results
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 13:35:22
@Description: The chain function is a simple but useful function that combines the results of multiple iterators.
"""
import itertools

a = range(3)
b = range(5)
assert list(itertools.chain(a, b)) == [0, 1, 2, 0, 1, 2, 3, 4]

iterables = [range(3), range(5)]
# accept an iterable containing iterables
assert list(itertools.chain.from_iterable(
    iterables)) == [0, 1, 2, 0, 1, 2, 3, 4]
