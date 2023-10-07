"""
@Title: itertools.tee – Using an output multiple times 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 18:32:07
@Description: 
"""
# 弥补生成器只能使用一次的缺点

import itertools


def spam_and_eggs():
    yield "spam"
    yield "eggs"


a, b = itertools.tee(spam_and_eggs())
assert next(a) == 'spam'
assert next(a) == 'eggs'
assert next(b) == 'spam'
assert next(b) == 'eggs'
