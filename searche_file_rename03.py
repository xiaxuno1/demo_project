# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: SearchFileRename
# FN: searche_file_rename
# Author: xiaxu
# DATA: 2023/2/15
# Description:查找指定文件夹内文件
# ---------------------------------------------------
import re,sys,os,shutil


path = r"E:\配置文件过程库\2020型车站"   #r表示不使用转义
for root,dir,files in os.walk(path):
    """正则匹配绝对路径"""
    root_parttern = '配置文件功能测试'
    file_parttern = '.*测试报告V1.0.0.0.*'
    if re.search(root_parttern,root):
        for file in files:
            if re.search(file_parttern,file):
                print(root)
                print(files)
            #print(root)
            #file_path = os.path.join(root,file[0:-13]+".docx")
            #file_path.replace('\\','/')
            #print("root",root) #绝对路径
            #print(dir)  #该路径下的子目录,列表
            #print(file) #改路径下的文件，列表
            #获取文件名和后缀
