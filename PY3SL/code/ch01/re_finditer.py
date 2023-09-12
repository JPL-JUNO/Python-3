"""
@Title: finditer()
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-12 09:57:32
@Description: 
"""

import re
text = "abbaaabbbaaaaa"

pattern = "ab"

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print("Found {!r} at {:d}:{:d}".format(text[s:e], s, e))
