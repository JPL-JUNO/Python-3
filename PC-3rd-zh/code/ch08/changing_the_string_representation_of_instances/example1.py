"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 10:24:58
@Description: 
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair({0.x!r}, {0.y!r})".format(self)
        # return "Pair(%r, %r)" % (self.x, self.y)

    def __str__(self):
        return "({0.x!s}, {0.y!s})".format(self)
