"""
@Description: 获取远程文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 15:10:29
"""

from urllib.request import urlretrieve
urlretrieve("http://www.python.org", './python_webpage.html')
