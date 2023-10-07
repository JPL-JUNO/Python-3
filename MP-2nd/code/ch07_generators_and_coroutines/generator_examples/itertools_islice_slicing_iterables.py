"""
@Title: itertools.islice – Slicing iterables
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 17:11:45
@Description: 弥补生成器的缺点
"""

import itertools

some_list = list(range(1000))

assert some_list[:5] == [0, 1, 2, 3, 4]

assert list(itertools.islice(some_list, 5)) == [0, 1, 2, 3, 4]

assert some_list[10:20:2] == [10, 12, 14, 16, 18]

assert list(itertools.islice(some_list, 10, 20, 2)) == [10, 12, 14, 16, 18]

# 尽管结果一样，但是内部的实现完全不同
# 常规的切片仅能在可切片对象上（sliceable）工作
# 这意味着它们需要实现 __getitem__ 方法，

# 此外，切片是快速且高效的运行方式，取出任意 k 给元素的时间复杂度是 O(k)
# 无论是 some_list[:10] 还是 some_list[900:920:2]

# 但是 islice 完全不同，获取前十个元素很容易，但是获取第 900 个就很困难


def islice(iterable, start, stop=None, step=1):
    """
    仿写 itertools.islice()
    """
    # 如果只指定一个位置参数，那么这个参数是 stop 的值
    if stop is None and step == 1 and start is not None:
        start, stop = 0, start

    # 创建一个迭代器，忽略前面的 start 个
    iterator = iter(iterable)
    for _ in range(start):
        next(iterator)

    for i, item in enumerate(iterator, start):
        # 停止条件
        if i >= stop:
            return
        # 跳过一些不是的点位
        if i % step:
            continue
        yield item


assert list(islice(range(1_000), 10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert list(islice(range(1_000), 900, 920, 2)) == [
    900, 902, 904, 906, 908, 910, 912, 914, 916, 918]

assert list(islice(range(1_000), 900, 910)) == [
    900, 901, 902, 903, 904, 905, 906, 907, 908, 909]
