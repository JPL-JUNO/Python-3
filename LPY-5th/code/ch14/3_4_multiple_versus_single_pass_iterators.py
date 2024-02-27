"""
@File         : 3_4_multiple_versus_single_pass_iterators.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-25 20:47:27
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

R = range(3)
try:
    next(R)
except TypeError as e:
    print(e)

I1 = iter(R)
assert next(I1) == 0
assert next(I1) == 1

I2 = iter(R)
assert next(I2) == 0
assert next(I1) == 2

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)  # Two iterators on one zip
I2 = iter(Z)
assert I1 is I2
assert next(I1) == (1, 10)
assert next(I1) == (2, 11)
assert next(I2) == (3, 12)  # (3.X) I2 is at same spot as I1!

M = map(abs, (-1, 0, 1))
I1 = iter(M)
I2 = iter(M)
assert I1 is I2
print(next(I1), next(I1), next(I1))

try:
    next(I2)
except StopIteration as e:
    print(e)

R = range(3)
I1, I2 = iter(R), iter(R)
assert I1 is not I2

[next(I1), next(I1), next(I1)]
assert next(I2) == 0
