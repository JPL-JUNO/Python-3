"""
@Description: 使用dict.get获取并更新词出现的位置列表
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-30 17:43:16
"""

import re

WORD_RE = re.compile(r'\w+')
index = {}

with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            # 这里是获取单词
            word = match.group()
            # 获取单词所在的列号
            column_no = match.start()+1
            location = (line_no, column_no)
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            
for word in sorted(index, key=str.upper):
    print(word, index[word])
        