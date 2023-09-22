"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 09:34:17
@Description: 
"""
from numpy import average


def drop_first_last(grades):
    _, *middle, _ = grades
    return average(middle)


records = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3, 4)
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(s):
    print("bar", s)


for tag, *args in records:
    if tag == "foo":
        do_foo(*args)
    elif tag == "bar":
        do_bar(*args)


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
