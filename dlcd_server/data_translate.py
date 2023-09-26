# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: data_deal
# Author: xiaxu
# DATA: 2023/3/1
# Description:定义数据处理的：16进制表示的字符转换为ascii, 十进制转换为指定路数的进制
# ---------------------------------------------------
import struct,base64
import time


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

def deci_to_str(deci,form,file_width=8):
    """
    将十进制的数据转换为字符串
    :param daci:
    :param type:
    :return:
    """
    return base64.b16encode( struct.pack(form,deci)).decode().zfill(file_width)


if __name__ == '__main__':
    print(deci_to_str(int(time.time()), '<i'))
