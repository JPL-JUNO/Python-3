"""
@File  : item9.py
@Author: Stephen CUI
@Time  : 2024-04-03 16:45:03
"""

for i in range(3):
    print("Loop", i)
else:
    print("Else Block!")


for i in range(3):
    print("Loop", i)
    if i == 1:
        break
else:
    print("Else Block!")

for x in []:
    print("Never runs")
else:
    print("For Else Block")


while False:
    print("Never runs")
else:
    print("For Else Block")

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    # 互质：除了 1，没有其他数可以同时整除他们
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print("Not coprime")
        break
else:
    print("Coprime")


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


assert coprime(4, 9)
assert not coprime(3, 6)


def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime


assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
