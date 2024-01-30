"""
@File         : 3_nested_scope_examples.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 14:44:42
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

X = 99  # Global scope name: not used


def f1():
    X = 88  # Enclosing def local

    def f2():
        print(X)  # Reference made in nested def

    f2()


f1()  # Prints 88: enclosing def local


def f1():
    X = 999

    def f2():
        print(X)

    return f2


action = f1()
action()
