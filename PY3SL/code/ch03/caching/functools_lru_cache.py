"""
@Title: 缓存
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-21 20:42:48
@Description: 
"""

import functools
from itertools import product


@functools.lru_cache
def expensive(a, b):
    print("expensive({}, {})".format(a, b))
    return a * b


MAX = 2
print("First set of calls:")
# for i in range(MAX):
#     for j in range(MAX):
#         expensive(i, j)
for (i, j) in product(range(MAX), repeat=2):
    expensive(i, j)
print(expensive.cache_info())

# 有相同的参数值，结果在缓存中
print("\nSecond set of calls:")
for (i, j) in product(range(MAX + 1), repeat=2):
    expensive(i, j)
print(expensive.cache_info())

print("\nThird set of calls:")
for (i, j) in product(range(MAX), repeat=2):
    expensive(i, j)
print(expensive.cache_info())
print()


# 为了避免一个长时间运行的进程导致缓存无限制地扩张
# 要指定一个大小，默认是 128 个元素
# 不过对于每个缓存可以使用 maxsize 参数改变这个大小
@functools.lru_cache(maxsize=2)
def expensive(a, b):
    print("called expensive({}, {})".format(a, b))
    return a * b


def make_call(a, b):
    print("({}, {})".format(a, b), end=" ")
    pre_hits = expensive.cache_info().hits
    expensive(a, b)
    post_hits = expensive.cache_info().hits
    if post_hits > pre_hits:
        print("cache hit")


print("Establish the cache")
make_call(1, 2)
make_call(2, 3)

print("\nUse cached items")
make_call(1, 2)
make_call(2, 3)

print("\nCompute a new value, triggering cache expiration")
# 缓存中最老的元素取代
make_call(3, 4)

print("\nCache still contains one old item")
make_call(2, 3)

print("\nOldest item need to be recomputed")
make_call(1, 2)
print()

# lru_cache() 管理的缓存中的键必须是可以 hashable
# 所以对于用缓存查找包装的函数，它的所有参数都必须是 hashable
make_call(1, 2)

try:
    make_call([1], 2)
except TypeError as err:
    print("ERROR: {}".format(err))

try:
    make_call(1, {'2': 'two'})
except TypeError as err:
    print("ERROR: {}".format(err))
