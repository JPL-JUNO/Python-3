"""
@Title: 反向迭代
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-03 19:52:24
@Description: 
"""
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

f = open('example1.txt')
for line in reversed(list(f)):
    print(line, end='')


class Countdown:
    def __init__(self, start) -> None:
        self.start = start

    # forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
# 定义一个反向迭代器可使代码变得更加高效，因为这样就无需先把数据放到列表中，
# 然后再反向去迭代列表了。
