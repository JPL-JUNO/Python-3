
from math import sqrt
print('Age:', 42)  # Age: 42

name = "Gumby"
salutation = "Mr."
greeting = 'Hello,'
print(greeting, salutation, name)  # Hello, Mr. Gumby

print('I', "wish", 'to', 'register', 'a', 'complaint', sep='_')
# I_wish_to_register_a_complaint

print('Hello, ', end='')
print('World!')
# Hello, World!

x, y, z = 1, 2, 3
x, y, z  # (1, 2, 3)
x, y = y, x
x, y, z  # (2, 1, 3)

a, b, *rest = [1, 2, 3, 4]
rest  # [3, 4]
head, *rest, tail = [1, 2, 3, 4]
rest  # [2, 3]
*head, a, b = [1, 2, 3, 4]
head  # [1, 2]

status = 'friend' if name.endswith('Gumby') else 'stranger'

# num = int(input("Enter a number: "))
# if num > 0:
#     print('The number is positive')
# elif num < 0:
#     print('The number is negative')
# else:
#     print('The number is zero')

# name = input('What is your name?')
# if name.endswith('Gumby'):
#     if name.startswith('Mr.'):
#         print('Hello, Mr. Gumby')
#     elif name.startswith('Mrs.'):
#         print("Hello, Mrs. Gumby")
#     else:
#         print("Hello, Gumby")
# else:
#     print('Hello, stranger')

x = y = [1, 2, 3]
z = [1, 2, 3]
x == y, x == z, x is y, x is z  # (True, True, True, False)
id(x), id(y), id(z)

# name = input('What is your name?')
# if 's' in name:
#     print('Your name contains the letter "s".')
# else:
#     print("Your name does not contain the letter 's'.")
"alpha" < "beta"  # True
"😊" < "😝"
ord('a')  # 97
chr(155)  # '\x9b'

[1, 2] < [2, 1]  # True
[1, [5, 6]] < [1, [5, 7]]  # True
# [1, 2, [5, 6]] < [1, [5, 7]]
# '<' not supported between instances of 'int' and 'list'

age = 10
assert 0 < age < 100

range(0, 10)
range(10)  # range(0, 10)

# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#     print(key, 'correspond to', d[key])

# for key in d.keys():
#     print(key)

# for value in d.values():
#     print(value)

# for key, value in d.items():
#     print(key, 'correspond to', value)

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
list(zip(names, ages))
# [('anne', 12), ('beth', 45), ('george', 32), ('damon', 102)]
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old.')
list(zip(range(5), range(1000)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find!")

[x * x for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

girls = ['alice', 'bernice', 'clarice', 'beta']
boys = ['chris', 'arnold', 'bob', 'alpha']
[b+'+'+g for b in boys for g in girls if b[0] == g[0]]

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
[b+'+'+g for b in boys for g in letterGirls[b[0]]]

squares = {i: "{} squared is {}".format(i, i * i) for i in range(10)}
squares[8]  # '8 squared is 64'

if name == 'Stephen CUI':
    print('Welcome!')
elif name == 'Enid':
    pass
elif name == 'Bill Gates':
    print('Access denied!')

scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel
scoundrel  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
scoundrel = None
robin  # {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}

x = ['Hello', 'World']
y = x
y[1] = 'Python'
del x
y  # ['Hello', 'Python']

scope = {}
exec('sqrt = 1', scope)
sqrt(4)  # 2
scope['sqrt']  # 1

# eval(input('Enter an arithmetic expression: '))

scope = {}
scope['x'] = 2
scope['y'] = 3
eval('x * y', scope)  # 6

scope = {}
exec('x = 2', scope)
eval('x * x', scope)  # 4
