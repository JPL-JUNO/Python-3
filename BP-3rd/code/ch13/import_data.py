"""
@Description: 数据库应用程序示例
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 11:28:38
"""
import sqlite3


def convert(value):
    # 原本的数据集 文本型两侧有~，去掉，不同字段使用^分隔
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)


conn = sqlite3.connect("food.db")
curs = conn.cursor()

curs.execute("""
CREATE TABLE food (
    id TEXT PRIMARY KEY,
    desc TEXT,
    water FLOAT,
    kcal FLOAT,
    protein FLOAT,
    fat FLOAT,
    ash FLOAT,
    carbs FLOAT,
    fiber FLOAT,
    sugar FLOAT
)
""")
# 使用的参数风格为 qmark，即使用问号来标记字段。
query = "INSERT INTO food VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
field_count = 10
for line in open("ABBREV.txt"):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)
conn.commit()
conn.close()
