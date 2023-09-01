"""
@Title: 筛选序列中的元素
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:48:46
@Description: 
"""

my_list = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in my_list if n > 0]

[n for n in my_list if n < 0]

pos = (n for n in my_list if n > 0)
pos
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


i_vals = list(filter(is_int, values))
print(i_vals)


clip_neg = [n if n > 0 else 0 for n in my_list]
clip_neg
clip_pos = [n if n < 0 else 0 for n in my_list]
clip_pos
