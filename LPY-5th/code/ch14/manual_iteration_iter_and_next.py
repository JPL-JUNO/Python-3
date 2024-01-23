"""
@File         : Manual Iteration.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-23 22:31:26
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

f = open("./script2.py")
f.__next__()
f.__next__()

f = open("./script2.py")
next(f)
next(f)

# Obtain an iterator object from an iterable
L = [1, 2, 3]
I = iter(L)
# Call iterator's next to advance to next item
I.__next__()
# Or use I.next() in 2.X, next(I) in either line
I.__next__()
I.__next__()
try:
    I.__next__()
except StopIteration as e:
    print(e)

# 文件对象就是自己的迭代器。
# 也就是说，文件有自己的__next__方法，
# 因此不需要像这样返回一个不同的对象：
f = open("./script2.py")
assert iter(f) is f
assert iter(f) is f.__iter__()
f.__next__()

L = [1, 2, 3]
assert iter(L) is not L
try:
    L.__next__()
except AttributeError as e:
    print(e)

I = iter(L)
assert I.__next__() == 1
assert next(I) == 2  # Same as I.__next__()
