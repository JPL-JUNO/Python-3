"""
@File         : class_statement.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-28 21:37:58
@Email        : cuixuanstephen@gmail.com
@Description  : class 语句
"""


class SharedData:
    spam = 42  # Generates a class data attribute


x = SharedData()  # Make two instances
y = SharedData()
x.spam, y.spam  # They inherit and share 'spam' (a.k.a. SharedData.spam)
SharedData.spam = 99
x.spam, y.spam, SharedData.spam
x.spam = 88
x.spam, y.spam, SharedData.spam


class MixedNames:
    data = "spam"

    def __init__(self, value) -> None:
        self.data = value

    def display(self):
        print(self.data, MixedNames.data)


x = MixedNames(1)
y = MixedNames(2)
x.display()
y.display()
