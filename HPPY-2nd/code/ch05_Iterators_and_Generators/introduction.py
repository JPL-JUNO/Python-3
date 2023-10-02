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


def test_fibonacci_list():
    """
    >>> %timeit test_fibonacci_list()
    728 ms ± 68.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    >>> %load_ext memory_profiler
    >>> %memit test_fibonacci_list()
    peak memory: 536.66 MiB, increment: 447.37 MiB
    """
    for _ in fibonacci_list(100_000):
        pass


def test_fibonacci_gen():
    """
    基本不会增加任何的运行内存，并且运行效率同样提升
    >>> %timeit test_fibonacci_gen()
    166 ms ± 11.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    >>> %memit test_fibonacci_gen()
    peak memory: 94.02 MiB, increment: 0.03 MiB
    """
    for _ in fibonacci_gen(100_000):
        pass


# 这是一个列表生成式，仍然会暂用较大内存
# >>> %memit len([n for n in fibonacci_gen(100_000) if n % 3 == 0])
# peak memory: 209.20 MiB, increment: 116.12 MiB
divisible_by_three = len([n for n in fibonacci_gen(100_000)
                          if n % 3 == 0])

# 这个是一个生成器
# (<value> for <item> in <sequence> if <condition>)
divisible_by_three_gen = (n for n in fibonacci_gen(100_00)
                          if n % 3 == 0)

# sum(1 for n in fibonacci_gen(100_000) if n % 3 == 0)
# 可以省略一个圆括号
# sum((1 for n in fibonacci_gen(100_000) if n % 3 == 0))
# (1 for n in fibonacci_gen(100_000) if n % 3 == 0)

# >>> %memit sum(1 for n in fibonacci_gen(100_000) if n % 3 == 0)
# peak memory: 94.54 MiB, increment: 0.00 MiB
# 运行的内存减少了，但是运行效率嘛，仍然很慢
# >>> %timeit sum(1 for n in fibonacci_gen(100_000) if n % 3 == 0)
# 3.8 s ± 107 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
