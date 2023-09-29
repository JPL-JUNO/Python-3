"""
@Title: signature_function.py
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-29 13:54:26
@Description: 
"""
import inspect
import example

sig = inspect.signature(example.module_level_function)
print("module_level_function{}".format(sig))

print("\nParameter details")
for name, param in sig.parameters.items():
    if param.kind == inspect.Parameter.POSITIONAL_ONLY:
        print("  {} (position-only)".format(name))
    elif param.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD:
        if param.default != inspect.Parameter.empty:
            print("  {}={!r}".format(name, param.default))
        else:
            print("  {}".format(name))
    elif param.kind == inspect.Parameter.VAR_POSITIONAL:
        print("  *{}".format(name))
    elif param.kind == inspect.Parameter.KEYWORD_ONLY:
        if param.default != inspect.Parameter.empty:
            print("  {}={!r} (keyword-only)".format(name, param.default))
        else:
            print("  {} (keyword-only)".format(name))
    elif param.kind == inspect.Parameter.VAR_KEYWORD:
        print("  **{}".format(name))
