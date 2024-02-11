"""
@File         : common_os.path_tools.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-11 19:23:31
@Email        : cuixuanstephen@gmail.com
@Description  : 常见 os.path 工具
"""

import os

os.path.isdir(r"C:\Users"), os.path.isfile(r"C:\Users")

os.path.isdir(r"C:\config.sys"), os.path.isfile(r"C:\config.sys")

os.path.isdir("nonesuch"), os.path.isfile("nonesuch")


assert not os.path.exists(r"C:\Users\Brian")
assert os.path.exists(r"C:\Users\Default")

if os.path.exists(r"C:\autoexc.bat"):
    os.path.getsize(r"C:\autoexec.bat")

os.path.split(r"C:\temp\data.txt")

os.path.join(r"C:\temp", "data.txt")

name = r"C:\temp\data.txt"  # Windows paths
os.path.dirname(name), os.path.basename(name)


name = "/home/sc/temp/data.txt"  # Unix-style paths
os.path.dirname(name), os.path.basename(name)

os.path.splitext(r"C:\PP4thEd\Examples\PP4E\PyDemos.pyw")

mixed = "C:\\temp\\public/files/index.html"
os.path.normpath(mixed)

os.chdir(r"C:\Users")
os.getcwd()
os.path.abspath("")  # empty string means the cwd
os.path.abspath("temp")  # expand to full pathname in cwd
os.path.abspath(r"PP4E\dev")  # partial paths relative to cwd

os.path.abspath(".")  # 拓展相对路径句法
os.path.abspath("..")
os.path.abspath("../examples")

os.path.abspath(r"C:\PP4E\chapters")  # absolute paths unchanged
os.path.abspath(r"C:\temp\spam.txt")
