# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: test_singled
# Author: xiaxu
# DATA: 2023/9/26
# Description:
# ---------------------------------------------------
# Worker thread
import threading


def worker(n, sema):
    # Wait to be signaled
    sema.acquire()

    # Do some work
    print('Working', n)

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
#创建线程池，但是并不会执行,会等待获取信号量
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema,))
    t.start()
#信号量别释放后会唤醒一个线程执行
sema.release() #Working 0
sema.release()

