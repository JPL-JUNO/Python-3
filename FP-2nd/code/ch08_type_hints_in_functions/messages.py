"""
@Title: show_count from messages.py without type hints
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 11:32:24
@Description: 
"""


def show_count(count: int, word: str) -> str:
    if count == 1:
        return f"1 {word}"

    count_str = str(count) if count else "no"
    return f"{count_str} {word}s"

# If a function signature has no annotations, Mypy ignores it by default—unless
# configured otherwise.
