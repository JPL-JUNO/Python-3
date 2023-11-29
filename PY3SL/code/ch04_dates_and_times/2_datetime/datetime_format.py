"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-11-29 21:16:20
@Description: 
"""

import datetime
today = datetime.datetime.today()

print('ISO:', today)
print('format(): {:%a %b %d %H:%M:%S %Y}'.format(today))
