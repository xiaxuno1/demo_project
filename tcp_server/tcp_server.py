# --------------------------------------------------
# -*- coding: utf-8 -*-
# !/usr/bin/python
# PN: interface_test
# FN: tcp_client
# Author: xiaxu
# DATA: 2022/9/29
# Description:创建tcp client
# ---------------------------------------------------
import socket
from yaml_read import yaml_load
import json,time


class ServerSocket:
    def __init__(self,port,ip="localhost"):
        self.s = socket.socket()  # 调用socket实例化
        if ip == "localhost":  # bind传参
            ip = socket.gethostname()  #默认为本机IP
        self.s.bind((ip, port))
        self.s.listen(5)  #监听连接最多5个
    def accept_msg(self):
        '''
        接收客户端连接，向客户端发送数据
        :param send_data:
        :return:
        '''
        c,addr = self.s.accept()  #接收客户端连接，返回（client,address）
        print("Got connect from", addr)  #连接成功服务器显示
        return addr,c           #返回收到的字节码

    def send_msg(self,str):
        self.s.send(bytes.fromhex(str))

    def client_close(self,client_obj):
        client_obj.close()

if __name__ == '__main__':
    yaml_data = yaml_load("./data.yaml")
    data = []
    server = ServerSocket(5555)
    addr,c = server.accept_msg()
    while True:
        for i in range(len(yaml_data)):
            if "电源屏" in yaml_data[i]['msg']:
                data = yaml_data[i]['dyp_data']['data']
                c.send(bytes.fromhex(data))
                print("发送数据成功")
                time.sleep(1)
