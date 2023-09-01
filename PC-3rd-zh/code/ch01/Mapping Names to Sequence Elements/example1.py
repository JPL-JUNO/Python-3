"""
@Title: 将名称映射到序列的元素中
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 15:34:52
@Description: 
"""
from collections import namedtuple
Subscriber = namedtuple("Subscribe", ['addr', 'joined'])
sub = Subscriber("cuixuanstephen@gmail.com", "2023-09-01")
print(sub)

sub.addr
sub.joined
assert len(sub) == 2
addr, joined = sub


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


Stock = namedtuple("Stock", ["name", "shares", "price"])


def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
