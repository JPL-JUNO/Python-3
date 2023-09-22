"""
@Title: 使用Beautiful Soup的屏幕抓取程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 15:26:30
@Description: 
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

text = urlopen("http://python.org/jobs").read()
soup = BeautifulSoup(text, "html.parser")

jobs = set()
for job in soup.body.section("h2"):
    # 每个 h2 元素都表示一个职位
    # 我们感兴趣的是它包含的第一个连接 job.a
    # 属性 string 是链接的文本内容
    jobs.add("{} ({})".format(job.a.string, job.a["href"]))
print("\n".join(sorted(jobs, key=str.lower)))
