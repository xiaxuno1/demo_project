# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: event_
# Author: xiaxu
# DATA: 2023/9/26
# Description:event实现线程等待
# ---------------------------------------------------
from threading import Thread, Event
import time

# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10,started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()  #这里会等待，直到started_evt.set()执行(信号量置1)
print('countdown is running')