"""
@File         : person.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-18 13:59:58
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class Person:
    # def __init__(self, name, job, pay) -> None:
    #     self.name = name
    #     self.job = job
    #     self.pay = pay
    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100_000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    # print(bob.name.split()[-1])
    # sue.pay *= 1.10
    # print(f"{sue.pay:.2f}")
    print(bob.last_name(), sue.last_name())
    sue.give_raise(0.1)
    print(sue.pay)
