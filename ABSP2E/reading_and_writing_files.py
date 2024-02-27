"""
@File         : reading_and_writing_files.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-14 19:18:48
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from pathlib import Path

Path("spam", "bacon", "eggs")
str(Path("spam", "bacon", "eggs"))
my_files = ["accounts.txt", "details.csv", "invite.docx"]
for file in my_files:
    print(Path(r"C:\Users\Stephen", file))

Path("spam") / "bacon" / "eggs"
Path("spam") / Path("bacon/eggs")
Path("spam") / Path("bacon", "eggs")

import os

Path.cwd()
os.chdir("C:\\Windows\\System32")
os.chdir("C:\\ThisFolderDoesNotExist")

Path.home()

os.makedirs("C:\\delicious\\walnut\\waffles")
Path(r"C:\Users\JPL-JUNO\spam").mkdir()

Path.cwd()
Path.cwd().is_absolute()
Path("spam/bacon/eggs").is_absolute()

Path("my/relative/path")
Path.cwd() / Path("my/relative/path")
Path.home() / Path("my/relative/path")

os.path.abspath(".")
os.path.abspath(".\\Scripts")
os.path.isabs(".")
os.path.isabs(os.path.abspath("."))
os.path.relpath("C:\\Windows", "C:\\")
os.path.relpath("C:\\Windows", "C:\\spam\\eggs")

p = Path("C:/Users/JPL-JUNO/spam.txt")
p.anchor
p.parent  # This is a Path object, not a string.
p.name
p.stem
p.suffix
p.drive

p.parents[0]
p.parents[1]
p.parents[2]

calc_file_path = "C:\\Windows\\System32\\calc.exe"
os.path.dirname(calc_file_path)
os.path.basename(calc_file_path)
os.path.split(calc_file_path)

calc_file_path.split(os.sep)
"/usr/bin".split("/")

os.path.getsize("C:\\Windows\\System32\\calc.exe")
os.listdir("C:\\Windows\\System32")

total_size = 0
for file in os.listdir("C:\\Windows\\System32"):
    total_size += os.path.getsize(Path("C:\\Windows\\System32") / file)

p = Path("C:/Users/JPL-JUNO/Desktop")
p.glob("*")
list(p.glob("*"))
list(p.glob("*.txt"))
list(p.glob("project?.docx"))

for text_file_path_obj in p.glob("*.txt"):
    print(text_file_path_obj)

win_dir = Path("C:/Windows")
not_exist_dir = Path("C:/This/Folder/Does/Not/Exist")
calc_file = Path("C:/Windows/System32/calc.exe")
win_dir.exists()
win_dir.is_dir()
not_exist_dir.exists()
calc_file.is_file()
calc_file.is_dir()
