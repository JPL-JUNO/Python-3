"""
@File         : list_overallocation.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-02 14:45:05
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from itertools import islice
import matplotlib.pyplot as plt


def overalloc_dict():
    o = list_overalloc()
    i = 1
    s, e, _ = next(o)
    while True:
        if i > e:
            s, e, _ = next(o)
        # 计算多余的数字
        yield e - i
        i += 1


def list_overalloc():
    s = 1
    while True:
        e = alloc = s + overalloc(s)
        yield s, e, alloc
        s = e + 1


overalloc = lambda N: (N >> 3) + (3 if N < 9 else 6)
plt.scatter(
    list(range(1, 10000)),
    list(islice(overalloc_dict(), 10000 - 1)),
    marker=".",
    s=1,
)
plt.ylim(0, 10000 - 1)
plt.xlim(0, 10000 - 1)
plt.ylim(0, 2000)
plt.ylim(0, 1500)
plt.ylim(0, 1400)
plt.ylim(0, 1300)
plt.xlabel("Size of the list")
plt.ylabel("Number of elements overallocated")
plt.grid()
plt.title("Overallocation in lists")
plt.savefig("figure/list_overallocation.png")
