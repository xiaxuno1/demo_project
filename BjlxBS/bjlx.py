# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: bjlx
# Author: xiaxu
# DATA: 2023/9/20
# Description:北京联讯光纤半自动实现
# ---------------------------------------------------
from BjlxBS.check_code import bcc


class BJLX:
    def __init__(self):
        #形式为bytes
        self._start_code = b'\x01'
        self._func_code = b''
        self._data_len = b''
        self._func_code = b''
        self._addr = b'\x01\x00' #2B
        self._end_code = b'\x03'
        self._data = b''
        self._bcc_code = b''
        self._ack_code = b'\x15'

    def get_data_len(self):
        return self._data_len

    def get_func_code(self):
        return self._func_code

    def get_addr(self):
        return self._addr

    def get_ack(self):
        return self._ack_code

    def get_data(self):
        return self._data

    def get_bcc_code(self):
        return self._bcc_code

    def get_pkg(self):
        return self._start_code+self._data_len+self._func_code+self._addr+self._ack_code\
               +self._data+self._bcc_code+self._end_code

    def set_func_code(self,func_code):
        if(isinstance(func_code,(bytes,))):
            self._func_code = func_code
        self._func_code = bytes.fromhex(func_code) #字符串转化为目标格式bytes

    def set_addr(self,addr):
        if (isinstance(addr, (bytes,))):
            self._addr = addr
        self._addr = bytes.fromhex(addr)

    def set_ack(self,ack_code):
        if (isinstance(ack_code, (bytes,))):
            self._ack_code = ack_code
        self._ack_code = bytes.fromhex(ack_code)

    def set_len(self): #整帧长度
        if(len(self._data)):
            self._data_len=bytes.fromhex(hex(len(self._data)+8)[2:].zfill(2))
        else:
            print('data为空')

    def get_len(self):
        return len(self._data)+8

    def real_data(self):
        pass

    def set_bcc_code(self):
        bcc_temp = self.get_len()
        for i in self._func_code+self._addr+self._ack_code+self._data: #除头尾数据异或
            bcc_temp = bcc(bcc_temp,i)
        self._bcc_code =bytes.fromhex(hex(bcc_temp)[2:].zfill(2))

    #组包
    def pkg(self):
        pkg = self._start_code+self._data_len+self._func_code+self._addr+self._ack_code+\
        self._data+self._bcc_code+self._end_code
        return pkg

if __name__ == '__main__':
    b = bytes.fromhex('11 22 33')
    b2 = bytes.fromhex('44 55')
    for i in b+b2:
        print(i,(i)+1)
    print(b+b2)
    print(b[1])
