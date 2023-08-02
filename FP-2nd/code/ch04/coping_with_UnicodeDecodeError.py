"""
@Description: 处理 UnicodeDecodeError 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-02 13:36:44
"""

octets = b'Montr\xe9al'
octets.decode('cp1252')
octets.decode('iso8859_7')
octets.decode('koi8_r')

try:
    octets.decode('utf_8')
except UnicodeDecodeError:
    print("The 'utf_8' codec detects that octets is not valid UTF-8, and raises UnicodeDecodeError.")

octets.decode('utf_8', errors='ignore')
# Using 'replace' error handling, the \xe9 is replaced by “�” (code point
# U+FFFD), the official Unicode REPLACEMENT CHARACTER intended to represent
# unknown characters.
