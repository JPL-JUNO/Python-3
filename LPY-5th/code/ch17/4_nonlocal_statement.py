"""
@File         : 4_nonlocal_statement.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-30 20:31:11
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def info(string):
    print("*" * 10, string, "*" * 10)


def tester(start):
    state = start  # Referencing nonlocals works normally

    def nested(label):
        print(label, state)  # Remembers state in enclosing scope

    return nested


F = tester(0)
F("spam")
F("ham")


def tester(start):
    state = start

    def nested(label):
        print(label, state)
        state += 1  # Cannot change by default (never in 2.X)

    return nested


F = tester(0)
try:
    F("spam")
except UnboundLocalError as e:
    print(e)

info("Using nonlocal for changes")


def tester(start):
    state = start  # Each call gets its own state

    def nested(label):
        nonlocal state  # Remembers state in enclosing scope
        print(label, state)
        state += 1  # Allowed to change it if nonlocal

    return nested


# This works even though `tester` has returned
# and exited by the time we call the returned `nested` function through the name `F`
F = tester(0)  # Increments state on each call
F("spam")
F("ham")
F("eggs")

G = tester(42)  # Make a new tester that starts at 42
G("spam")
G("ham")
G("eggs")
# in a closure function, nonlocals are per-call, multiple copy data.

info("Boundary cases")


# def tester(start):
#     def nested(label):
#         nonlocal state  # Nonlocals must already exist in enclosing def!
#         state = 0
#         print(label, state)

#     return nested
# SyntaxError: no binding for nonlocal 'state' found


def tester(start):
    def nested(label):
        global state  # Globals don't have to exist yet when declared
        state = 0  # This creates the name in the module now
        print(label, state)

    return nested


F = tester(0)
F("abc")
assert state == 0

# spam = 99


# def tester():
#     def nested():
#         nonlocal spam  # Must be in a def, not the module!
#         print("Current=", spam)
#         spam += 1

#     return nested
# SyntaxError: no binding for nonlocal 'spam' found
