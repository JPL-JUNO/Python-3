"""
@Title: grouping your sorted iterable
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 18:05:25
@Description: 
"""

import itertools
import operator

words = ['aa', 'ab', 'ba', 'bb', 'ca', 'cb', 'cc']

getter = operator.itemgetter(0)

for group, items in itertools.groupby(words, key=getter):
    print(f'group: {group}, items: {list(items)}')
# 注意点：
# 1. 必须按照 key 排序
# 2. 结果是一次性的，不能复用，想要复用，需要使用 list 或者 tuple

# 没有排序的副作用
raw_items = ['spam', 'eggs', 'sausage', 'spam']


def key_func(group):
    return group[0]


for group, items in itertools.groupby(raw_items, key_func):
    print(f"group: {group}, items: {list(items)}")
# group: s, items: ['spam']
# group: e, items: ['eggs']
# group: s, items: ['sausage', 'spam']

raw_items.sort()

for group, items in itertools.groupby(raw_items, key=key_func):
    print(f"group: {group}, items: {list(items)}")
# group: e, items: ['eggs']
# group: s, items: ['sausage', 'spam', 'spam']
