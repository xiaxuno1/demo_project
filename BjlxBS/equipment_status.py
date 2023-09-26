# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: equipment__status
# Author: xiaxu
# DATA: 2023/9/22
# Description:设备状态数据
# ---------------------------------------------------
from  BjlxBS.bjlx import BJLX
from BjlxBS.base.cfg_info import CFGInfo
import time,struct


class Status(BJLX):
    def __init__(self):
        super().__init__()
        self._data = b''
        self._pkg_num =1 #数据包编号
        self.cfg = CFGInfo()

    def _time(self):
        time_struct = time.localtime()
        year = bytes.fromhex(hex(time_struct.tm_year-2000)[2:].zfill(2))
        mon = bytes.fromhex(hex(time_struct.tm_mon)[2:].zfill(2))
        day = bytes.fromhex(hex(time_struct.tm_mday)[2:].zfill(2))
        hour = bytes.fromhex(hex(time_struct.tm_hour)[2:].zfill(2))
        min = bytes.fromhex(hex(time_struct.tm_min)[2:].zfill(2))
        sec = bytes.fromhex(hex(time_struct.tm_sec)[2:].zfill(2))
        msec = bytes.fromhex('00')
        return year+mon+day+hour+min+sec+msec

    def change_status(self):
        #获取报警开关量信息
        infos = self.cfg.get_info("继电器开关量")

    def all_status(self):
        self._data = b'' #初始化
        self._data = self._data+struct.pack('<H',self._pkg_num) #低字节在前
        self._pkg_num = (self._pkg_num+1)%0xffff
        #数据区定义
        self._data = self._data+self._time()
        infos = self.cfg.get_info("继电器开关量")
        #全体设备的序号和状态
        for i in range(1,len(infos)):
            jdq_ori = ((len(infos)-1)//35)+1 #设备方向
            jdq_num = i % 35 #继电器编号
            jdq_index = jdq_ori&0xc0+jdq_num&0x3f #继电器序号，位操作2+6
            status = eval(infos[i][-1]) #继电器状态 0/1
            self._data = self._data+ bytes.fromhex(hex(jdq_index)[2:].zfill(2))+bytes.fromhex(hex(status)[2:].zfill(2))
        self.set_len()  #计算长度
        self.set_func_code('48')
        self.set_addr('01 00')
        self.set_bcc_code()
        return self.pkg()


if __name__ == '__main__':
    #组装包
    s = Status()
    print(len(s.all_status()))
    print(s.all_status())




