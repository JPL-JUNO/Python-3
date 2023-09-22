"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 10:59:46
@Description: 
"""
from datetime import date
d = date(2023, 8, 31)
format(d)
format(d, "%A, %B, %d, %Y")
"The end is {:%d %b %Y}. Goodbye".format(d)
