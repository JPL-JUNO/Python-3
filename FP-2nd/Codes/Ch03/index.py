"""
@Description: 使用dict.setdefault获取并更新词出现的位置
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-30 18:00:52
"""
import re

WORD_RE = re.compile(r'\w+')
index = {}

with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])


# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(new_value)
# 可以写成下面这样行，前一种写法至少要搜索两次key,没找到要搜索三次
# 但是下面这一行只需要搜索一次key
# my_dict.setdefault(key, []).append(new_value)
