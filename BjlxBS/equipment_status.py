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
from BjlxBS.file_info_update import FileUpdate
from BjlxBS import observer


class Status(BJLX,observer.Observer):
    def __init__(self):
        super().__init__()
        self._data = b''
        self._pkg_num =1 #数据包编号
        self.cfg = CFGInfo()
        self.before_info = [] #初始信息
        self.updated_info = self.cfg.get_info("继电器开关量") #更新后的信息
        self._change_info = [] #修改的信息,[序号，状态]，序号从1开始
        self.all_status = self._all_status() #存放全体开关量
        self.change_status = b'' #状态变化数据

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

    def update(self, subject: FileUpdate) -> None:
        #更新文件内容;获取更新的内容;返回
        self._change_info = [] #每次有更新时清空上次数据
        self.before_info = self.updated_info  #记录初始的数据;有更新时之前最新数据变为过时数据
        self.cfg = CFGInfo()
        self.updated_info = self.cfg.get_info("继电器开关量")
        if len(self.before_info) != len(self.updated_info):
            print("数据更新后路数长度与之前不一致")
        else:
            for i in range(1,len(self.updated_info)):
                #判断数据位的修改
                if  self.updated_info[i][-1] != self.before_info[i][-1]:
                    self._change_info.append([i,self.updated_info[i][-1]])
        #更新保存的全体状态数据和变化状态数据
        self.all_status = self._all_status()  # 存放全体开关量
        self.change_status = self._change_status()  # 状态变化数据
        #print(self.change_status)

    def _change_status(self):
        #这里可能同时会产生多种不同功能码的数据
        #获取报警开关量信息
        self._data = b''  # 初始化
        #按照设备方向组包数据
        equ1_data = self._data
        equ2_data = self._data
        equ3_data = self._data
        equ4_data = self._data
        #变化数据组包
        for i in range(0,len(self._change_info)):
            # 时间信息7bt
            self._data = self._data+self._time()
            #继电器序号、继电器状态；按照设备分别组包
            #print(self._change_info[i])
            jdq_ori = ((self._change_info[i][0]-1)//35)+1 #设备方向
            jdq_index = ((self._change_info[i][0]-1) % 35) #继电器编号;i应该从0开始
            #jdq_index = ((jdq_ori<<6)&0xc0)+(jdq_num&0x3f) #继电器序号，位操作2+6
            status = eval(self._change_info[i][1]) #继电器状态 0/1
            if jdq_ori == 1:
                equ1_data = equ1_data + self._time()
                equ1_data = equ1_data+ bytes.fromhex(hex(jdq_index)[2:].zfill(2))+bytes.fromhex\
                        (hex(status)[2:].zfill(2))
            elif jdq_ori ==2:
                equ2_data = equ2_data + self._time()
                equ2_data = equ2_data + bytes.fromhex(hex(jdq_index)[2:].zfill(2)) + bytes.fromhex\
                        (hex(status)[2:].zfill(2))
            elif jdq_ori ==3: #数据
                equ3_data = equ3_data + self._time()
                equ3_data = equ3_data + bytes.fromhex(hex(jdq_index)[2:].zfill(2)) + bytes.fromhex\
                        (hex(status)[2:].zfill(2))
            elif jdq_ori == 4:
                equ4_data = equ4_data + self._time()
                equ4_data = equ4_data + bytes.fromhex(hex(jdq_index)[2:].zfill(2)) + bytes.fromhex\
                        (hex(status)[2:].zfill(2))
        #将每个设备完整包合并到一起返回
        if len(equ1_data):
            self._data = b''
            self._pkg_num = (self._pkg_num+1)%0xffff #2个字节
            self._data = self._data+struct.pack('<H',self._pkg_num) #数据包编号低字节在前
            self._data = self._data+equ1_data
            self.set_func_code('42')
            self.set_len()
            self.set_bcc_code()
            equ1_data_pkg = self.pkg()
        else:equ1_data_pkg = b''

        if len(equ2_data):
            self._data = b''
            self._pkg_num = (self._pkg_num+1)%0xffff #2个字节
            self._data = self._data+struct.pack('<H',self._pkg_num) #数据包编号低字节在前
            self._data = self._data+equ2_data
            self.set_func_code('44')
            self.set_len()
            self.set_bcc_code()
            equ2_data_pkg = self.pkg()
        else: equ2_data_pkg = b''

        if len(equ3_data):
            self._data = b''
            self._pkg_num = (self._pkg_num+1)%0xffff #2个字节
            self._data = self._data+struct.pack('<H',self._pkg_num) #数据包编号低字节在前
            self._data = self._data+equ3_data
            self.set_func_code('49')
            self.set_len()
            self.set_bcc_code()
            equ3_data_pkg = self.pkg()
        else:equ3_data_pkg = b''

        if len(equ4_data):
            self._data = b''
            self._pkg_num = (self._pkg_num+1)%0xffff #2个字节
            self._data = self._data+struct.pack('<H',self._pkg_num) #数据包编号低字节在前
            self._data = self._data+equ4_data
            self.set_func_code('4b')
            self.set_len()
            self.set_bcc_code()
            equ4_data_pkg = self.pkg()
        else:equ4_data_pkg = b''

        return equ1_data_pkg+equ2_data_pkg+equ3_data_pkg+equ4_data_pkg

    def _all_status(self):
        self._data = b'' #初始化
        self._data = self._data+struct.pack('<H',self._pkg_num) #低字节在前
        self._pkg_num = (self._pkg_num+1)%0xffff
        #数据区定义
        self._data = self._data+self._time()
        infos = self.updated_info
        #全体设备的序号和状态
        for i in range(1,len(infos)):
            jdq_ori = ((i-1)//35)+1 #设备方向
            jdq_num = ((i-1) % 35) #继电器编号;i应该从0开始
            jdq_index = ((jdq_ori<<6)&0xc0)+(jdq_num&0x3f) #继电器序号，位操作2+6
            status = eval(infos[i][-1]) #继电器状态 0/1
            self._data = self._data+ bytes.fromhex(hex(jdq_index)[2:].zfill(2))+bytes.fromhex(hex(status)[2:].zfill(2))
        self.set_len()  #计算长度
        self.set_func_code('48')
        self.set_addr('01 00')
        self.set_bcc_code()
        return self.pkg()


if __name__ == '__main__':
    #组装包
    alarm =Status()
    file_info = FileUpdate() #观察目标
    file_info.attach(alarm) #添加观察者
    print(alarm._all_status())
    while True:
        time.sleep(5) #5s检测一次
        if file_info.isfile_update():
            print("文件更新")
            print(alarm._all_status())
            break




