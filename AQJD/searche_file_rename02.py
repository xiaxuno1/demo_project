# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: SearchFileRename
# FN: searche_file_rename
# Author: xiaxu
# DATA: 2023/2/15
# Description:查找文件重新命名复制到指定位置
# ---------------------------------------------------
import re,sys,os,shutil


path = r"F:\2020型车站配置文件"   #r表示不使用转义
for root,dir,files in os.walk(path):
    """正则匹配绝对路径"""
    root_parttern = '配置文件功能测试'
    file_parttern = '.*测试报告V1.0.0.0.*'
    if re.search(root_parttern,root):
        print(files)
