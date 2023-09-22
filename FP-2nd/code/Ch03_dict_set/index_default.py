"""
@Description: 使用defaultdict替代setdefault
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-30 18:12:34
"""

import re
from collections import defaultdict
WORD_RE = re.compile(r'\w+')

index = defaultdict(list)
with open('zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 如果index中当前没有word键，调用default_factory生成缺失的值
            # 这里生成一个空列表，赋值给index[word]，然后返回空列表
            index[word].append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
