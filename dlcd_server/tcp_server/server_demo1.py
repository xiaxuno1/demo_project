# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: server_demo1
# Author: xiaxu
# DATA: 2023/6/20
# Description:
# ---------------------------------------------------
from socketserver import BaseRequestHandler,TCPServer

class ServerHandler(BaseRequestHandler):
    def handle(self):
        print("Get Connerction from:",self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            print(msg)
            self.request.sendall(msg)


if __name__ == '__main__':
    pass
