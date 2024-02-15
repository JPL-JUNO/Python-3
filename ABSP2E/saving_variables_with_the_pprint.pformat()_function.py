"""
@File         : saving_variables_with_the_pprint.pformat()_function.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-15 18:52:40
@Email        : cuixuanstephen@gmail.com
@Description  : 用 pprint.pformat()函数保存变量
"""

import pprint

cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
pprint.pformat(cats)
file_obj = open("my_cats.py", "w")
file_obj.write("cats = " + pprint.pformat(cats) + "\n")
file_obj.close()

import my_cats

my_cats.cats
my_cats.cats[0]
my_cats.cats[0]["name"]
