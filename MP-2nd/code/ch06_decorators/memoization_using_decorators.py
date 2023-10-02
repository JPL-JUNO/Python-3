"""
@Title: 使用装饰器记忆
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 00:04:25
@Description: 
"""

import functools


def memoize(function):
    # Store the cache as attribute of the function so we can
    # apply the decorator to multiple functions without
    # sharing the cache
    function.cache = dict()

    @functools.wraps(function)
    def _memoize(*args):
        # if the cache is not available, call the function
        # Note that all args need to be hashable
        if args not in function.cache:
            # 因为不知道 function(*args) 的类型，
            # 不能使用 collections.defaultdict(factory_functions)
            function.cache[args] = function(*args)
        return function.cache[args]
    return _memoize


@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 7):
    print(f"Fibonacci {i}: {fibonacci(i)}")

fibonacci.__wrapped__.cache

try:
    fibonacci(n=2)
except TypeError as err:
    print(err)
    print("It breaks keyword arguments")

try:
    fibonacci([123])
except TypeError as err:
    print(err)
    print("Unhashable types don't work as dict keys:")


# Create a simple call counting decorator
def counter(function):
    function.calls = 0

    @functools.wraps(function)
    def _counter(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)
    return _counter

# lru_cache stand for least recently used cache
# when calling fibonacci the execution order is as follows:
# 1. functools.lru_cache
# 2. counter
# 3. fibonacci


@functools.lru_cache(maxsize=3)
@counter
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# fibonacci = functools.lru_cache(counter(fibonacci))
# returning the values works in the reverse order
# of course, fibonacci returns its value to counter
# which passes the value along to lru_cache


assert fibonacci(100) == 354224848179261915075
fibonacci.cache_info()
assert fibonacci.__wrapped__.__wrapped__.calls == 101
# that's because we recursively require only n-1 and n-2
# so we have no need for a larger cache in this cache
