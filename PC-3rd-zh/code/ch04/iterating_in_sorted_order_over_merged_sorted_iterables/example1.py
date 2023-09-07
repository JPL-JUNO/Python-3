"""
@Title: 合并多个有序序列，再对整个有序序列进行迭代
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 10:06:44
@Description: 
"""

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# heapq.merge 的迭代性质意味着它对所有提供的序列都不会做一次性读取。这意味着可
# 以利用它处理非常长的序列，而开销却非常小。

with open("sorted_file_1", "rt") as file1, \
    open("sorted_file_2", "rt") as file2, \
        open("merged_file", "wt") as out_file:
    for line in heapq.merge(file1, file2):
        out_file.write(line)
# 需要重点强调的是，heapq.merge()要求所有的输入序列都是有序的。特别是，它不会首
# 先将所有的数据读取到堆中，或者预先做任何的排序操作。它也不会对输入做任何验
# 证，以检查它们是否满足有序的要求。相反，它只是简单地检查每个输入序列中的第
# 一个元素，将最小的那个发送出去。然后再从之前选择的序列中读取一个新的元素，
# 再重复执行这个步骤，直到所有的输入序列都耗尽为止。
