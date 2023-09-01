"""
@Title: 同时对数据做转换和换算
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 16:01:41
@Description: 
"""

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

import os
files = os.listdir("./")
if any(name.endswith(".py") for name in files):
    print("There be python!")
else:
    print("Sorry, no Python.")

s = ("ACME", 50, 123.45)
print(",".join(str(x) for x in s))

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

# 不必重复使用括号）。比如，下面这两行代码表示的是同一个意思：
s = sum((x * x for x in nums))
s = sum(x * x for x in nums)

# 但这引入了一个额外的步骤而且创建了额外的列表。
# 如果 nums 非常巨大，那么就会创建一个庞大的临时数
# 据结构，而且只用一次就要丢弃。基于生成器的解决方案可以以迭代的方式转换数据，
# 因此在内存使用上要高效得多。
s = sum([x * x for x in nums])

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda x: x['shares'])
