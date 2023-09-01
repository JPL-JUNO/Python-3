"""
@Title: 在两个字典中寻找相同点 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 11:21:19
@Description: 
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# 如果需要对字典的键做常见的集合操作，那么就能直接使用 keys-view 对象而不必先将它们转化为集合。
a.keys() & b.keys()
a.keys() - b.keys()

# 字典的 items()方法返回由(key,value)对组成的 items-view 对象。
a.items() & b.items()

# 可用来修改或过滤掉字典中的内容
c = {key: a[key] for key in a.keys() - {"z", 'w'}}
