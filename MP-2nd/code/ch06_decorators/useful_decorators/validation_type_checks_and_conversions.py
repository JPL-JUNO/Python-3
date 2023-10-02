"""
@Title: Validation, type checks, and conversions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 10:56:47
@Description: 
"""

import inspect
import functools


def enforce_type_hints(function):
    # Contract the signature from the function which
    # contains the type annotations
    signature = inspect.signature(function)

    @functools.wraps(function)
    def _enforce_type_hints(*args, **kwargs):
        # Bind the argument and apply the default values
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()

        for key, value in bound.arguments.items():
            param = signature.parameters[key]
            # the annotation should be a callable
            # type/function so we can cast as validation
            if param.annotation:
                bound.arguments[key] = param.annotation(value)
        return function(*bound.args, **bound.kwargs)
    return _enforce_type_hints


@enforce_type_hints
def sandwich(bacon: float, egg: int):
    print(f"bacon: {bacon!r}, eggs: {egg!r}")


sandwich(1, 2)
try:
    sandwich(3, "abc")
except ValueError as err:
    print(err)
