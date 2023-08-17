"""
@Description: 最简单的服务器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 14:26:22
"""
import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send(b"Thank you for connecting")
    c.close()
