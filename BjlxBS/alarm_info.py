# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: alarm_info
# Author: xiaxu
# DATA: 2023/9/21
# Description:告警信息
# ---------------------------------------------------
from  BjlxBS.bjlx import BJLX
from BjlxBS.base.cfg_info import CFGInfo


class Alarm(BJLX):
    def __init__(self):
        super().__init__()
        self.set_func_code('41')
        self._data = b''
        self.cfg = CFGInfo()
        self.set_alarm_data()
        self.set_len()
        self.set_bcc_code()

    def set_alarm_data(self):
        #获取报警开关量信息
        info = self.cfg.get_info("报警开关量")
        for i in range(1,len(info)):
            alarm_num = eval(info[i][2])  #报警编号
            alarm_content = eval(info[i][-1]) #报警内容
            #16进制表示
            self._data = self._data+\
                bytes.fromhex(hex(alarm_num)[2:].zfill(2)+hex(alarm_content)[2:].zfill(2))
    def get_alarm_data(self):
        return self._data

if __name__ == '__main__':
    #组装包
    alarm = Alarm()
    print(alarm.pkg())





