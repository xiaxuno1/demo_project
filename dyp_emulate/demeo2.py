# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: demeo2
# Author: xiaxu
# DATA: 2023/2/27
# Description:数据转换
# ---------------------------------------------------
import base64

data = 'hello ..你好'
data1 = '68656C6C6F202E2EE4BDA0E5A5BD'
data2 = b'68656C6C6F202E2EE4BDA0E5A5BD'
print(data.encode()) #b'hello ..\xe4\xbd\xa0\xe5\xa5\xbd' 字符串编码
print(base64.b16encode(data.encode())) #b'68656C6C6F202E2EE4BDA0E5A5BD' 字节码编为16进制的字节码
print(base64.b16encode(data.encode()).decode()) #68656C6C6F202E2EE4BDA0E5A5BD 字节码编码
print(base64.b16decode(data2))
print(base64.b16decode(data1)) #字节码或类字节码，解码 Base16 编码的类似字节的对象或 ASCII 字符串。

