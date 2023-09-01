"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 11:21:56
@Description: 
"""

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET,
                 type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = SOCK_STREAM
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


conn = LazyConnection(("www.python.org", 80))
with conn as s1:
    pass
    with conn as s2:
        pass
