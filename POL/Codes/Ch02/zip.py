"""
@Description: Formatting Databases with the zip() Function
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-06 10:57:32
"""

lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
zipped = list(zip(lst_1, lst_2))
assert zipped == [(1, 4), (2, 5), (3, 6)]

lst_1_new, lst_2_new = zip(*zipped)
assert list(lst_1_new) == lst_1
assert list(lst_2_new) == lst_2


column_names = ["name", "salary", "job"]
db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'),
           ('Frank', 87000, 'CEO')]
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)

# print([list(row.values()) for row in db])
