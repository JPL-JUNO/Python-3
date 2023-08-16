"""
@Description: 使用文件的基本方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-16 22:20:14
"""

# 首先是 read(n)
f = open('basic_file.txt')
assert f.read(7) == "Welcome"
assert f.read(4) == " to "
f.close()

# 首先是 read(n)
f = open('basic_file.txt')
print(f.read())
f.close()

# 下面是 readline()：
f = open('basic_file.txt')
for i in range(3):
    # 好像 print 会自动换行，end 指的是下一行的首个输出？
    print(str(i) + ": " + f.readline(), end='')
f.close()

# 最后是 readlines()：
import pprint
print()
pprint.pprint(open(r"basic_file.txt").readlines())
# 请注意，这里我利用了文件对象将被自动关闭这一事实

# 尝试写入
f = open(r"basic_file.txt")
lines = f.readlines()
f.close()
lines[1] = "isn't a\n"
f = open(r"basic_file.txt", 'w')
f.writelines(lines)
f.close()
