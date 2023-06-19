"""
@Description: Integers
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-19 21:12:26
"""

a = 14
b = 3
assert a + b == 17
assert a - b == 11
assert a * b == 42
print(a / b)
assert a // b == 4
assert a % b == 2
assert a**b == 2744

assert 7 / 4 == 1.75
assert 7 // 4 == 1
assert -7 / 4 == -1.75
assert -7 // 4 == -2


assert pow(10, 3) == 1000.0
assert 10**3 == 1000
assert pow(10, -3) == .001
assert 10**-3 == .001

assert 10 % 3 == 1
assert 10 % 4 == 2


assert pow(123, 4) == 228886641
assert pow(123, 4, 100) == 41
assert pow(37, -1, 43) == 7
assert 37 * 7 % 43 == 1

n = 1_024
assert n == 1024
hex_n = 0x_4_00
assert hex_n == 1024

# Booleans
assert int(True) == 1
assert int(False) == 0
assert bool(1) == True
assert bool(0) == False
assert bool(-42) == True
assert not True == False
assert not False == True
assert True and True == True
assert False or True == True

assert 1 + True == 2
assert False + 42 == 42
assert 7 - True == 6
