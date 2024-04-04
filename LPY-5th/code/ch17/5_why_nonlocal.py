"""
@File         : 5_why_nonlocal.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-30 21:26:31
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def info(string):
    print("*" * 10, string, "*" * 10)


info("State with nonlocal: 3.X only")


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1

    return nested


F = tester(0)
F("spam")
try:
    F.state
except AttributeError as e:
    print(e)
    print("nonlocal 声明变量在外层函数外面是看不见的")

info("State with Globals: A Single Copy Only")


def tester(start):
    global state  # Move it out to the module to change it
    state = start  # global allows changes in module scope

    def nested(label):
        global state
        print(label, state)
        state += 1

    return nested


F = tester(0)
F("spam")  # Each call increments shared global state
F("eggs")
# A worse, and more subtle, problem is that it only allows for a single shared copy of the
# state information in the module scope

G = tester(42)
G("toast")
G("bacon")
F("ham")

# 只能保持一个副本，不能对每次调用外层函数都记住

info("State with Classes: Explicit Attributes (Preview)")


class Tester:
    def __init__(self, start):
        self.state = start  # save state explicitly in new object

    def nested(self, label):
        print(label, self.state)  # Reference state explicitly
        self.state += 1  # Changes are always allowed


F = Tester(0)
F.nested("spam")
F.nested("ham")

G = Tester(42)  # Each instance gets new copy of state
G.nested("toast")  # Changing one does not impact others

F.nested("eggs")  # F's state is where it left off
assert F.state == 3  # State may be accessed outside class


class Tester:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):  # Intercept direct instance calls
        print(label, self.state)  # So .nested() not required
        self.state += 1


H = Tester(999)
H("juice")
H("pancakes")

info("State with Function Attributes: 3.X and 2.X")
