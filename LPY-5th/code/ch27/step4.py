"""
@File  : step4.py
@Author: Stephen CUI
@Time  : 2024-02-27 12:37:13
"""


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f"[Person: {self.name}, {self.pay}]"


class Manager(Person):
    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100_000)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.1)
    print(sue)
    tom = Manager("Tom Jones", "mgr", 50_000)
    tom.give_raise(0.1)
    print(tom.last_name())
    print(tom)
