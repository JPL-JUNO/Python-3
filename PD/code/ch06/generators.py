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


def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1


c = countdown(3)
for i in c:
    print("T-minus", i)

for n in c:
    print("T-minus", i)


class countdown:
    def __init__(self, start) -> None:
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1


# Generator Delegation
def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1


def countdown(start):
    n = start
    while n > 0:
        yield n
        n -= 1


def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)


for i in up_and_down(5):
    print(i, end=" ")


def up_and_down(n):
    for x in countup(n):
        yield x
    for x in countdown(n):
        yield x


def flatten(items):
    for i in items:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


a = [1, 2, [3, [4, 5], 6, 7], 8]
for x in flatten(a):
    print(x, end=" ")

import pathlib, re

for path in pathlib.Path(".").rglob("*.py"):
    if path.exists():
        with path.open("rt", encoding="utf-8") as file:
            for line in file:
                # 匹配注释
                m = re.match(".*(#.*)$", line)
                if m:
                    # 获取注释
                    comment = m.group(1)
                    if "spam" in comment:
                        print(comment)


def get_paths(top_dir, pattern):
    for path in pathlib.Path(top_dir).rglob(pattern):
        if path.exists():
            yield path


def get_files(paths):
    for path in paths:
        with path.open("rt", encoding="utf-8") as file:
            yield file


def get_lines(files):
    # file 本身是个迭代器
    for file in files:
        yield from file


def get_comments(lines):
    for line in lines:
        m = re.match(".*(#.*)$", line)
        if m:
            yield m.group(1)


def print_matching(lines, substring):
    for line in lines:
        if substring in line:
            print(line)


paths = get_paths(".", "*.py")
files = get_files(paths)
lines = get_lines(files)
comments = get_comments(lines)
print_matching(comments, "spam")
