"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 21:06:14
@Description: 
"""
import os
for file in os.listdir():
    os.rename(file, file.lower().replace(" ", "_"))
