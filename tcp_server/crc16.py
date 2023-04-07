# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: PythonCRC32
# FN: crc16
# Author: xiaxu
# DATA: 2022/11/18
# Description:
# ---------------------------------------------------
# -*-coding:utf8-*-
# 这样你可以input数据，用空格隔开，.split在此是用来分割字符串的
# 输入数据后，打印一下列表
def crc16_modbus(bytes_data,poly= 0xA001,init_crc = 0xFFFF):
    """接收字节码"""
    crc16 = init_crc
    #self.poly=0xA001 #CRC的计算公式self.poly=x16+x15+x2+1

    datas = list(bytes_data.split())
    for data in datas:
    # 表示将datas列表中的每一个变量赋值给data，
    # 在此你可以自由输入数据，校验的次数是由你输入的数据的多少决定的
        a=int(data,16)
        # print(a)
        crc16 = a ^ crc16
        #^ 异或运算：如果两个位为“异”（值不同），则该位结果为1，否则为0。
        for i in range(8):
            # 对于每一个data，都需要右移8次，可以简单理解为对每一位都完成了校验
            if 1&(crc16) == 1:
                # crc16与上1 的结果(16位二进制)只有第0位是1或0，其他位都是0
                #判断最后一位是否为1为1则移位重复异或运算，为0则移位；重复8次
                # & 与运算：都是1才是1，否则为0
                crc16 = crc16 >> 1
                # >>表示右移，即从高位向低位移出，最高位补0
                crc16 = crc16^poly
            else:
                crc16 = crc16 >> 1
    #print(crc16,type(crc16))#得到的结果还是10进制
    crc16=hex(int(crc16))# 将10进制转换成16进制
    print(crc16.upper())
    crc16=crc16[2:].upper()
    # [2:]的作用是将4位16进制的0x消除
    # .upper()可以让字母变成大写，只是为了格式好看而已，并不影响校验结果
    print(crc16)
    length = len(crc16)
    high=crc16[0:length-2].zfill(2)
    high=str(high)
    # [0:length]是将得到的4位16进制切片成两个校验码而已
    # 一些结果以0开头，会自动把0给吞掉 .zfill(2)可以让结果以两位二进制的形式出现
    low=crc16[length-2:length].zfill(2)
    low=str(low)
    # print(type(low))
    print("校验码低位："+low.upper())
    print("校验码高位："+high.upper())


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
    ls = "30 10 00 00 3C 57 08 63 8F 64 01 40 41 02 03 8F 42 6B 43 A9 59 6B 43 8B 4E 6B 43 97 6F 6B 43 85 " \
         "AB 6A 43 B5 BC 6A 43 49 B1 6A 43 60 D4 6A 43 48 21 6A 43 C6 31 6A 43 A5 4D 6A 43 F5 44 6A 43 66 26" \
         " 6B 43 FC 33 6B 43 36 28 6B 43 AC 68 6B 43 5C 4F 6B 43 DD 53 6B 43 38 56 6B 43 13 8D 6B 43 7B 14 6A " \
         "43 21 25 6A 43 B8 15 6A 43 46 42 6A 43 0A D7 BB 40 C7 FC BD 40 91 32 C1 40 10 11 C5 40 9A 99 51 41 " \
         "87 88 52 41 62 4B 53 41 AE 01 56 41 A4 70 19 41 56 13 1A 41 03 C6 1A 41 18 44 1B 41 00 00 00 00 00 " \
         "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 " \
         "00 00 00 00 00 00 00 00 00 00 0A D7 47 42 53 EA 47 42 08 8D 48 42 28 E3 47 42 0A D7 47 42 65 D9 47 " \
         "42 9D 30 48 42 04 E4 48 42 0A D7 47 42 67 0D 48 42 73 81 48 42 36 51 48 42 0A D7 47 42 43 EE 47 42 " \
         "61 3E 48 42 F2 A3 48 42 0A D7 47 42 D0 2B 48 42 86 82 48 42 BD 05 48 42 0A D7 47 42 5A 18 48 42 4D " \
         "40 48 42 4C 60 48 42 0A D7 EF 42 CC DE EF 42 93 39 F0 42 DE 3B F0 42 1F 05 F0 42 AE 35 F0 42 25 33 " \
         "F0 42 B0 47 F0 42 E1 7A EF 42 6A 9C EF 42 89 C4 EF 42 0E E8 EF 42 5C 8F EF 42 33 94 EF 42 C1 AC EF " \
         "42 49 10 F0 42 "
    #print(bytes.fromhex(ls))
    crc = CRC16_XMODEM()
    crc_val = crc.crcb(ls) #获取的是10进制数据，有时需要翻转
    print(hex(crc_val),type(hex(crc_val)))
