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
