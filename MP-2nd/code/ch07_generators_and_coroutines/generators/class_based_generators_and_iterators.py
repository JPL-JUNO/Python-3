"""
@Title: Class-based generators and iterators
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-07 15:10:12
@Description: 
"""


class CountGenerator:
    """名称有点歧义，
    该类的实现仅仅完成了 __iter__，应该仅是可迭代的"""

    def __init__(self, start=0, step=1, stop=None):
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):

        i = self.start
        while self.stop is None or i < self.stop:
            yield i
            i += self.step


# 如果不指定 stop 将会是一个无穷的迭代器，这会耗尽内存
assert list(CountGenerator(start=2.5, step=.5, stop=5)) == [
    2.5, 3.0, 3.5, 4.0, 4.5]


class CountIterator:
    def __init__(self, start=0, step=1, stop=None):
        self.i = start
        self.start = start
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop is not None and self.i >= self.stop:
            raise StopIteration
        value = self.i
        # 使用新变量 i 是为了可以重现迭代器，不然这个迭代器是一次性的
        self.i += self.step
        return value


assert list(CountIterator(start=2.5, step=.5, stop=5)) == [
    2.5, 3.0, 3.5, 4.0, 4.5]

import itertools


class AdvancedCountIterator(CountIterator):
    def __init__(self, start=2.5, step=.5, stop=None):
        super().__init__(start=start, step=step, stop=stop)

    def __len__(self):
        return int((self.stop - self.start) / self.step)

    def __contains__(self, key):
        return self.start < key < self.stop

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(start={self.start}, "
            f"step={self.step}, stop={self.stop})"
        )

    def __getitem__(self, slice_):
        return itertools.islice(self, slice_.start, slice_.stop, slice_.step)


count = AdvancedCountIterator(start=2.5, step=.5, stop=5)

# Pretty representation using '__repr__'
print(count)

assert 3 in count
assert 3.1 in count
assert not 5.2 in count
assert len(count) == 5


count[:3]
assert list(count[:3]) == [2.5, 3.0, 3.5]
assert list(count[:3]) == [4.0, 4.5]
