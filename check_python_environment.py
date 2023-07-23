"""
@Description: 检查 python 环境和包配置
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-23 23:14:42
"""

import sys
import platform
from packaging import version
python_ver = platform.python_version()
if version.parse(python_ver) < version.parse('3.9'):
    print(
        f'[FAIL] We recommend Python 3.9 or later but found version {sys.version}')
else:
    print(f'[OK] Your Python Version is {sys.version}')

if __name__ == '__main__':
    pass
