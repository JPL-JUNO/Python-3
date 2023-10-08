"""
@Title: Mixing generators and coroutines
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 22:57:58
@Description: 
"""

from coroutine_decorator import coroutine

lines = 'some old text', 'really really old', 'old old old'


@coroutine
def replace(search, replace):
    while True:
        item = yield
        # 为什么是打印，而不是生成
        print(item.replace(search, replace))


old_replace = replace('old', 'new')
for line in lines:
    old_replace.send(line)


@coroutine
def replace(search, replace):
    while True:
        item = yield
        yield item.replace(search, replace)


old_replace = replace('old', 'new')
for line in lines:
    # 这里不会显示任何的结果
    old_replace.send(line)


@coroutine
def replace(search, replace):
    item = yield
    while True:
        item = yield item.replace(search, replace)


# 这个仅仅是使用协程模仿生成器，实际上没有任何的意义
old_replace = replace('old', 'new')
for line in lines:
    old_replace.send(line)


@coroutine
def replace(target, search, replace):
    while True:
        target.send((yield).replace(search, replace))


# Print will print the items using the provided formatstring
@coroutine
def print_(formatstring):
    count = 0
    while True:
        count += 1
        print(count, formatstring.format((yield)))

# tee multiplexes the items to multiple targets


@coroutine
def tee(*targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


# First, create a printer for the items:
printer = print_('print: {}')

old_replace = replace(printer, 'old', 'new')
current_replace = replace(printer, 'old', 'current')

branch = tee(old_replace, current_replace)
for line in lines:
    branch.send(line)
