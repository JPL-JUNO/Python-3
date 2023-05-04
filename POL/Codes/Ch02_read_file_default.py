"""
@Description: reading a file
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-04 21:55:34
"""
filename = "Ch02_read_file_default.py"
f = open(filename, "r")
lines = []
for line in f:
    lines.append(line.strip())


assert lines == [line.strip() for line in open('Ch02_read_file_default.py')]
