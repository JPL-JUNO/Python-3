"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-15 23:07:38
@Description: 
"""

# for (i=0; i<10; i++){
#     do_work(i);
# }


def do_work(n):
    pass


# 看起来我们调用了 range 然后生成了数据，（这可能是个耗时的过程），但实际上不是这样的
for i in range(10):
    do_work(i)

# range 函数实际上允许我们进行懒评估，这类函数保留可读性的同时没有性能上的影响


def fibonacci_list(num_items):
    numbers = []
    a, b = 0, 1
    while len(numbers) < num_items:
        numbers.append(a)
        a, b = b, a + b
    return numbers


def fibonacci_gen(num_items):
    a, b = 0, 1
    while num_items:
        # This function will yield many values instead of returning one value.
        # This turns this regular-looking function into a generator
        # that can be polled repeatedly for the next available value.
        yield a
        a, b = b, a + b
        num_items -= 1


# 任意一个可迭代对象
iterable_object = list()

for i in iterable_object:
    do_work(i)
# is equivalent to

object_iterator = iter(iterable_object)
while True:
    try:
        i = next(object_iterator)
    except StopIteration:
        break
    else:
        do_work(i)
