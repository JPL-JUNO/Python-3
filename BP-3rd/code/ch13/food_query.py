"""
@Description: 食品数据库查询程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 12:47:39
"""

import sqlite3
import sys
conn = sqlite3.connect("food.db")
curs = conn.cursor()
query = "SELECT * FROM food WHERE " + sys.argv[1]
print(query)
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}: {}'.format(*pair))
    print()
# 这个程序从用户那里获取输入，并将其插入到 SQL 查询中。在你是用户而且不会输入太不
# 可思议的内容时，这没有问题。然而，利用这种输入偷偷地插入恶意的 SQL 代码以破坏数
# 据库是一种常见的计算机攻击方式，称为 SQL 注入攻击。请不要让你的数据库（以及其他
# 任何东西）暴露在原始用户输入的“火力范围”内，除非你对这样做的后果心知肚明。
