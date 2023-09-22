"""
@Title: 序列运算
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 22:39:32
@Description: 
"""

from operator import concat, contains, countOf, getitem, setitem, delitem

a = [1, 2, 3]
b = ['a', 'b', 'c']

print("a = ", a)
print("b = ", b)

print("\nConstructive:")
print("  concat(a, b):", concat(a, b))

print("\nSearching:")
print("  contains(a, 1)  :", contains(a, 1))
print("  contains(b, 'd'):", contains(b, 'd'))
# Return the number of items in a which are, or which equal, b.
# 0 是没找到嘛？从 1 开始
print("  countOf(a, 1)   :", countOf(a, 1))
print("  countOf(a, 5)   :", countOf(a, 5))
print("  countOf(b, 'd') :", countOf(b, 'd'))

print("\nAccess Items:")
print("  getitem(b, 1):", getitem(b, 1))
print("  getitem(b, slice(1, 3)):", getitem(b, slice(1, 3)))
# 就地修改没有任何返回值
print("  setitem(b, 1, 'd')", setitem(b, 1, 'd'))
print(b)
print('  setitem(a, slice(1, 3), [4, 5]):', setitem(a, slice(1, 3), [4, 5]))
print(a)


print('\nDestructive:')
# 就地删除
print('  delitem(b, 1):', delitem(b, 1))
print(b)
print('  delitem(a, slice(1, 3)):', delitem(a, slice(1, 3)))
print(a)
