"""
@File         : step5.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 20:13:36
@Email        : cuixuanstephen@gmail.com
@Description  : 定制构造函数
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

    def __str__(self):
        return f"[Person: {self.name}, {self.pay}]"


class Manager(Person):
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, "mgr", pay)  # Run original with 'mgr'

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
    tom = Manager("Tom Jones", 50_000)  # Job name not needed:
    tom.give_raise(0.10)  # Implied/set by class
    print(tom.last_name())
    print(tom)
