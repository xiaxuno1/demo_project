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
from threading import Thread,Event
from BjlxBS.alarm_info import Alarm
from BjlxBS.equipment_status import Status
from BjlxBS.base.log import FrameLog

class Singleton:
    '''单例模式，只能建立一个对象'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 重写new方法，当发现已经有实例时，直接返回实例，没有才创建
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
#串口号 波特率 校验位 停止位
class BjlxData(Singleton):
    def __init__(self):
        self.log = FrameLog().log()
        self.ser = serial.Serial("COM21", 9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,timeout=10)
        self.read_size = 1*1024  #接收数据的大小7M
        self._running = True  #用于终止进程
        self._alarm_info_data = b'' #发送数据
        self._all_status_data = b''
        self._change_status_data = b''
        self._timing = b''
        self._read_buffer = b'' #接收数据

    def terminate(self):
        self._running = False #终止进程

    def serial_write(self,time_gap,data_type):
        while self._running :
            self.log.info("发送数据...")
            self.ser.write(data_type)
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

def run():
    bjlx = BjlxData()
    t2 = Thread(target=bjlx.serial_read,args=())
    t2.start()

    t3 = Thread(target=bjlx.print_data,args=(),daemon=True)
    t3.start()

    bjlx._write_buffer = Alarm().pkg().reload()
    #t4 = Thread(target=ser.serial_write,args=(1,),daemon=True)

