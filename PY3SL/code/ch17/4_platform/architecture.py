"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-21 16:36:16
@Description: 
"""

import platform
print('interpreter:', platform.architecture())
print('/bin/ls    :', platform.architecture('/bin/ls'))
