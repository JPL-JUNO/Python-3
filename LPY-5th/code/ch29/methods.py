"""
@File         : methods.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-28 21:56:29
@Email        : cuixuanstephen@gmail.com
@Description  : 方法
"""


class NextClass:  # Define class
    def printer(self, text):  # Define method
        self.message = text  # Change instance
        print(self.message)  # Access instance


x = NextClass()
x.printer("Instance call")  # Call its method
x.message
NextClass.printer(x, "class call")  # Direct class call
x.message  # Instance changed again
