"""
@Title: 与字典有关的计算问题
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 11:07:57
@Description: 
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# zip()创建了一个迭代器，它的内容只能被消费一次。
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# 如果尝试在字典上执行常见的数据操作，将会发现它们只会处理键，而不是值。
assert min(prices) == "AAPL"
assert max(prices) == "IBM"

# 可以利用字典的 values()方法来解决这个问题
assert min(prices.values()) == 10.75
assert max(prices.values()) == 612.78

# 如果提供一个 key 参数传递给 min()和 max()，就能得到最大值和最小值所对应的键是什么。
# 字典本身处理的是 key
assert min(prices, key=lambda k: prices[k]) == "FB"
assert max(prices, key=lambda k: prices[k]) == "AAPL"

min_value = prices[min(prices, key=lambda k: prices[k])]

# 利用了 zip()的解决方案是通过将字典的键-值对“反转”为值-键对序列来解决这个问题的。
# 当在这样的元组上执行比较操作时，值会先进行比较，然后才是键。
prices = {'AAA': 45.23, 'ZZZ': 45.23}
min(zip(prices.values(), prices.keys()))
