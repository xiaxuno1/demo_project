# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: create_data_file
# Author: xiaxu
# DATA: 2023/4/3
# Description:查找文件相关功能
# ---------------------------------------------------
import os,shutil
from AQJD.base.excel_op import ExcelOP


def find_file(path,file_name):
    for root,dir,files in os.walk(path):
        for file in files:
            if file_name in file: #近似匹配
                return file_name
    else: return -1

def find_xl_content(path,file_keyword,keyword,col_index,sheet_name = "Sheet1"):
    '''
    查找excel中指定列的内容
    在指定路径下查找符合关键字的excel文件，打开查找指定列，并返回列内容带有关键字的索引
    :param path:
    :param file_keyword:
    :return:
    '''
    for root,dirs,file_list in os.walk(path):
        if len(file_list)>0:
            for file in file_list:
                if file_keyword in file:
                    xl_path =os.path.normpath( root+"\\"+file)
                    xl = ExcelOP(xl_path,sheet_name)
                    test_results = xl.get_cols()[col_index] #测试结果列
                    i = 0
                    for test_result in test_results:
                        i = i+1
                        if test_result is not None and keyword in test_result: #内容为空时in方法会报错
                            print("存在未通过",xl_path," ",i)

def check_file_exsits(path,file_keyword):
    '''
    检查指定路径下是否存在包含关键字的文件
    :param path:
    :param file_keyword:
    :return:
    '''
    for root,dirs,files in os.walk(path):
        if len(files)>0:
            for file in files:
                file_path = os.path.normpath(root+"\\"+file)
                if file_keyword in file:
                    #print("找到了文件",file_path)
                    return 1
    print("未找到文件",path)





if __name__ == '__main__':
    #find_xl_content(path,"测试大纲.xlsx","未通过",4)
    path = r"E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件"  # r表示不使用转义
    listdir = os.listdir(path)
    for dir in listdir:
        loc = path + "\\" + dir
        if os.path.isdir(loc):
            '''
            删除指定文件
           if os.path.exists(loc+"\\Device基本设备列表.ini"):
               os.remove(loc+"\\Device基本设备列表.ini")
               os.remove(loc+"\\Device开关量名称列表.ini")
            '''
            #检查指定文件
            test_record= "\\Release\\测试报告"
            if os.path.exists(loc + "\\Release\\测试报告") :
                test_record ="\\Release\\测试报告"
            elif os.path.exists(loc + "\\Release\\测试记录") :
                test_record = "\\Release\\测试记录"
            elif os.path.exists(loc + "\\Release\\遍历记录") :
                test_record = "\\Release\\遍历记录"
            elif os.path.exists(loc + "\\Release\\Output\\遍历测试"):
                test_record = "\\Release\\Output\\遍历测试"
            elif os.path.exists(loc+"\\Release\\测试结果"):
                test_record = "\\Release\\测试结果"
            else:
                print("没有找到测试报告",loc)
                continue #没有测试报告，不检查是否存在设备列表

            check_file_exsits(loc+test_record,"设备列表.xlsx")


