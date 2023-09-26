# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: check_code
# Author: xiaxu
# DATA: 2023/9/20
# Description:计算检查码
# ---------------------------------------------------

def bcc(data1,data2):
    return data1 ^ data2

if __name__ == '__main__':
    data1 = 5
    data2 = 6
    print(bcc(data1,data2))
    data3 = 0x05
    print(bcc(data3,data2))