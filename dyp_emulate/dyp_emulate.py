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
    """
    ascii_chars = ''
    byte_strs = hex_str.split(' ')
    for byte_str in byte_strs:
        for i in byte_str: #字节的字符串转换为ascii
            print(ord(i)) #将16进制形式的字符串转换为ascii码
            ascii_chars =ascii_chars#将单个字符串转换为整形
    return ascii_chars

if __name__ == '__main__':
    data1 = '01' #A
    data2 = '23 45'
    data3 = '67 89 ab cd'
    print(strs_to_ascii(data1))
    print(strs_to_ascii(data2))
    print(strs_to_ascii(data3))


