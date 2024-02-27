"""
@File         : person.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 21:42:31
@Email        : cuixuanstephen@gmail.com
@Description  : Record and process information about people. Run this file directly to test its classes.
"""

import sys
from os import path

sys.path.append(path.normpath(path.join(path.dirname(__file__), "..")))
from classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and process person records
    """

    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]  # Assumes last is last

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay=0) -> None:
        Person.__init__(self, name, "mgr", pay)  # Job name is implied

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100_000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.10)
    print(sue)
    tom = Manager("Tom Jones", 50000)
    tom.give_raise(0.10)
    print(tom.last_name())
    print(tom)
