"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 21:44:03
@Description: 
"""

import random


class BingoCage:
    # Why build a BingoCage when we already have random.choice?
    # The choice function may return the same item multiple times,
    # because the picked item is not removed from the collection given.
    # Calling BingoCage never returns duplicate results—as long as the instance is filled with unique values.
    def __init__(self, items):
        # building a local copy prevents unexpected side
        # effects on any list passed as an argument.
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("Pick from empty BingoCage")

    def __call__(self):
        # 它的实例是可以调用的，因为实现了 __call__ 方法
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
bingo()
assert callable(bingo)
