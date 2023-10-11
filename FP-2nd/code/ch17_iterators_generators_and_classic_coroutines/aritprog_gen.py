"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-11 22:13:49
@Description: 
"""


def aritprog_gen(begin, step, end=None):
    result = type(begin+step)(begin)
    forever_mask = end is None
    index = 0
    while forever_mask or result < end:
        yield result
        index += 1
        result = begin + step*index
