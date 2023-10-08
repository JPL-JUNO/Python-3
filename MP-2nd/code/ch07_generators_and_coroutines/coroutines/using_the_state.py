"""
@Title: 如何写一个函数，必须记住所有的状态
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-08 17:47:16
@Description: 
"""

import itertools
from coroutine_decorator import coroutine


@coroutine
def average():
    total = yield
    for count in itertools.count(start=1):
        total += yield total / count


averager = average()
averager.send(20)
averager.send(15)


@coroutine
def print_(formatstring):
    while True:
        print(formatstring.format((yield)))


@coroutine
def average(target):
    total = 0
    for count in itertools.count(start=1):
        # keep track the measure count by using itertools.count
        total += yield
        target.send(total / count)


printer = print_('{:.1f}')
averager = average(printer)
averager.send(20)
averager.send(15)


# 示例：itertools.groupby

@coroutine
def groupby():
    key, value = yield
    old_key, values = key, []
    while True:
        old_value = value
        if key == old_key:
            key, value = yield
        else:
            key, value = yield old_key, values
            old_key, values = key, []
        values.append(old_value)


grouper = groupby()
grouper.send('a1')
grouper.send('a2')
grouper.send('a3')
grouper.send('b1')
grouper.send('b2')
grouper.send('a1')
grouper.send('a2')
grouper.send((None, None))

# 纯粹的协程版本


@coroutine
def print_(formatstring):
    while True:
        print(formatstring.format(*(yield)))


@coroutine
def groupby(target):
    old_key = None
    while True:
        key, value = yield
        if old_key != key:
            if old_key and values:
                target.send((old_key, values))
            values = []
            old_key = key
        values.append(value)


grouper = groupby(print_('group: {}, values: {}'))
grouper.send('a1')
grouper.send('a2')
grouper.send('a3')
grouper.send('b1')
grouper.send('b2')
grouper.send('a1')
grouper.send('a2')
grouper.send((None, None))
