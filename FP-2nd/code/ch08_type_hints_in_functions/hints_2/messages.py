"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 11:54:10
@Description: 
"""


def show_count(count: int, singular: str, plural: str = "") -> str:
    if count == 1:
        return f"1 {singular}"
    count_str = str(count) if count else "no"
    if not plural:
        plural = plural + 's'
    return f"{count_str} {plural}"
