"""
@File         : ospath_split.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-22 22:32:40
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import os.path

PATHS = ["one/two/three", "/one/two/three/", "/", ".", ""]
for path in PATHS:
    print(f"{path!r:>17} : {os.path.split(path)}")
