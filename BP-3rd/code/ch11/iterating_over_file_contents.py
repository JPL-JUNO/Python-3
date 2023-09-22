"""
@Description: 迭代文件内容
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 09:18:46
"""


def process(string):
    print("Processing:", string)


# 每次一个字符（或字节）
with open("somefile.txt", "r") as f:
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)
# 这个程序之所以可行，是因为到达文件末尾时，方法read将返回一个空字符串，但在此之前，
# 返回的字符串都只包含一个字符（对应于布尔值True）。只要char为True，你就知道还没结束。

# 因为上面的代码段有重复行，因此改为下面这种更优的写法
with open("somefile.txt", "r") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)

# 每次一行
with open("basic_file.txt", 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        # 每个 line 后面都有一个 \n，除了最后一行，因此换两次行
        process(line)

with open("basic_file.txt", 'r') as f:
    # f.read() 返回的是一个 str，因此 for 迭代没问题
    for char in f.read():
        process(char)

with open("basic_file.txt", 'r') as f:
    # f.readlines() 返回的是一个 list[str]
    for line in f.readlines():
        process(line)

# 使用 fileinput 实现延迟行迭代
import fileinput
for line in fileinput.input("basic_file.txt"):
    process(line)

# 文件迭代器
with open("basic_file.txt", 'r') as f:
    for line in f:
        process(line)
# 请注意，与其他文件一样，sys.stdin也是可迭代的，因此要迭代标准输入中的所有行.
# import sys
# for line in sys.stdin:
    # process(line)
f = open("somefile.txt", 'w')
# 使用了print来写入文件，这将自动在提供的字符串后面添加换行符。
print("first", "line", file=f)
print("Second", "line", file=f)
print("Third", "and final", "line", file=f)
f.close()
lines = list(open("somefile.txt"))
print(lines)
# 对打开的文件进行序列解包，从而将每行存储到不同的变量中。
# （这种做法不常见，因为通常不知道文件包含多少行，但这演示了文件对象是可迭代的。）
first, second, third = open("somefile.txt")
print(first)
print(second)
print(third)
