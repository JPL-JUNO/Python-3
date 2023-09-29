"""
@Title: signature_bind_partial.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 14:27:11
@Description: 
"""

import inspect
import example

sig = inspect.signature(example.module_level_function)
partial = sig.bind_partial(
    "this is arg1",
)

print("Without defaults:")
for name, value in partial.arguments.items():
    print("{} = {!r}".format(name, value))

print("\nWith defaults:")
partial.apply_defaults()  # 可以增加默认值中的值
for name, value in partial.arguments.items():
    print("{} = {!r}".format(name, value))
