"""
@File         : person-composite.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 20:19:22
@Email        : cuixuanstephen@gmail.com
@Description  : 组合类的其他方式
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


class Manager:
    def __init__(self, name, pay) -> None:
        self.person = Person(name, "mgr", pay)  # Embed a Person object

    def give_raise(self, percent, bonus=0.1):
        self.person.give_raise(percent + bonus)  # Intercept and delegate

    def __getattr__(self, attr):
        return getattr(self.person, attr)  # Delegate all other attrs

    def __str__(self) -> str:
        return str(self.person)  # Must overload again (in 3.X)


# Manager 不是一个真正的 Person，因此，我们
# 需要额外的代码手动为嵌入的对象分派方法；像 __str__ 这样的运算符重载方
# 法必须重新定义
