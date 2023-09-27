"""
@Title: Decorating class functions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 12:40:07
@Description: 
"""

import functools


def plus_one(function):
    @functools.wraps(function)
    def _plus_one(self, n, *args):
        # the class function decorator now gets passed along self
        # as the instance
        return function(self, n + 1, *args)
    return _plus_one


class Adder(object):
    @plus_one
    def add(self, a, b=0):
        return a + b


adder = Adder()
assert adder.add(0) == 1
assert adder.add(3, 4) == 8
