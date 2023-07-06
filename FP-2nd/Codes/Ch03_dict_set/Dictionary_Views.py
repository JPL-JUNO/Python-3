"""
@Description: Dictionary Views
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-06 13:12:10
"""

d = dict(a=10, b=20, c=30)
values = d.values()
print(values)

# 可以查询视图的长度
assert len(values) == 3

# 视图是可迭代对象，方便构建列表
list(values)

# 视图实现了__reverse__方法，返回一个自定义迭代器
reversed(values)

try:
    # 不能使用[]获取视图中的项
    print(values[0])
except TypeError as e:
    print(e)


d['z'] = 99
print(d)
# 动态代理
print(values)

values_class = type({}.values())
print(values_class)
try:
    # dict_values, dict_keys, dict_items是内部类
    # 可以得到实例，但是不能自己手动创建
    v = values_class()
except TypeError as e:
    print(e)
