"""
@Title: 统一修改文件夹名称
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 16:29:27
@Description: 
"""
import os
import sys
sys.path.append("./")

for folder in os.listdir("../ch01"):
    os.rename(folder, folder.replace(" ", "_").lower())
