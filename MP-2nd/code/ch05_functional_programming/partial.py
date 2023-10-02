"""
@Title: prefill function arguments
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-22 23:20:48
@Description: 
"""

import heapq

heap = []
# 比如说需要想 heap 中推入一个参数，但是每次都要写 heap
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 4)
heapq.nsmallest(3, heap)
# 我们可以定义一个函数不写参数，比如说


def push(*args, **kwargs):
    return heapq.heappush(heap, *args, **kwargs)


# 但是 Python 提供了一种新的方式
import functools

heap = []
push = functools.partial(heapq.heappush, heap)
# 把关键字参数传递给 heapq.nsmallest
smallest = functools.partial(heapq.nsmallest, iterable=heap)
push(1)
push(3)
push(5)
push(2)
push(4)
smallest(3)


def lambda_push(x): return heapq.heappush(heap, x)
# lambda_push = lambda x: heapq.heappush(heap, x)


print(heapq.heappush)
print(push)
print(lambda_push)

print(heapq.heappush.__doc__)
print(push.__doc__)
print(lambda_push.__doc__)
# <built-in function heappush>
# functools.partial(<built-in function heappush>, [1, 2, 5, 3, 4])
# <function <lambda> at 0x000001845B2C8180>
# Push item onto heap, maintaining the heap invariant.
# partial(func, *args, **keywords) - new function with partial application
#     of the given arguments and keywords.

# None
