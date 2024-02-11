"""
@File         : platforms_and_versions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-11 12:53:04
@Email        : cuixuanstephen@gmail.com
@Description  : 平台和版本
"""

import sys

print(sys.platform, sys.maxsize, sys.version)
if sys.platform[:3] == "win":
    print("Hello Windows")
