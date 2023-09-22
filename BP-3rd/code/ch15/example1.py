"""
@Title: 屏幕抓取
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 13:16:25
@Description: 
"""

from urllib.request import urlopen
import re
p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = urlopen("http://python.org/jobs").read().decode()
for url, name in p.findall(text):
    print("{} ({})".format(name, url))
# 存在的缺点：
# 1. 正则表达式一点都不容易理解。
# 2. 它对付不了独特的HTML内容，如CDATA部分和字符实体（如&amp;）。
