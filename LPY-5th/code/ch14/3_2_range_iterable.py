"""
@File         : 3_2_range_iterable.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-25 19:34:07
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""
R = range(10)
print(R)

I = iter(R)
next(I)
next(I)
list(range(10))

assert len(R) == 10
assert R[-1] == 9
assert next(I) == 2
assert I.__next__() == 3
