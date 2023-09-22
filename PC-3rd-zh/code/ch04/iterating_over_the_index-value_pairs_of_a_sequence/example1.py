"""
@Title: 以索引-值对的形式迭代序列
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 10:23:18
@Description: 
"""

my_list = ['A', 'B', 'C']
for idx, val in enumerate(my_list):
    print(idx, val)
# 0 A
# 1 B
# 2 C

for idx, val in enumerate(my_list, 1):
    print(idx, val)
# 1 A
# 2 B
# 3 C


def parse_data(file_name):
    with open(file_name, "rt") as f:
        for line_no, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[0])
            except ValueError as e:
                print("Line {}: Parse error: {}".format(line_no, e))


# 可以找到每个单词出现的行号
# Fluent Python 中也有，来展示 defaultdict
from collections import defaultdict
word_summary = defaultdict(list)
with open("my_file.txt", "r") as f:
    lines = f.readlines()
for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
