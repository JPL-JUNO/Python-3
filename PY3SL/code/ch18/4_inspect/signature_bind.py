"""
@Title: signature_bind.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 14:10:58
@Description: 
"""

import inspect
import example

sig = inspect.signature(example.module_level_function)

bound = sig.bind(
    "this is arg1",
    "this is arg2",
    "this is an extra positional argument",
    extra_named_arg="value",
)

print("Arguments:")
for name, value in bound.arguments.items():
    print("{} = {!r}".format(name, value))

print("\nCalling:")
# The BoundArguments instance has attributes args and kwargs that can be used to call
# the function using the syntax to expand the tuple and dictionary onto the stack as the
# arguments.
print(example.module_level_function(*bound.args, **bound.kwargs))
