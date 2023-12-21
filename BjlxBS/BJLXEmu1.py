# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: serial_port
# Author: xiaxu
# DATA: 2023/9/20
# Description:串口通信实现，不采用多线程
# ---------------------------------------------------
import serial,time
from threading import Thread,Event
from BjlxBS.alarm_info import Alarm
from BjlxBS.equipment_status import Status
from BjlxBS.base.log import FrameLog
from BjlxBS.base.yaml_read import yaml_load
from BjlxBS.file_info_update import FileUpdate
from concurrent.futures import ThreadPoolExecutor
from BjlxBS import observer,check_time

log = FrameLog().log()

class Singleton:
    '''单例模式，只能建立一个对象'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            # 重写new方法，当发现已经有实例时，直接返回实例，没有才创建
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
#串口号 波特率 校验位 停止位
class BjlxCom(Singleton,observer.Observer):
    def __init__(self):
        cfg_data = yaml_load('.//cfg//cfg.yaml')
        self.ser = serial.Serial(cfg_data[0]['seriel_com'],
                                 cfg_data[0]['bundrate'],
                                 parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                                 timeout=cfg_data[0]['timeout'])
        self.read_size = 1*1024  #接收数据的大小7M
        self.updata = False  #数据更新标志
        self._running = True #运行
        self._alarm_info_data = b'' #发送数据
        self._all_status_data = b''
        self._change_status_data = b''
        self._timing = b''
        self._read_buffer = b'' #接收数据

    def terminate(self):
        self._running = False #终止进程

    def update(self, subject: FileUpdate) -> None:
        self.updata = True

    def serial_write(self,data):
        if data:#之所以不放上面，防止初始时没有数据结束
            #log.info("发送数据...")
            self.ser.write(data)

    def serial_read(self):
        #正在运行且没超时,当数据更新或者手动结束时结束进程
        while self._running:
            self._read_buffer = self._read_buffer+self.ser.read(size=1024)  #阻塞模式没有收到数据时阻塞一直到超时
            if len(self._read_buffer)>=self.read_size:  #接收数超过缓冲大小
                self.read_data = '' #直接清空
    def print_data(self):  #调试用
        while self._running:
            print(self._read_buffer)
            time.sleep(10)

def th_file_update_check(file_info):
    log.info('开启文件更新检查线程')
    while True:
        time.sleep(5)  # 5s检测一次
        if file_info.isfile_update(): #检查文件更新，并通知观察者
            log.info("检测到文件更新")

def th_alarm_data(comm:BjlxCom,data_obj,attr_name,time_gap): #通用的数据发送模块
    log.info('开启报警数据发送线程')
    while True:
        data = getattr(data_obj,attr_name)()  #反射回对象属性
        if data:
            comm.serial_write(data)
        time.sleep(time_gap)

def th_all_status(comm:BjlxCom,data_obj,attr_name,time_gap): #通用的数据发送模块
    log.info('开启全体状态发送线程')
    while True:
        data = getattr(data_obj,attr_name)  #反射回对象属性
        if data:
            comm.serial_write(data)
        time.sleep(time_gap)

def th_chang_status(comm:BjlxCom,data_obj,attr_name,time_gap,reback :bool = 0,repet = 3): #通用的数据发送模块
    '''
    :param comm:通讯建立对象，提供发送接收接口
    :param data_obj: 数据对象，提供数据
    :param attr_name: 通过对应方法、属性获取实时数据
    :param time_gap: 时间间隔
    :param reback: 是否收到回执，bool类型
    :param repet: 重发次数
    :return:
    '''
    #收到回执或者发送三次
    log.info('开启变化状态线程')
    data = getattr(data_obj, attr_name)  # 反射回对象属性
    while reback or repet>0 :
        if data:
            comm.serial_write(data)
            repet = repet-1
        else:
            log.info("data为空")
            break
        time.sleep(time_gap)
    log.info('结束变化状态线程')


def run():
    alarm = Alarm()
    status = Status()
    bjlx = BjlxCom() #初始化串口

    file_info = FileUpdate() #观察目标
    file_info.attach(alarm)  #添加观察者
    file_info.attach(status) #添加观察者
    file_info.attach(bjlx)

    #记录最后一次发送数据的时间
    last_alarm_time = time.time()
    last_all_status_time = time.time()
    last_change_status_time =  time.time()
    last_timming =  time.time()

    #发送校时命令,仅发送一次
    log.info('发送校时命令')
    bjlx.serial_write(check_time.Timming().pkg())
    pool = ThreadPoolExecutor(100)

    while True:

    #文件更新
        file_info.isfile_update()
        now_time = time.time()
    #报警数据发送线程
        if now_time-last_alarm_time>=1:
            last_alarm_time = now_time
            bjlx.serial_write(alarm.pkg())
        if now_time-last_all_status_time>=60:
            last_all_status_time = now_time
            bjlx.serial_write(status.all_status)
        if bjlx.updata:
            bjlx.updata = False #更新复位，等待下次更新
            pool.submit(th_chang_status,bjlx,status,'change_status',2)
        time.sleep(1)



if __name__ == '__main__':
    run()

