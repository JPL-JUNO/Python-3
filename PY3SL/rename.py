"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-11 14:53:59
@Description: 
"""
import os
for file in os.listdir('./'):
    os.rename(file, file.lower().replace(' ', '_'))
