"""
@Title: chain.from_iterable()
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:18:27
@Description: 
"""

from itertools import chain


def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c', 'd', 'e', 'f']


for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=" ")
