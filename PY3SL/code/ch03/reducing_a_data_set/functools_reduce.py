"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 21:16:34
@Description: 
"""
import functools


def do_reduce(a, b):
    print("do_reduce({}, {})".format(a, b))
    return a + b


data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data)
print("result: {}".format(result))
print()

# 可选的参数 initializer 放在序列最前面，可以利用这个参数以新输入更新前面计算的值
result = functools.reduce(do_reduce, data, 99)  # 位置参数，好像不是关键字参数
# a previous sum of 99 is used to initialize the value computed by reduce().
print("result: {}".format(result))
print()


# Sequences with a single item automatically reduce to that value when no initializer is
# present. Empty lists generate an error, unless an initializer is provided.


print("Single item in sequence:",
      functools.reduce(do_reduce, [1]))
print()
print("Single item in sequence with initializer:",
      functools.reduce(do_reduce, [1], 99))
print()

print("Empty sequence with initializer:",
      functools.reduce(do_reduce, [], 99))
print()

try:
    print("Empty sequence:", functools.reduce(do_reduce, []))
except TypeError as err:
    print("Error: {}".format(err))
