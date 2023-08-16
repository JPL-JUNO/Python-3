from functools import reduce
import math
fibs = [0, 1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
fibs  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

fibs = [0, 1]
# num = int(input("How many Fibonacci numbers da you want?"))
for i in range(num-2):
    fibs.append(fibs[-2] + fibs[-1])
fibs

x = 1
y = math.sqrt
callable(x)  # False
callable(y)  # True


def hello(name):
    return 'Hello, ' + name + '!'


hello('World')  # 'Hello, World!'
hello('Gumby')  # 'Hello, Gumby!'


def square(x):
    'Calculate the square of the number x'
    return x * x


square.__doc__
# 'Calculate the square of the number x'

help(square)
# Help on function square in module __main__:

# square(x)
#     Calculate the square of the number x


def test():
    print('This is a demo')
    return
    print('This is not')


x = test()  # This is a demo
print(x)  # None


def try_to_change(n):
    n = 'Mr. Gumby'


name = 'Mrs. Entity'
try_to_change(name)
name  # 'Mrs. Entity'

name = 'Mrs. Entity'
n = name
n = 'Mr. Gumby'
name  # 'Mrs. Entity'


def change(n):
    n[0] = 'Mr. Gumby'


names = ['Mes. Entity', 'Mrs. Thing']
change(names)
names  # ['Mr. Gumby', 'Mrs. Thing']

names = ['Mes. Entity', 'Mrs. Thing']
n = names
n[0] = 'Mr. Gumby'
names  # ['Mr. Gumby', 'Mrs. Thing']

names = ['Mes. Entity', 'Mrs. Thing']
n = names[:]
n is names  # False
n == names  # True


def change(n):
    n[0] = 'Mr. Gumby'


names = ['Mrs. Entity', 'Mrs. Thing']
change(names[:])
names  # ['Mrs. Entity', 'Mrs. Thing']


def inc(x): return x + 1


foo = 10
foo = inc(foo)
foo  # 11


def inc(x): x[0] += 1


foo = [10]
inc(foo)
foo  # [11]


def hello(greeting, name):
    print('{}, {}!'.format(greeting, name))


hello('Hello', 'Python')  # Hello, Python!


def hello(greeting='Hello', name='World'):
    print('{}, {}!'.format(greeting, name))


def print_params(*params):
    print(params)


print_params('Testing')  # ('Testing',)


def print_params_2(title, *params):
    print(title)
    print(params)


print_params_2('Title', 1, 2, 3)
# Title
# (1, 2, 3)

print_params_2('Noting: ')
# Noting:
# ()


def in_the_middle(x, *y, z):
    print(x, ',', y, ',', z)


in_the_middle(1, 2, 3, 4, 6, 7, z=3)  # 1 , (2, 3, 4, 6, 7) , 3
# in_the_middle(1, 2, 3, 4, 5)
# in_the_middle() missing 1 required keyword-only argument: 'z'


# print_params_2('Hmm...', something=42)
# print_params_2() got an unexpected keyword argument 'something'

def print_params_3(**params):
    print(params)


print_params_3(x=1, y=2, z=3)  # {'x': 1, 'y': 2, 'z': 3}


def print_params_4(x, y, *pos_params, z=1, **key_params):
    print(x, y, z)
    print(pos_params)
    print(key_params)


print_params_4(1, 2, 7, 11, z=3, foo=5, bar=13)
# 1 2 3
# (7, 11)
# {'foo': 5, 'bar': 13}


def hello_3(name='CUI', greeting='Hello'):
    print('{}, {}'.format(greeting, name))


params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)  # Well met, Sir Robin


# def foo(x, y, z, m=0, n=0):
#     print(x, y, z, m, n)


# def call_foo(*args, **kwds):
#     print(args)
#     print(kwds)
#     print("Calling foo")
#     foo(*args, **kwds)


# call_foo(1, 2, 3)


def story(**kwds):
    return 'Once upon a time, there was a '\
        '{job} called {name}.'.format_map(kwds)


def power(x, y, *others):
    if others:
        print('Received redundant parameters: ', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result


print(story(job='king', name='Gumby'))
# Once upon a time, there was a king called Gumby.
print(story(name='Sir Robin', job='brave knight'))
# Once upon a time, there was a brave knight called Sir Robin.
params = {'job': 'language', 'name': 'Python'}
print(story(**params))
# Once upon a time, there was a language called Python
del params['job']
print(story(job='stroke of genius', **params))
# Once upon a time, there was a stroke of genius called Python.
power(2, 3)  # 8
power(3, 2)  # 9
power(y=3, x=2)  # 8
params = (5, ) * 2
power(*params)
power(3, 3, 'Hello, world!')
# Received redundant parameters:  ('Hello, world!',)
# 27
interval(10)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interval(1, 5)  # [1, 2, 3, 4]
interval(3, 12, 4)  # [3, 7, 11]
power(*interval(3, 7))
# Received redundant parameters:  (5, 6)
# 81

x = 1
scope = vars()
scope['x']
scope['x'] += 1
x  # 2


def foo(): x = 42


x = 1
foo()
x  # 1


def combine(parameter): print(parameter + external)


external = 'berry'
combine('Shrub')  # Shrubberry


def combine(parameter):
    print(parameter + globals()['parameter'])


parameter = 'berry'
combine('Shrub')

x = 1


def change_global():
    global x
    x += 1


change_global()
x  # 2


def multiplier(factor):
    def multiplierByFactor(number):
        return number * factor
    return multiplierByFactor


double = multiplier(2)
double(5)  # 10
triple = multiplier(3)
triple(3)  # 9
multiplier(5)(4)  # 20


def recursion():
    return recursion()


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


power(2, 10)  # 1024


def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (upper + lower) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
search(seq, 34)  # 2
search(seq, 100)  # 5

list(map(str, range(10)))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
[str(i) for i in range(10)]


def func(x):
    return x.isalnum()


seq = ['foo', 'bar', 'x41', '***', '?!']
list(filter(func, seq))  # ['foo', 'bar', 'x41']

[x for x in seq if x.isalnum()]

list(filter(lambda x: x.isalnum(), seq))

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
reduce(lambda x, y: x + y, numbers)  # 1161
