# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: queue_
# Author: xiaxu
# DATA: 2023/9/26
# Description:利用queue来实现线程数据间的共享
# ---------------------------------------------------
from queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q):
    while True :
        # Produce some data
        ...
        data = 1
        out_q.put(data)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()

        # Process the data
        ...
        # Indicate completion
        in_q.task_done()  #告诉线程，get（）完成

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join() #阻塞直到所有被put()的被消费