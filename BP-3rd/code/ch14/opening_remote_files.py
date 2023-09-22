"""
@Description: 打开远程文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 15:05:16
"""

from urllib.request import urlopen
webpage = urlopen("http://www.python.org")

import re
text = webpage.read()
m = re.search(b'<a href="([^"]+)" .*?about</a>', text, re.IGNORECASE)
print(m.group(1))
