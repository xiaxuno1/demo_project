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


path = r"F:\2020型车站配置文件"   #r表示不使用转义
for root,dir,files in os.walk(path):
    """正则匹配绝对路径"""
    root_parttern = '配置文件功能测试'
    file_parttern = '.*测试报告V1.0.0.0.*'
    if re.search(root_parttern,root):
        for file in files:
            #print(root)
            #file_path = os.path.join(root,file[0:-13]+".docx")
            #file_path.replace('\\','/')
            #print("root",root) #绝对路径
            #print(dir)  #该路径下的子目录,列表
            #print(file) #改路径下的文件，列表
            #获取文件名和后缀
            if re.search(file_parttern,file):
                file_name = file[0:-13]
                file_postfix = file.split('.')[-1]
            else:
                file_name = file.split('.')[0]
                file_postfix = file.split('.')[-1]
            #print(file_name,file_postfix)
            #修改文件名，添加20to20
            if "V1.0.0.0" in file_name:
                file_name = file_name[0:-8]
            if '20TO20'not in file_name and "说明" not in file_name :
                #避免重复修改
                #print(root+"\\"+file)
                print("新的文件路径:",root + "\\" + file_name + "20TO20" + "." + file_postfix)
                #删除文件
                #os.unlink(root+"\\"+file)
                #移动文件,千万不要直接对真是环境高，涉及到文件的删除修改，不可逆；先测试完成
                shutil.move(root+"\\"+file,root+"\\"+file_name+"20TO20"+"."+file_postfix)

def sear_path_file(path,parttern):
    pass


