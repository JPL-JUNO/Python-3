"""
@File         : update_db.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-28 20:17:14
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import shelve

db = shelve.open("person_db")
for key in sorted(db):
    print(key, "\t->", db[key])

sue = db["Sue Jones"]
sue.give_raise(0.1)
db["Sue Jones"] = sue
db.close()
