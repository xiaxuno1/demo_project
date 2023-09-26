# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: serial_port
# Author: xiaxu
# DATA: 2023/9/20
# Description:串口通信实现
# ---------------------------------------------------
import serial,time
from BjlxBS.alarm_info import Alarm
from BjlxBS.equipment_status import Status
from BjlxBS.base.log import FrameLog


#串口号 波特率 校验位 停止位
class SerialData:
    def __init__(self):
        self.log = FrameLog().log()
        self.ser = serial.Serial("COM21", 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,timeout=10)
        self.read_size = 1*1024  #接收数据的大小7M
        self._running = True  #用于终止进程
        self._write_buffer = b'' #发送数据
        self._read_buffer = b'' #接收数据

    def terminate(self):
        self._running = False #终止进程

    def serial_write(self,time_gap):
        while self._running and self._write_buffer:
            self.log.info("发送数据...")
            self.ser.write(self._write_buffer)
            time.sleep(time_gap)

    def serial_read(self):
        #正在运行且没超时
        while self._running:
            self._read_buffer = self._read_buffer+self.ser.read()
            if len(self._read_buffer)>=self.read_size:  #接收数超过缓冲大小
                self.read_data = '' #直接清空
            self.log.info('接收数据...')
    def print_data(self):  #调试用
        while self._running:
            print(self._read_buffer)
            time.sleep(10)


if __name__ == '__main__':
    from threading import Thread
    ser = SerialData()
    ser._write_buffer = Status().all_status()
    t1 = Thread(target=ser.serial_write,args=(60,),daemon=True)
    t1.start()

    t2 = Thread(target=ser.serial_read,args=())
    t2.start()

    #t3 = Thread(target=ser.print_data,args=(),daemon=True)
    #t3.start()

    ser._write_buffer = Alarm().pkg()
    t4 = Thread(target=ser.serial_write,args=(1,),daemon=True)

