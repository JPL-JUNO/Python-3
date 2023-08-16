# website = 'http://www.python.org'
# website[-3:] = 'com'  # str' object does not support item assignment


import string
import math
from math import e
from math import pi

format = "Hello, %s. %s enough for ya?"
values = ("world", "Hot")
format % values

"{}, {}, {}".format("first", "second", "third")  # 'first, second, third'
"{2}, {0}, {1}".format("first", "second", "third")  # 'third, first, second'
"{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
# 'to be or not to be'

"{name} is approximately {value:.2f}.".format(value=pi, name="pi")
# 'pi is approximately 3.14.'
f"Euler's constant is roughly {e}."
# "Euler's constant is roughly 2.718281828459045."

"Euler's constant is roughly {e}.".format(e=e)
# "Euler's constant is roughly 2.718281828459045."


"{}, {}".format(2, 7)  # '2, 7'
"{foo}, {bar}".format(bar=2, foo=7)  # '7, 2'
"{foo}, {}, {bar}".format(1, bar=2, foo=7)  # '7, 1, 2'

fullname = ["Alfred", "Smoketoomuch"]
"Mr {name[1]}".format(name=fullname)  # 'Mr Smoketoomuch'

tmpl = "The {mod.__name__} module defines the value {mod.pi} for pi."
tmpl.format(mod=math)
# 'The math module defines the value 3.141592653589793 for pi.'

"The number is {num}".format(num=42)  # 'The number is 42'
"The number is {num:f}".format(num=42)  # 'The number is 42.000000'
"The number is {num:b}".format(num=42)  # 'The number is 101010'

"{num:10}".format(num=3)
# '         3'
"{name:10}".format(name="Stephen")
# 'Stephen   '

"Pi day is {pi:.2f}".format(pi=pi)  # 'Pi day is 3.14'
"{pi:10.2f}".format(pi=pi)  # '      3.14'

"One googol is {:,}".format(10 ** 100)
# 'One googol is 10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,00
# 0,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000'

"{:010.2f}".format(pi)  # '0000003.14'
# print("{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi))
# 3.14
#    3.14
#       3.14

# print("{0:-.2}\n{1:-.2}".format(pi, -pi))  # default
# # 3.1
# # -3.1
# print("{0:+.2}\n{1:+.2}".format(pi, -pi))
# # +3.1
# # -3.1
# print("{0: .2}\n{1: .2}".format(pi, -pi))
# #  3.1
# # -3.1

"{:b}".format(42)  # '101010'
"{:#b}".format(42)  # '0b101010'

"{:g}".format(42)  # '42'
"{:#g}".format(42)  # '42.0000'

"The Middle by Jimmy Eat World".center(39)
# '     The Middle by Jimmy Eat World     '
"The Middle by Jimmy Eat World".center(39, "*")
# '*****The Middle by Jimmy Eat World*****'

'With a moo-moo here, and a moo-moo there'.find('moo')  # 7
title = "Monty Python's Flying Circus"
title.find("Python")  # 6
title.find("Flying")  # 15
title.find("Zirquss")  # -1

subject = "$$$ Get rich now!!! $$$"
subject.find("$$$")  # 0
subject.find("$$$", 1)  # 20
subject.find("!!!")  # 16
subject.find("!!!", 0, 16)  # -1

seq = [1, 2, 3, 4, 5, 6]
sep = "+"
# sep.join(seq)
# sequence item 0: expected str instance, int found

seq = ['1', '2', '3', '4', '5']
sep.join(seq)  # '1+2+3+4+5'

'Trondheim Hammer Dance'.lower()  # 'trondheim hammer dance'

"that's all folks.".title()  # "That'S All Folks."
string.capwords("that's all folks.")  # "That's All Folks."

"This is a test".replace("is", "eez")  # 'Theez eez a test'

'1+2+3+4+5'.split('+')
# ['1', '2', '3', '4', '5']
'/usr/bin/env'.split('/')
# ['', 'usr', 'bin', 'env']
'Using the    default'.split()
# ['Using', 'the', 'default']

' internal whitespace is kept '.strip()
# 'internal whitespace is kept'
# names = ["gumby", "smith", "jones"]
# name = "gumby "
# if name in names:
#     print("Found it!")
# if name.strip() in names:
#     print("Found it!")  # Found it!

'*** SPAM * for * everyone!!! ***'.strip(' *!')  # 'SPAM * for * everyone'

table = str.maketrans('cs', 'kz')
table  # {99: 107, 115: 122}
'this is an incredible test'.translate(table)
# 'thiz iz an inkredible tezt'

table = str.maketrans('cs', 'kz', ' ')
'this is an incredible test'.translate(table)  # 'thizizaninkredibletezt'
