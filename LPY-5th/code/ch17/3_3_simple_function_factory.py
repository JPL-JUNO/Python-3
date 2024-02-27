"""
@File         : 3_3_simple_function_factory.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 14:55:10
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def marker(N):
    def action(X):
        return X**N

    return action


f = marker(2)  # Pass 3 to X, N remembers 2: 3 ** 2
# what we get back is a reference to the generated nested function
print(f)

assert f(3) == 9
assert f(4) == 16
# Perhaps the most unusual part of this, though,
# is that the nested function remembers integer 2,
# the value of the variable N in maker,
# even though maker has returned and exited by the time we call action.

# In effect, N from the enclosing local scope is retained as state
# information attached to the generated action,
# which is why we get back its argument squared when it is later called.

g = marker(3)  # g remembers 3, f remembers 2
assert g(4) == 64
assert f(4) == 16
