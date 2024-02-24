"""
@File         : saving_variables_with_the_shelve_module.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-15 14:31:28
@Email        : cuixuanstephen@gmail.com
@Description  : 用 shelve 模块保存变量
"""

import shelve

shelf_file = shelve.open("my_data")
cats = ["Zophie", "Pooka", "Simon"]
shelf_file["cats"] = cats
shelf_file.close()

shelf_file = shelve.open("my_data")
type(shelf_file)
shelf_file["cats"]
shelf_file.close()

shelf_file = shelve.open("my_data")
list(shelf_file.keys())
list(shelf_file.values())
shelf_file.close()
