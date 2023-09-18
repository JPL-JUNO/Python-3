"""
@Title: 批量重命名文件
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 11:20:45
@Description: 
"""

import os

for file in os.listdir('./'):
    os.rename(file, file.lower().replace(" ", "_"))
