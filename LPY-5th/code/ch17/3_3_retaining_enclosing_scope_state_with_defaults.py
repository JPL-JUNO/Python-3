"""
@File         : 3_3_retaining_enclosing_scope_state_with_defaults.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-30 19:56:41
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def info(string):
    print("-" * 10, string, "-" * 10)


def f1():
    x = 88

    def f2(x=x):  # Remember enclosing scope X with defaults
        print(x)

    f2()


f1()  # Prints 88
info("Nested scopes, defaults, and lambdas")


def func():
    x = 4
    action = lambda n: x**n  # x remembered from enclosing def
    return action


x = func()
print(x(2))  # Prints 16, 4 ** 2


def func():
    x = 4
    action = lambda n, x=x: x**n  # Pass x in manually
    return action


info("Loop variables may require defaults, not scopes")


def make_actions():
    acts = []
    for i in range(5):  # Tries to remember each i
        acts.append(lambda x: i**x)  # But all remember same last i!
    return acts


acts = make_actions()
assert acts[0](2) == acts[2](2) == acts[4](2) == 16


def make_actions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)
    return acts


acts = make_actions()
assert acts[0](2) == 0

info("Arbitrary scope nesting")


def f1():
    x = 99

    def f2():
        def f3():
            print(x)  # Found in f1's local scope!

        f3()

    f2()


f1()
# Except in limited contexts, your life (and the lives of your
# coworkers) will generally be better if you minimize nested function definitions.
