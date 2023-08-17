"""
@Description: 起步
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 11:04:44
"""

import sqlite3
# 创建到数据库文件的连接，只需要提供一个文件名，如果不存在将自动创建它
conn = sqlite3.connect("somedatabase.db")
# 从连接获得游标，使用这个游标可以来执行查询
curs = conn.cursor()
# 执行完查询后，如果修改了数据，务必提交所做的修改，这样才会将其保存到文件中
conn.commit()
# 要关闭连接，只需调用方法 close
conn.close()
