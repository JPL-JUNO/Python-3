"""
@Title: 一个简单的标记程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-05 15:06:10
@Description: 
"""

import sys
import re
from util import blocks

print("<html><head><title>...</title><body>")
title = True
for block in blocks(sys.stdin):
    block = re.sub(r"\*(.+?)\*", r"<em>\1</em>", block)
    if title:
        print("<h1>")
        print(block, end='')
        print("</h1>")
        title = False
    else:
        print("<p>")
        print(block, end='')
        print("</p>")
print("</body></html>")
