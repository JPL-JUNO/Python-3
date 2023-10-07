"""
@Title: Breaking an iterable up into chunks/groups
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 16:38:12
@Description: 
"""

import itertools


def grouper(iterable, n, fillvalue=None):
    """"""
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


list(grouper('ABCDEFG', 3, 'X'))


def chunker(iterable, chunk_size):
    iterable = iter(iterable)

    def chunk(value):
        yield value

        for _ in range(chunk_size - 1):
            try:
                yield next(iterable)
            except StopIteration:
                break
    while True:
        try:
            yield chunk(next(iterable))
        except StopIteration:
            break


for chunk in chunker('ABCDEFG', 3):
    for value in chunk:
        print(value, end=', ')
    print()
