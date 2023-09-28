"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 23:32:08
@Description: Create a single-dispatch decorator that considers all or a configurable number of arguments instead of only the first one.
"""

import functools
import inspect
import typing


def fancy_single_dispatch(*disabled_args, **disabled_kwargs):
    """A single-dispatch decorator that considers all or a configurable
    number of arguments instead of only the first one.

    Returns
    -------
    _type_
        _description_

    Raises
    ------
    TypeError
        _description_
    """
    registry = dict()
    disabled_args = set(disabled_args)
    for key, value in disabled_kwargs.items():
        if value:
            disabled_args.add(key)

    def register(function):
        key_parts = []
        for key, type_ in typing.get_type_hints(function).items():
            if key == "return":
                # ignore the return type
                continue
            if key in disabled_args:
                key_parts.append(None)
            else:
                key_parts.append(type_)
        registry[tuple(key_parts)] = function
        return function

    def dispatch(function):
        signature = inspect.signature(function)

        @functools.wraps(function)
        def _dispatch(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()

            key_parts = []
            for key, value in bound.arguments.items():
                if key in disabled_args:
                    key_parts.append(None)
                else:
                    key_parts.append(type(value))
            key = tuple(key_parts)
            if key in registry:
                return registry[key](*args, **kwargs)
            else:
                raise TypeError(f"No matching function for {key}")

        _dispatch.register = register
        register(function)
        return _dispatch

    return dispatch


@fancy_single_dispatch(last_name=True)
def hello(first_name: str, last_name: str, age: None = None) -> str:
    return f"Hello {first_name} {last_name}"


@hello.register
def first_name_only(
    first_name: str,
    last_name: None = None,
    age: None = None,
) -> str:
    return f"Hello {first_name}"


@hello.register
def name_age(first_name: str, last_name: str, age: int) -> str:
    return hello(first_name, last_name) + f', you are {age} years old'


@hello.register
def name_age_days(first_name: str, last_name: str, age: float) -> str:
    days = int((age % 1) * 365)
    age = int(age)
    return hello(first_name, last_name) + \
        f', you are {age} years and {days} days old'


def main():
    # 多态设计
    print(hello("Rick", "Van Hattem"))
    print(hello("Rick", "Van Hattem", age=30))
    print(hello("Rick", "Van Hattem", age=30.5))


if __name__ == "__main__":
    main()
