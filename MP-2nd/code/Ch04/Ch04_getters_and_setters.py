"""
@Description: No need for getters and setters with properties
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-23 00:08:42
"""


class Sandwich:
    def __init__(self, spam) -> None:
        self.spam = spam

    @property
    def spam(self):
        return self._spam

    @spam.setter
    def spam(self, value):
        self._spam = value
        if self._spam >= 5:
            print('You must be hungry')

    @spam.deleter
    def spam(self):
        self._spam = 0


sandwich = Sandwich(2)
sandwich.spam += 1
assert sandwich.spam == 3
sandwich.spam += 2
