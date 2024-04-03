# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: demo
# Author: xiaxu
# DATA: 2023/10/12
# Description:
# ---------------------------------------------------
import struct,time


data = bytes.fromhex('01 00 00 00 ') #开关量完整性编号
data_time =bytes.fromhex('33 b0 bb 63 ')
data2 = bytes.fromhex('33 33 5E 43')
print("开关量编号：",struct.unpack('<l', data))
print(time.ctime(struct.unpack('<l', data_time)[0]))
print("模拟量数据：",struct.unpack('<f', data2))
print(struct.pack(">h", 250))