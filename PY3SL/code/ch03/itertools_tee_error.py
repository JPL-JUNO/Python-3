"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:45:00
@Description: 创建的新迭代器会共享器输入迭代器，所有创建了新迭代器后，不应再使用原迭代器
"""

from itertools import count, islice, tee
r = islice(count(), 5)
i1, i2 = tee(r)

print("r:", end=' ')
for i in r:
    print(i, end=' ')
    if i > 1:
        break
print()
# If values are consumed from the original input,
# the new iterators will not produce those values.
print('i1:', list(i1))
for i in i1:
    print(i, end=' ')
print('i2:', list(i2))

# ❌
# for i in r:
#     print(i, end=' ')
