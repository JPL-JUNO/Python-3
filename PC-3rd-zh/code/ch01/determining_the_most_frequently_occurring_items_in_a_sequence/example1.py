"""
@Title: 找出序列中出现次数最多的元素
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:03:25
@Description: 
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]

# 如果想手动增加计数，只需简单地自增即可
more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

for word in more_words:
    word_counts[word] += 1
assert word_counts["eyes"] == 9

word_counts.update(more_words)

a = Counter(words)
b = Counter(more_words)
# key 并起来，相同 key 计数增加，不同的 key 并集
c = a + b
# 差集，相同的 key 做减法，为 0 的 key 删除
d = a - b
