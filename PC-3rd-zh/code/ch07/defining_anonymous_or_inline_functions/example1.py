"""
@Title: 定义匿名或内联函数
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 11:43:04
@Description: 
"""
# 不允许这样定义
# add = lambda x, y: x + y
def add(x, y): return x + y


add(2, 3)
add("hello", "world")

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
sorted(names, key=lambda name: name.split()[-1].lower())
