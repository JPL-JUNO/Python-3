"""
@Title: 可迭代对象与迭代器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-05 23:08:03
@Description: 
"""

s = "ABC"
for char in s:
    """这里，字符串 'ABC' 是可迭代的对象。
    背后是有迭代器的"""
    print(char)

print()
print("用 while 模拟 for 循环")
# 如果没有 for 循环，就不得不使用 while 循环模拟
it = iter(s)  # 根据可迭代对象构建迭代器 it
while True:
    try:
        print(next(it))  # 不断在迭代器上调用 next 函数，获取下一项
    except StopIteration:
        del it  # 释放对 it 的引用，即废弃迭代器对象
        break  # 退出循环
