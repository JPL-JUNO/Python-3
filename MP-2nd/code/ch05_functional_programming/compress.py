"""
@Title: Selecting items using a list of Booleans
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 13:40:39
@Description: It applies a Boolean filter to your iterable, making it return only the elements you actually need. 
"""

import itertools
# stop if either the data is exhausted
# or no elements are being fetched anymore
# so even with infinite range, it works without a hitch
assert list(itertools.compress(range(1_000), [
            0, 1, 1, 1, 0, 1])) == [1, 2, 3, 5]

# 如果对于一个很大的数据，并且计算是 heavy operation，还是数据是可变的
primes = [0, 0, 1, 1, 0, 1, 1]
odd = [0, 1, 0, 1, 0, 1, 0, 1]
numbers = ['zero', 'one', 'two', 'three', 'four', 'five']

assert list(itertools.compress(numbers, primes)) == ['two', 'three', 'five']
assert list(itertools.compress(numbers, odd)) == ['one', 'three', 'five']
assert list(itertools.compress(numbers, map(
    all, zip(odd, primes)))) == ['three', 'five']
