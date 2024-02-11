>>> line = 'aaa\nbbb\nccc\n'
>>> line.split('\n')
['aaa', 'bbb', 'ccc', '']
>>> line.splitlines()
['aaa', 'bbb', 'ccc']


D:\...\PP4E\System>python more.py more.py
"""
@File         : more.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-10 23:39:04
@Email        : cuixuanstephen@gmail.com
@Description  : 分割字符串或文本并交互地进行分页
"""

>>> from more import more
>>> import sys
>>> more(sys.__doc__)
>>>