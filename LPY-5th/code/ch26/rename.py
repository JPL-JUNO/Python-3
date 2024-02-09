"""
@File         : rename.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-23 22:15:57
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import os

for file in os.listdir("./"):
    os.rename(file, file.lower().replace(" ", "_"))
