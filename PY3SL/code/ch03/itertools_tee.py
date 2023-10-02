"""
@Title: tee
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:39:23
@Description: The tee() function returns several independent iterators (defaults to 2) based on a single original input.
"""
from itertools import count, tee, islice

r = islice(count(), 5)
i1, i2 = tee(r)

print("i1:", list(i1))
print("i2:", list(i2))
