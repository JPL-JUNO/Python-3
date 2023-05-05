"""
@Description: Using Slicing to Extract Matching Substring Environments
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-05 10:58:25
"""

s = "Eat some fruits"
assert s[0:3] == "Eat"
assert s[3:0] == ""
assert s[:5] == "Eat s"
assert s[5:] == "ome fruits"
assert s[:100] == "Eat some fruits"
assert s[4:8:2] == "sm"
assert s[::3] == "E mfi"
assert s[::-1] == "stiurf emos taE"
assert s[6:1:-1] == "mos t"

letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''


def find(x, q): return x[x.find(q) - 18:x.find(q) + 18] if q in x else -1


find(letters_amazon, 'SQL') == "a fully-managed MySQL and PostgreSQL"
