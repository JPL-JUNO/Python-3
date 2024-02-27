"""
@File         : person-department.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 20:24:19
@Email        : cuixuanstephen@gmail.com
@Description  : 
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


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100_000)
    tom = Manager("Tom Jones", 50_000)
    development = Department(bob, sue)  # Embed objects in a composite
    development.add_member(tom)
    development.give_raises(0.10)  # Runs embedded objects' giveRaise
    development.show_all()
