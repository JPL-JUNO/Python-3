"""
@File         : 3_5_dictionary_view_iterables.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-25 21:37:24
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()  # A view object in 3.X, not a list

try:
    next(K)
except TypeError as e:
    print(e)

I = iter(K)
assert next(I) == "a"
assert next(I) == "b"

for k in D.keys():
    print(k, end=" ")

K = D.keys()
list(K)
V = D.values()
list(V)

try:
    V[0]
except TypeError as e:
    print(e)

assert list(V)[0] == 1
list(D.items())

for k, v in D.items():
    print(k, v, end=" ")
print()

I = iter(D)
assert next(I) == "a"
assert next(I) == "b"

for key in D:
    print(key, end=" ")
print()

for k in sorted(D.keys()):
    print(k, D[k], end=" ")

for k in sorted(D):  # "Best practice" key sorting
    print(k, D[k], end=" ")
