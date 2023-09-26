# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: mult_thread
# Author: xiaxu
# DATA: 2023/6/16
# Description:多线程
# ---------------------------------------------------
from dlcd_server.dlcd_main import *
from threading import Thread


class DLCDServer():
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running =False #定义线程终止的条件，以便手动终止；防止长期阻塞

    def run(self,sock):
        sock.settimeout(10) #30s未收到数据认为中断
        while self._running:
            try:
                data = sock.recv(8192)
            except sock.timeout:
                continue
        return

c = DLCDServer()
sock = ServerSocket(7000).s
t = Thread(target=c.run, args=(sock,))
t.start()
#c.terminate() # Signal termination
t.join()      # Wait for actual termination (if needed)


