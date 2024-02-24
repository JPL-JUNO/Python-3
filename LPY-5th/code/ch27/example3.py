"""
@File         : example3.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-17 22:23:23
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class FirstClass:  # Define a class object
    def set_data(self, value):  # Define class's methods
        self.data = value  # self is the instance

    def display(self):
        print(self.data)  # self.data: per instance


class SecondClass(FirstClass):
    def display(self):
        print(f"Current value = {self.data}")


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self) -> str:
        return f"[ThirdClass: {self.data}]"

    def mul(self, other):
        self.data *= other


if __name__ == "__main__":
    a = ThirdClass("abc")
    a.display()
    # 对于 print，Python 把要打印的对象传给 __str__ 中的 self
    print(a)

    b = a + "xyz"
    b.display()
    print(b)

    a.mul(3)
    print(a)
