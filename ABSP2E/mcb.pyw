"""
@File         : mcb.pyw
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-15 22:20:27
@Email        : cuixuanstephen@gmail.com
@Description  : 项目：多重剪贴板
"""

# .pyw 扩展名意味着 Python 在运行该程序时不会显示命令行窗口。

# 程序将利用一个关键字保存每段剪贴板文本。例如，当运行
# py mcb.pyw save spam 时，剪贴板中当前的内容就用关键字 spam 保存。
# 运行 py mcb.pyw spam，这段文本稍后将重新加载到剪贴板中。
# 如果用户忘记了都有哪些关键字，可以运行 py mcb.pyw list，将所有关键字
# 的列表复制到剪贴板中。
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open("mcb")

if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()
