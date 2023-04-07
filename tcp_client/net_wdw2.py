# --------------------------------------------------
#coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: tcp_client
# Author: xiaxu
# DATA: 2022/9/29
# Description:创建外电网的网口发送数据,接另两个外电网时
# ---------------------------------------------------
import time,base,base64
from socket import *
from tcp_client.yaml_read import yaml_load


yaml_data = yaml_load("./data.yaml")
data = []
tcpclient = socket(AF_INET,SOCK_STREAM)
tcpclient.bind(("0.0.0.0",6065))  #这里指定了client绑定的port
host = '172.16.32.116'
port = 7778
tcpclient.connect((host,port))
while True:
    #recv_size = tcpclient.recv(1024)
    #print(recv_size)
    for i in range(len(yaml_data)):
        if "外电网" in yaml_data[i]['msg']:
            data = yaml_data[i]['wdw_data']['data']
            tcpclient.send(bytes.fromhex(data))
            #print('发送成功')
            time.sleep(1)
    #tcpclient.send(bytes.fromhex(data2))
    # data = 'hello ..你好'
    # data1 = '68656C6C6F202E2EE4BDA0E5A5BD'
    #print(base64.b16decode(data1)) #解码 Base16 编码的类似字节的对象或 ASCII 字符串。
    #tcpclient.send(base64.b16decode(data1)) #编码
    #rec = tcpclient.recv(1024)
