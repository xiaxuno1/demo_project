# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dyp_emulate
# Author: xiaxu
# DATA: 2023/2/27
# Description:
# ---------------------------------------------------
import base64

def strs_to_ascii(hex_str):
    """
    :param hex_str  16进制的字符串类似：'12h 34h'
    转换器，将16进制形式的字符串转换为ascii码转换为ascii码
    数据类型：整型（2B）、浮点型（4B）低字节在前。单字节
    转换返回：返回ascii码的16进制表示形式如："31H 32H 33H 34H"
    实际上就是将一个字节的内容转换为两个字节的字符串即可
    """
    ascii_chars = ''
    byte_strs = hex_str.split(' ')
    for byte_str in byte_strs:
        for i in byte_str: #字节的字符串转换为ascii
            #print(ord(i)) #将16进制形式的字符串转换为ascii码
            ascii_chars =ascii_chars+i#将单个字符串转换为整形
    return ascii_chars

def deci_to_bin(data,length:int):
    """
    定义十进制转换为二进制的方法
    :param length: 转换后的长度
    :param data: 接收一个待转换的数值
    :return 返回转换后的二进制字符串
    """
    d = ''
    while data > 0:
        d = d + str(data % 2)  # 取余数，
        data = data // 2  # 整除数
    d = d[::-1]  # 根据计算规则翻转
    while len(d) < length:  # d的位数小于规定位数前面填充0
        d = '0' * (12 - len(d)) + d
    return d


class DYPChck:
    """电源屏校验的整体结构，包含需要计算校验的部分数据"""
    def __init__(self,equ_type,info_type,info,eoi="0d",soi="7e"):
        """
        初始化每个部分
        :param soi:起始字节码7eH，类型为一个字节
        :param equ_type:设备类型1B。两个字节ascii码
        :param info_type:信息类型1B。两个字节ascii码
        :param info_length:信息长度2B。规定格式
        :param info:信息内容x*b。规定的ascii码
        :param checksum:校验和2B。规定的ascii码
        :param eoi:结束字节码0DH，一个字节
        """
        self.soi = soi
        self.equ_type = equ_type
        self.info_type = info_type
        self.info = info
        self.eoi = eoi

    def info_length(self):
        """
        义计算info_length的内容
        LENGTH共2个字节，由LENID和LCHKSUM组成，LENID表示INFO项的ASCII码字节数，
        LENGTH传输中先传高字节，再传低字节，分四个ASCII码传送。
        校验码的计算：D11D10D9D8+D7D6D5D4+D3D2D1D0，求和后模16的余数取反加1。
        :return: 将二进制字符串转换为10进制传递
        """
        info_len = len(self.info) #LENID表示INFO项的ASCII码字节数
        d = deci_to_bin(info_len,12) #d11-d0的字符串形式
        d_sum = int(d[0:4], 2) + int(d[4:8], 2) + int(d[8::], 2)
        lchksum = (~d_sum % 16) + 1  # 注意这里的括号，因为+-的优先级要高于^ &的优先级
        lchksum_str = deci_to_bin(lchksum,4)
        length_str = lchksum_str+d
        return int(length_str,2)

    def checksum(self,info_length):
        """
        定义计算checksum方法
        CHKSUM的计算是除SOI、EOI和CHKSUM外，其他字符ASCII码值累加求和，所得结果模65535余数取反加1
        :param info_length: info字节长度的ascii形式
        :return: checksum的int表示
        """
        checksum = 0
        for i in self.equ_type:
            checksum +=i
        for i in self.info_type:
            checksum +=i
        for i in info_length:
            checksum +=i
        for i in self.info:
            checksum +=i
        checksum = (~checksum % 65535) + 1  # 注意这里的括号，因为+-的优先级要高于^ &的优先级
        return checksum

    def dyp_package(self,info_length,checksum):
        """
        根据协议各个部分组包,接收16进制格式的字符串
        :return:组包完成的字节流
        """
        pkg = bytes.fromhex(self.soi+self.equ_type+self.info_type+info_length+self.info+checksum+self.eoi)
        return pkg



if __name__ == '__main__':
    data1 = '01' #A
    data2 = '23 45'
    data3 = '67 89 ab cd'
    print(strs_to_ascii(data1))
    print(strs_to_ascii(data2))
    print(strs_to_ascii(data3))


