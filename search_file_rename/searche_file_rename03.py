# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: SearchFileRename
# FN: searche_file_rename
# Author: xiaxu
# DATA: 2023/2/15
# Description:查找指定文件夹内文件,打印
# ---------------------------------------------------
import re,sys,os,shutil
import time

import win32api
import win32print

path = r"E:\配置文件过程库\2020型车站\打印"   #r表示不使用转义
for root,dir,files in os.walk(path):
    """正则匹配绝对路径"""
    root_parttern = '配置文件功能测试'
    file_parttern = '.*测试报告.*docx'
    if re.search(root_parttern,root):
        for file in files:
            if re.search(file_parttern,file):
                #print(root)
                #print(files)
            #print(root)
            #file_path = os.path.join(root,file[0:-13]+".docx")
            #file_path.replace('\\','/')
            #print("root",root) #绝对路径
            #print(dir)  #该路径下的子目录,列表
            #print(file) #改路径下的文件，列表
            #获取文件名和后缀
                #打印
                filename = root+'\\'+file
                print("查询的文件：",filename)
                win32api.ShellExecute(
                    0,
                    "print",  # 这个参数为open可以调用默认程序打开指定文件，为
                    filename,
                    #
                    # If this is None, the default printer will
                    # be used anyway.
                    #
                    '/d:"%s"' % win32print.GetDefaultPrinter(),
                    ".",
                    0
                )
                time.sleep(15)
