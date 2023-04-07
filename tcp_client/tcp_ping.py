# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: tcp_ping
# Author: xiaxu
# DATA: 2022/12/13
# Description:实现tcp ping的功能，使用pythonping模块
# ---------------------------------------------------
from pythonping import ping


dst_ip = '172.16.30.213'
count = 100
response = ping(target=dst_ip,count = count)
print(response.rtt_avg)
print(response)

# ping a range of server
import subprocess

string_part = 'ping -w 1 -n 2 172.16.' #设置超时2s 设置具有连接次数为2

for i in (30,32):
     for j in range(0,255):
          prompt = string_part + str(i) + '.' + str(j)
          #subprocess.call() returns the exit code of the process.
          # To get the stdout output of the ping command, use a pipe and Popen.communicate() instead
          result = subprocess.call(prompt, shell = True)
          print(result)

