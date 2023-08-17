"""
@Description: 最简单的客户端
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-17 14:28:39
"""

import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.connect((host, port))
print(s.recv(1024))
