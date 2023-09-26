# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: server_demo3
# Author: xiaxu
# DATA: 2023/6/20
# Description:
# ---------------------------------------------------
import socket
from socketserver import StreamRequestHandler,TCPServer


class EchoHandler(StreamRequestHandler):
    # Optional settings (defaults shown)
    timeout = 30                      # Timeout on all socket operations
    rbufsize = -1                    # Read buffer size
    wbufsize = 0                     # Write buffer size
    disable_nagle_algorithm = False  # Sets TCP_NODELAY socket option
    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                # self.wfile is a file-like object for writing
                print(line)
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out!')


if __name__ == '__main__':
    #千万注意，发送时需要发送“\n”作为结束符，否则会一直接收数据
    from threading import Thread
    NWORKERS = 10
    serv = TCPServer(('', 7000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()