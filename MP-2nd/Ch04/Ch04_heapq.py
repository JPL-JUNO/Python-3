"""
@Description: Sorting collections using heapq
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-07 12:52:08
"""

import heapq

# sorted as a tree
heap = [1, 3, 5, 7, 2, 4, 3]
heapq.heapify(heap)
print(heap)

while heap:
    print(heapq.heappop(heap), heap)


def heapsort(iterable):
    heap = []
    # O(n*log(n))
    for value in iterable:
        heapq.heappush(heap, value)

    while heap:
        # O(log(n))
        yield heapq.heappop(heap)
