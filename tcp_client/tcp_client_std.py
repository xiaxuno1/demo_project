# --------------------------------------------------
# -*- coding: utf-8 -*-
# !/usr/bin/python
# PN: interface_test
# FN: tcp_client
# Author: xiaxu
# DATA: 2022/9/29
# Description:创建tcp client
# ---------------------------------------------------
import time,base,base64
from socket import *


tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.bind(("0.0.0.0",6050))  #这里指定了client绑定的port
host = '172.16.32.115'
port = 5555
tcpclient.connect((host,port))
while True:
    time.sleep(1)
    #recv_size = tcpclient.recv(1024)
    #print(recv_size)
    data1 = 'EF EF EF EF 30 10 00 00 3C 57 08 63 8F 64 01 40 41 02 03 8F 42 6B 43 A9 59 6B 43 8B 4E 6B 43 97 6F 6B 43 ' \
            '85 AB 6A 43 B5 BC 6A 43 49 B1 6A 43 60 D4 6A 43 48 21 6A 43 C6 31 6A 43 A5 4D 6A 43 F5 44 6A 43 66 26 6B ' \
            '43 FC 33 6B 43 36 28 6B 43 AC 68 6B 43 5C 4F 6B 43 DD 53 6B 43 38 56 6B 43 13 8D 6B 43 7B 14 6A 43 21 25 ' \
            '6A 43 B8 15 6A 43 46 42 6A 43 0A D7 BB 40 C7 FC BD 40 91 32 C1 40 10 11 C5 40 9A 99 51 41 87 88 52 41 62 ' \
            '4B 53 41 AE 01 56 41 A4 70 19 41 56 13 1A 41 03 C6 1A 41 18 44 1B 41 00 00 00 00 00 00 00 00 00 00 00 00 ' \
            '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ' \
            '00 0A D7 47 42 53 EA 47 42 08 8D 48 42 28 E3 47 42 0A D7 47 42 65 D9 47 42 9D 30 48 42 04 E4 48 42 0A D7 ' \
            '47 42 67 0D 48 42 73 81 48 42 36 51 48 42 0A D7 47 42 43 EE 47 42 61 3E 48 42 F2 A3 48 42 0A D7 47 42 D0 ' \
            '2B 48 42 86 82 48 42 BD 05 48 42 0A D7 47 42 5A 18 48 42 4D 40 48 42 4C 60 48 42 0A D7 EF 42 CC DE EF 42 ' \
            '93 39 F0 42 DE 3B F0 42 1F 05 F0 42 AE 35 F0 42 25 33 F0 42 B0 47 F0 42 E1 7A EF 42 6A 9C EF 42 89 C4 EF ' \
            '42 0E E8 EF 42 5C 8F EF 42 33 94 EF 42 C1 AC EF 42 49 10 F0 42 43 87 FE FE FE FE'
    #data2 = '02038C000000000000271013861386138658F8591658E94D174CE84CFC177A1760177400030001000100000000000000000000000000000000000027102710271000000000000058E200BD00F600770098011B59140113019A00BF006800F658DC00690100004F0078010B00000000000000000000000000000000000000' \
    #       '00000000000000000000000000000000005EAD'
    tcpclient.send(bytes.fromhex(data1))
    time.sleep(1)
    #tcpclient.send(bytes.fromhex(data2))
    # data = 'hello ..你好'
    # data1 = '68656C6C6F202E2EE4BDA0E5A5BD'
    print(base64.b16decode(data1)) #解码 Base16 编码的类似字节的对象或 ASCII 字符串。
    #tcpclient.send(base64.b16decode(data1)) #编码
    #rec = tcpclient.recv(1024)
