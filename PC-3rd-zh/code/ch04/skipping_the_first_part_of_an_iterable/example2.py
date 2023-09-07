"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 09:43:59
@Description: dropwhile()和 islice()都是很方便实用的函数，可以利用它们来避免写出如下所示的混乱代码
"""

# ❌
with open("./passwd.txt") as f:
    # skip over initial comments
    while True:
        # 跳过了前面以 # 开头的行
        line = next(f, "")
        if not line.startswith("#"):
            break
    # process remaining lines
    # 这里是迭代器没有处理完，还能继续迭代
    # 如果下一行不是空行(没有任何显式字符的字符串的行仍然有一个换行符)
    while line:
        # replace with useful processing
        print(line, end='')
        line = next(f, None)


# ✅
with open("./passwd.txt") as f:
    # 生成器
    lines = (line for line in f if not line.startswith("#"))
    for line in lines:
        print(line, end='')
# 这么做显然会丢弃开始部分的注释行，但这同样会丢弃整个文件中出现的所有注释行。
# 而 example1.py 开始给出的解决方案只会丢弃元素，直到有某个元素不满足测试函数为止。那
# 之后的所有剩余元素全部会不经过筛选而直接返回。
