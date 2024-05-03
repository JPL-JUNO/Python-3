"""
@File         : create_file.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-02 14:46:10
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

sections = {"": []}


from pathlib import Path

for chapter, section in sections.items():
    code = Path("code") / chapter
    code.mkdir(parents=True, exist_ok=True)
    markdown = Path("notes") / chapter
    markdown.mkdir(parents=True, exist_ok=True)
    for s in section:
        with open(code / (s + ".py"), mode="w+", encoding="utf-8") as f:
            f.close()
        with open(markdown / (s + ".md"), mode="w+", encoding="utf-8") as f:
            f.close()
