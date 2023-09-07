"""
@Title: 用迭代器取代 while 循环
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-07 10:22:40
@Description: 
"""

CHUNK_SIZE = 8192


# 伪代码
# def reader(s):
#     while True:
#         data = s.recv(CHUNK_SIZE)
#         if data == b"":
#             break
#         process_data(data)
# def reader(s):
#     for chunk in iter(lambda: s.recv(CHUNK_SIZE), b""):
#         process_data(chunk)


import sys
f = open("../passwd.txt")
for chunk in iter(lambda: f.read(10), ""):
    n = sys.stdout.write(chunk)
