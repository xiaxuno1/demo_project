# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: PythonCRC32
# FN: crc16
# Author: xiaxu
# DATA: 2022/11/18
# Description:
# ---------------------------------------------------
import base64
import struct


def crc16(bytes_data,poly= 0xA001,init_crc = 0xffff):
    """
    定义crc16计算方法的实现，通过不同的多项式，初始值，实现不同模型计算
    :return crc16的数值
    """
    crc16 = init_crc #16位的初始寄存器
    datas = list(bytes_data.split()) #数据按照字节分开
    for data in datas:
        a=int(data,16)
        # 把第一个8位二进制数据（既通讯信息帧的第一个字节）与16位的CRC寄存器的低8
        #位相异或，把结果放于CRC寄存器，高八位数据不变；
        crc16 = a ^ crc16
        for i in range(8):
            # 把CRC寄存器的内容右移一位（朝低位）用0填补最高位，并检查右移后的移出位；
            # （4）、如果移出位为0：重复第3步（再次右移一位）；如果移出位为1，
            # CRC寄存器与多项式A001（1010 0000 0000 0001）进行异或；（5）、重复步骤3和4，直到右移8次，
            # 这样整个8位数据全部进行了处理；
            if 1&(crc16) == 1: #判断要右移的一位为0还是1
                crc16 = crc16 >> 1
                crc16 = crc16^poly
            else:
                crc16 = crc16 >> 1
    return crc16


class CRC16_XMODEM():
    def __init__(self):
        self.poly = 0x1021
        self.perset = 0
        self._tab = [self._initial(i) for i in range(256)] #初始化时计算crc表

    def _initial(self,c):
        """预先生成crc表"""
        crc = 0
        c = c << 8
        for j in range(8):
            if (crc ^ c) & 0x8000:
                crc = (crc << 1) ^ self.poly
            else:
                crc = crc << 1
            c = c << 1
        return crc
    
    def _update_crc(self,crc, c):
        cc = 0xff & c
    
        tmp = (crc >> 8) ^ cc
        crc = (crc << 8) ^ self._tab[tmp & 0xff]
        crc = crc & 0xffff
        #print (crc)
    
        return crc
    
    def crc(self,str):
        """对一个字节计算crc16后返回作为新的crc"""
        crc = self.perset
        for c in str:
            crc = self._update_crc(crc, ord(c))
        return crc

    def crcb(self,bytes_str):
        """循环全部字节，每个字节调用crc"""
        crc = self.perset
        datas = bytes_str.split()
        for c in datas:
            c = int(c,16)
            crc = self._update_crc(crc, c)
        return crc

if __name__ == '__main__':
    ls = "0E 03 00 72 00 01 00 01 00 01 00 01 00 01 00 01  \
         00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
         00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
        00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01\
    00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01 00 01"
    #print(bytes.fromhex(ls))
    crc = crc16(ls)
    print(base64.b16encode(struct.pack('<H',crc)).decode()) #struct编码再转换

