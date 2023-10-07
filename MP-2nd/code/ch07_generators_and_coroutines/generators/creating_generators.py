"""
@Title: Creating generators
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 13:57:59
@Description: 
"""


def generator():
    # The key difference with regular functions containing a return is
    # that you can have many yield statements in your function.
    yield 1
    yield 'a'
    yield []
    return "end"


result = generator()
print(result)
try:
    len(result)
except TypeError as e:
    print(e)
    print("不支持长度")

try:
    result[:10]
except TypeError as e:
    print(e)
    print("不支持切片")

list(result)
# 一次性的
# 似乎看见 return 的值消失了
# 不是这样的，return 的值在 StopIteration 中可以看见
assert list(result) == []


def generator_with_return():
    yield "some value"
    return "The end of our generator"


result = generator_with_return()
print(next(result))
try:
    next(result)
except StopIteration as e:
    print(e)
    print("这里体现的 return 的值")


def lazy():
    """阐释了懒加载（执行）的实现"""
    print("before the yield")
    yield "yielding"
    print("after the yield")


generator = lazy()
print(next(generator))
# print(next(generator))


print()
generator = lazy()
next(generator)
try:
    next(generator)
except StopIteration:
    pass

print()
for item in lazy():
    print(item)

# To properly handle generators,
# you always need to either catch the StopIteration yourself,
# or use a loop or another structure
# that handles the StopIteration implicitly.
