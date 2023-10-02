"""
@Title: map
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:50:34
@Description: 
"""


def times_two(x):
    return x * 2


def multiply(x, y):
    return (x, y, x * y)


print("Doubles:")
for i in map(times_two, range(5)):
    print(i)

print("\nMultiples:")
r1 = range(0, 5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print("{:d} * {:d} = {:d}".format(*i))

print("\nStopping:")
# 任一一个迭代器被消耗则停止，与 zip 类似
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)
