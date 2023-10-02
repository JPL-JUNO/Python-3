"""
@Title: 批量处理文件命名，非递归查找
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 00:03:11
@Description: 
"""
import os

for file in os.listdir():
    os.rename(file, file.lower().replace(" ", "_"))
