"""
@Description: Using Generator Expressions to Find Companies That Pay Below Minimum Wage
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-06 09:53:39
"""

companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}}

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
assert illegal == ["CheapCompany", "SosoCompany"]
