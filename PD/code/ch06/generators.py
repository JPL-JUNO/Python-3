def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


def func():
    yield 37
    return 42


f = func()
next(f)
try:
    next(f)
except StopIteration as e:
    value = e.value

for n in countdown(10):
    if n == 2:
        break
    pass


def countdown(n):
    print("Counting down from", n)
    try:
        while n > 0:
            yield n
            n = n - 1
    finally:
        print("Only made it to", n)


# def func(filename):
#     # 伪代码
#     pass
#     with open(filename) as file:
#         yield data
#     pass
