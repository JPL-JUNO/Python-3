"""
@File         : Inheritance.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-29 20:10:52
@Email        : cuixuanstephen@gmail.com
@Description  : 继承
"""


class Super:
    def method(self):
        print("in Super.method")


class Sub(Super):
    def method(self):  # Override method
        print("starting Sub.method")  # Add actions here
        Super.method(self)  # Run default action
        print("ending Sub.method")


x = Super()  # Make a Super instance
x.method()  # Runs Super.method
x = Sub()  # Make a Sub instance
x.method()  # Runs Sub.method, calls Super.method
