spam = 1, 2, 3
eggs = 4, 5, 6
data = dict()
data[spam] = 'spam'
data[eggs] = 'eggs'

import pprint
pprint.pprint(data)


spam = 1, 'abd', (2, 3, (4, 5)), 'def'
eggs = 4, (spam, 5), 6
data = dict()
data[spam] = 'spam'
data[eggs] = 'eggs'
pprint.pprint(data)


a, b, c = 1, 2, 3
assert a == 1
spam = a, (b, c)
assert spam == (1, (2, 3))
a, b = spam
assert a == 1
assert b == (2, 3)

spam, *eggs = 1, 2, 3, 4
assert spam == 1
assert eggs == [2, 3, 4]
a, b, c = eggs
assert c == 4

spam, *eggs = range(10)
assert spam == 0
assert eggs == [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, *c = a, *eggs
assert (a, b) == (2, 1)
assert c == [2, 3, 4, 5, 6, 7, 8, 9]


def eggs(*args):
    print('args:', args)


eggs(1, 2, 3)


def spam_eggs():
    return 'spam', 'eggs'


spam, eggs = spam_eggs()
assert spam == 'spam'
assert eggs == 'eggs'
