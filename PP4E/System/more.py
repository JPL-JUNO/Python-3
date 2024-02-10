"""
@File         : more.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-10 23:39:04
@Email        : cuixuanstephen@gmail.com
@Description  : 分割字符串或文本并交互地进行分页
"""


def more(text, num_lines=15):
    # 返回一个在换行符处分割后得到的子字符串组成的列表
    lines = text.splitlines()  # like split('\n') but no '' at end
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print(line)
        if lines and input("More?") not in ["y", "Y"]:
            break


if __name__ == "__main__":
    import sys

    more(open(sys.argv[1]).read(), 10)
