"""
@Title: Single dispatch – Polymorphism in Python
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-27 22:21:34
@Description: 
"""

import functools


@functools.singledispatch
def show_type(argument):
    print(f"argument: {argument}")


@show_type.register(int)
def show_int(argument):
    # explicit types
    print(f"int argument: {argument}")


@show_type.register
def show_float(argument: float):
    # 可以使用 Type annotations
    print(f"float argument: {argument}")


show_type("abc")
show_type(123)
show_type(1.23)
# 根据传入的第一个参数的类型调用对应函数

registry = dict()


def register(function):
    type_ = next(iter(function.__annotations__.values()))
    registry[type_] = function

    @functools.wraps(function)
    def _register(argument):
        next_function = registry.get(type(argument), function)
        return next_function(argument)
    return _register


@register
def show_type(argument: any):
    print(f"argument: {argument}")


@register
def show_int(argument: int):
    print(f"int argument: {argument}")


show_type("abc")
show_type(123)

# A slightly more useful example
import json


@functools.singledispatch
def write_as_json(file, data):
    json.dump(data, file)


@write_as_json.register(str)
@write_as_json.register(bytes)
def write_as_json_filename(file, data):
    # 这里定义的函数名似乎没有任何的影响
    # write_as_json 会根据第一个参数来进行判断如何调用
    with open(file, 'w') as fh:
        write_as_json(fh, data)


data = dict(a=1, b=2, c=3)
write_as_json("test1.json", data)
write_as_json(b"test2.json", 'w')
with open("test3.json", "w") as fh:
    write_as_json(fh, data)

write_as_json.registry.keys()
