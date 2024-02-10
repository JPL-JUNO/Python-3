"""
@File         : example2.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-10 11:22:49
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


x = FirstClass()  # Make two instances
y = FirstClass()  # Each is a new namespace
x.set_data("King Arthur")
y.set_data(3.14159)

x.display()
y.display()

x.data = "New Value"
x.display()

z = SecondClass()
z.set_data(42)
z.display()
