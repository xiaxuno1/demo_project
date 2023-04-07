# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: setFileDecode
# Author: xiaxu
# DATA: 2023/2/21
# Description:p文件的解码
# ---------------------------------------------------


"""
pz文件为二进制文件，其生成为原文件读为二进制文件，在与0x53异或操作形成
读出二进制文件
异或后的内容
解码（deode）后写入文件（编码方式为ansi）

"""
import base64
import struct


def file_read(file_name):
    with open(file_name,'rb') as fp:
        bin_code = fp.read()
    return bin_code

def bytes_to_strs(datas):
    """
    将字节流格式的数据转换为16进制字节表示的字符串形式 ‘51 53 62...’
    :param datas: bytes数据如：b'/x10/x20'
    :return: 字节流对应的字符串格式
    """
    strs = base64.b16encode(datas).decode()
    b16_strs= ''
    for i in range(0, len(strs), 2):
        b16_strs = b16_strs + strs[i:i + 2] + ' '
    return b16_strs.strip()  # 去除两边的空格（前导和尾部）


def xor(datas,code = 0x53):
    """
    文件解码,异或一个数字
    :param datas 字节流 bytes
    :return
    """
    hex_code = ""
    for data in datas:
        code = data^0x53
        hex_code =hex_code+ hex(code).replace('0x','').zfill(2) #转换为16进制，去除0x,补0=
    return bytes.fromhex(hex_code)

def file_write(file_name,data,encode = 'ansi'):
    """将 字节流流写入文件"""
    with open(file_name,'w',encoding=encode) as fp:
        fp.write(data)


if __name__ == '__main__':
    file_name = 'set.pz'
    bin_code = file_read(file_name)
    bytes_code =xor(bin_code)
    print(bytes_code)
