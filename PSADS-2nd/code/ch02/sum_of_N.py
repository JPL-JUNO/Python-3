"""
@Title: 何谓算法分析
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-25 13:04:57
@Description: 算法分析关心的是基于所使用的计算资源比较（内存或时间）算法
"""
import time


def sum_of_N(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i
    return the_sum


def foo(tom):
    """
    你会发现这个函数所做的
    工作在本质上和前一个相同。之所以不能一眼看出来，是因为代码写得太差。没有用好的变量名
    提高可读性，而且在累加时还使用了一条多余的赋值语句。
    """
    fred = 0
    for bill in range(1, tom + 1):
        barney = bill
        fred = fred + barney
    return fred


def sum_of_N_time(n):
    start = time.time()
    sum_of_N(n)
    end = time.time()
    return end - start


def sum_of_N_3(n):
    # 如果在另一台计算机上运行这个函数，或用另一种编程语言来实现，很可能会得到
    # 不同的结果。如果计算机再旧些，sum_of_N_3 的执行时间甚至更长。
    return (n * (n + 1)) / 2


for i in range(5):
    for n in (10_000, 100_000, 1_000_000):
        print("Sum is %15.d required %10.7f seconds" %
              (sum_of_N(n), sum_of_N_time(n)))

n = 10_000
a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a * k + 45
    v = b * b
d = 33
# 赋值操作的数量是 4 项之和：T(n)=3+3n^2+2n+1=3n^2+2n+4。
# 很容易看出来，n^2 起主导作用，所以这段代码的时间复杂度是 O(n^2)
