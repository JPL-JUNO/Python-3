"""
@Title: 从序列中移除重复项且保持元素间顺序不变
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 11:34:10
@Description: 
"""


def dedupe_hash(items):
    # 如果序列中的值是可哈希（hashable）的，那么这个问题可以通过使用集合和生成器轻松解决。
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
dedupe_hash(a)


def dedupe_no_hash(items, key=None):
    # 参数 key 的作用是指定一个函数用来将序列中的元素转换为可哈希的类型
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
dedupe_no_hash(a, key=lambda d: (d['x'], d['y']))
dedupe_no_hash(a, key=lambda d: d['x'])
