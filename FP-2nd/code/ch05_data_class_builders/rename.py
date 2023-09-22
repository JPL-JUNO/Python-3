"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 12:00:09
@Description: 
"""
import os

for file in os.listdir("./"):
    os.rename(file, file.lower().replace(" ", "_"))
