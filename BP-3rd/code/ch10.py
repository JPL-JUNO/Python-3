# import sys
# import pprint
# # pprint.pprint(sys.path)
# # sys.path.append('C:/Notes/Beginning-Python/Codes')
# pprint.pprint(sys.path)

# import copy
# [n for n in dir(copy) if not n.startswith('_')]
# # ['Error', 'copy', 'deepcopy', 'dispatch_table', 'error']

# copy.__all__  # ['Error', 'copy', 'deepcopy']

# from copy import *
# import copy
# from copy import dispatch_table
# copy.dispatch_table

# help(copy.copy)
# Help on function copy in module copy:

# copy(x)
#     Shallow copy operation on arbitrary Python objects.

#     See the module's __doc__ string for more info.

# print(copy.copy.__doc__)
# Shallow copy operation on arbitrary Python objects.

#     See the module's __doc__ string for more info.

# print(range.__doc__)
# range(stop) -> range object
# range(start, stop[, step]) -> range object

# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
# start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements.
# When step is given, it specifies the increment (or decrement).

# print(copy.__file__)
# d:\Python3.11.1\Lib\copy.py

# import webbrowser
# webbrowser.open('http://www.python.org')

# python some_script.py file1.txt file2.txt file3.txt


import shelve
from pprint import pprint
from random import randrange
from time import *
from random import *
import time
from collections import deque
from random import shuffle
from heapq import *
set(range(10))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

type({})  # dict

{0, 1, 2, 3, 0, 1, 2, 3, 4, 5}
# {0, 1, 2, 3, 4, 5}

a = {1, 2, 3}
b = {2, 3, 4}
a.union(b)  # {1, 2, 3, 4}
a | b  # {1, 2, 3, 4}

c = a & b
c.issubset(a)  # True
c <= a  # True

c.issuperset(a)  # False
c >= a  # False

a.intersection(b)  # {2, 3}
a & b  # {2, 3}
a.difference(b)  # {1}
a - b  # {1}

# A | B - A & B
a.symmetric_difference(b)  # {1, 4}
a ^ b  # {1, 4}
a.copy()  # {1, 2, 3}
a.copy() is a  # False

my_sets = []
for i in range(10):
    my_sets.append(set(range(i, i + 5)))
my_sets
# reduce(set.union, my_sets)

a = set()
b = set()
# a.add(b)  # TypeError: unhashable type: 'set'
a.add(frozenset(b))
a  # {frozenset()}

data = list(range(10))
shuffle(data)
data
heap = []
for n in data:
    heappush(heap, n)

heappush(heap, .5)
heap  # [0, 0.5, 1, 5, 3, 2, 6, 8, 7, 9, 4]

heappop(heap)  # 0
heappop(heap)  # 0.5
heappop(heap)  # 1
heap  # [2, 4, 3, 5, 6, 7, 8, 9]

heap = [5, 8, 0, 3, 6, 7, 9, 1, 4, 2]
heapify(heap)
heap  # [0, 1, 5, 3, 2, 7, 9, 8, 4, 6]

heapreplace(heap, .5)
heap  # [0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
heapreplace(heap, 10)
heap  # [1, 2, 5, 3, 6, 7, 9, 8, 4, 10]

data = list(range(1000))
shuffle(data)
nlargest(5, data)  # [999, 998, 997, 996, 995]
nsmallest(5, data)  # [0, 1, 2, 3, 4]

q = deque(range(5))
q.append(5)
q.appendleft(6)
q  # deque([6, 0, 1, 2, 3, 4, 5])
q.pop()  # 5
q.popleft()  # 6
q.rotate(3)
q  # deque([2, 3, 4, 0, 1])

q.rotate(-1)
q  # deque([3, 4, 0, 1, 2])


q.extend([1, 2])
# deque([3, 4, 0, 1, 2, 1, 2])
q.extendleft([1, 2])
q  # deque([2, 1, 3, 4, 0, 1, 2, 1, 2])

time.asctime()  # 'Sat Feb 18 17:32:01 2023'

date1 = (2023, 1, 1, 0, 0, 0, -1, -1, -1)
date2 = (2023, 12, 31, 23, 59, 59, -1, -1, -1)
time1 = mktime(date1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print(asctime(localtime(random_time)))
# Tue Oct 17 09:08:16 2023

# num = int(input("How many dice?"))
# sides = int(input("How many sides per die?"))
# sum = 0
# for i in range(num):


#     sum += randrange(sides) + 1
# print('The result is', sum)
# How many dice? 3
# How many sides per die? 6
# The result is 13

# values = list(range(1, 11)) + 'Jack Queen King'.split()
# suits = 'diamonds clubs hearts spades'.split()
# deck = ['{} of {}'.format(v, s) for v in values for s in suits]
# shuffle(deck)
# while deck:
#     ignore = input(deck.pop())


s = shelve.open('test')
s['x'] = ['a', 'b', 'c']
temp = s['x']
temp.append('d')
s['x'] = temp
s['x']
