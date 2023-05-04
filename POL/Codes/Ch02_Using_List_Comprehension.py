"""
@Description: Using List Comprehension to Find Top Earners 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-04 17:39:34
"""

employees = {'Alice': 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 88123,
             'Eve': 93121}
top_earners = []
for name, salary in employees.items():
    if salary >= 100_000:
        top_earners.append((name, salary))
assert top_earners == [('Alice', 100000), ('Carol', 122908)]

top_earners = [(k, v) for k, v in employees.items() if v >= 100_000]
assert top_earners == [('Alice', 100000), ('Carol', 122908)]

text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

w = [[x for x in line.split() if len(x) > 3] for line in text.split('\n')]
# print(w)
