# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: file_info
# Author: xiaxu
# DATA: 2023/10/7
# Description:
# ---------------------------------------------------
import os,time

file_path = "D://test_tool//BjlxBS//cfg_data//BjlxSet1.ini"
file_info = os.stat(file_path)
print(file_info)
print("访问时间",time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(file_info.st_atime))) #获取文件访问时间
print("创建时间：",time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(file_info.st_ctime))) #获取文件创建时间
print("修改时间",time.ctime(file_info.st_mtime))#获取文件修改时间
print("修改时间",time.ctime(os.path.getmtime(file_path)))#获取文件修改时间