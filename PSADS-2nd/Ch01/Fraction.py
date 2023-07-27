"""
@Description: Fraction 类
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-27 20:01:51
"""


def gcd(m: int, n: int) -> int:
    """实现寻找最大公因数（Greatest Common Divisor, GCD）

    Parameters
    ----------
    m : int
        _description_
    n : int
        _description_

    Returns
    -------
    int
        `m` 和 `n` 的最大公因数
    """
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)

    def __str__(self) -> str:
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num


my_fraction = Fraction(3, 5)
# my_fraction 唯一能做的就是显示存储在变量中的实际引用（地址本身）。
# 但是这里我们复写了 __str__ 方法，
print(my_fraction)

my_fraction.show()

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
try:
    print(f1 + f2)
except TypeError:
    print('目前还没有实现加法运算')

f1 = Fraction(1, 3)
f2 = Fraction(10, 30)
assert f1 == f2
