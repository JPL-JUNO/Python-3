"""
@Title: 让对象支持上下文管理协议
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 11:07:11
@Description: 让对象支持上下文管理协议（context-management protocol，通过 with 语句触发）。
"""

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM) -> None:
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected")
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


if __name__ == "__main__":
    from functools import partial

    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b"Get /index.html HTTP/1.0\r\n")
        s.send(b"Host: www.python.org\r\n")
        s.send(b"\r\n")
        resp = b''.join(iter(partial(s.recv, 8192), b''))
