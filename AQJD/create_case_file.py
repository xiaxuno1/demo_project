# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: SearchFileRename
# FN: searche_file_rename
# Author: xiaxu
# DATA: 2023/2/15
# Description:生成安全监督的配置文件，1.alarmset.ini的替换  2.Alarm 生成   3.Device 生成 4.set.ini生成
# ---------------------------------------------------
import re,sys,os,shutil
import time
from AQJD.base.cfg_info import CFGInfo
from AQJD.base.excel_op import ExcelOP

import win32api
import win32print

path = r"E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件"   #r表示不使用转义

station_type_path = "E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\项目管理.xlsx"

def file_copy2(src_path,dst_path):
    """
    复制文件到指定路径，保留原文件的元信息（生成时间，修改时间）
    :param src_path:
    :param dst_path:
    :return:
    """
    if check_file_isupdate(src_path,dst_path): #检查文件有修改时执行复制
        shutil.copy2(src_path,dst_path)

def create_set_file(station_code,station_name,dst_path):
    """
    生成set.ini 从ZHFX-set.ini文件生成：计算ID、
    :param
    :return:
    """
    file_path = dst_path+"\\"+"set.ini"
    shutil.copy2('.\\data\\ZHFX-set.ini', file_path)
    cfg = CFGInfo(file_path)
    station_id = 0
    if len(station_code) <= 2:
        station_id = ord(station_code[-1]) * 256
    else:
        station_id = ord(station_code[-2]) * 256 + ord(station_code[-1])
    station_info = station_code + "," + station_name + "," + str(station_id)
    cfg.set('车站配置', "1", station_info)
    cfg.write()

def check_file_isupdate(src_path,dst_path):
    """
    检查dst_path文件的修改时间，确定是否需要更新
    :param src_path:
    :param dst_path:
    :return: trur flase
    """
    #两个文件修改时间相等认为文件没有改变
    if os.stat(src_path).st_mtime ==os.stat(dst_path).st_mtime:
        return False
    else:
        return True

def copy_alarm_logic(alarm_logic_path,dst_path):
    '''
    复制报警逻辑到指定位置
    :param path:
    :return:
    '''
    file_copy2(alarm_logic_path+"\\AlarmAnalysis.ini",dst_path+"\\AlarmAnalysis.ini")
    file_copy2(alarm_logic_path+"\\AlarmCase.ini",dst_path+"\\AlarmCase.ini")
    file_copy2(alarm_logic_path+"\\AlarmRule.ini",dst_path+"\\AlarmRule.ini")
    file_copy2(alarm_logic_path+"\\Data.xml",dst_path+"\\Data.xml")
    file_name = ""
    if os.path.exists(alarm_logic_path+"此为c2-c3报警逻辑.txt"):
        file_name = "此为c2-c3报警逻辑.txt"
    elif os.path.exists(alarm_logic_path+"\\此为半自动逻辑.txt"):
        file_name = "此为半自动逻辑.txt"
    elif os.path.exists(alarm_logic_path+"\\此为普速线3显示逻辑.txt"):
        file_name = "此为普速线3显示逻辑.txt"
    elif os.path.exists(alarm_logic_path+"\\此为普速线4显示逻辑.txt"):
        file_name = "此为普速线4显示逻辑.txt"
    file_copy2(alarm_logic_path+"\\"+file_name,dst_path+"\\"+file_name)

def main(path):
    """
    主流程
    :param path:
    :return:
    """
    listdir = os.listdir(path)  #path下所有的文件夹和文件，默认所有站配置都在path下，不存在在子目录下
    xl = ExcelOP(".\\data\\项目管理.xlsx", "10型新增安全监督信息表")
    xl_cols = xl.get_cols()
    for dir in listdir:
        loc = os.path.normpath(path + "\\" + dir)
        if os.path.isdir(loc): #判断目录
            #判断配置文件是否完备output存在
            #print("正在执行：",loc)
            output_path = loc+"\\"+"Release\\Output"
            if os.path.exists(output_path+"\\"+"基本设备列表.ini") and os.path.exists(output_path+"\\"+"基本设备类型.ini") \
                and os.path.exists(output_path + "\\" + "开关量名称列表.ini"):
                if not os.path.exists(loc + '\\Device'):
                    os.mkdir(loc + '\\Device')  # 目录不存在时创建
                #to-do 检查文件有修改时创建
                file_copy2(src_path=output_path+"\\"+"基本设备列表.ini",dst_path=loc+"\\Device"+"\\基本设备列表.ini")
                file_copy2(src_path=output_path+"\\"+"基本设备类型.ini",dst_path=loc+"\\Device"+"\\基本设备类型.ini")
                file_copy2(src_path=output_path+"\\"+"开关量名称列表.ini",dst_path=loc+"\\Device"+"\\开关量名称列表.ini")
            else:
                print("路径不存在，不执行创建",output_path)
                continue  #不执行后续操作

            #查找报警类型，复制报警逻辑
            if not os.path.exists(loc + '\\Alarm'):
                os.mkdir(loc + '\\Alarm')  # 目录不存在时创建
            station_name = ''
            alarm_type = ""
            i = 0  #记录excel索引
            station_code_all = xl_cols[2]
            for station_code in station_code_all:
                if dir == station_code or station_code.lower() == dir.lower() :  #站码不区分大小写
                    station_name = xl_cols[1][i]
                    alarm_type = xl_cols[9][i]
                i = i + 1
            if len(station_name)==0 or len(alarm_type) == 0 :
                print("没有找到站码",dir)
                continue
            elif "半自动" in alarm_type:
                copy_alarm_logic(".\\data\\报警逻辑\\半自动",loc+"\\Alarm")
            elif "四显示" in alarm_type:
                copy_alarm_logic(".\\data\\报警逻辑\\普速线4显示",loc+"\\Alarm")
            elif "三显示" in alarm_type:
                copy_alarm_logic(".\\data\\报警逻辑\\普速线3显示",loc+"\\Alarm")
            elif "c2-c3客专" in alarm_type:
                copy_alarm_logic(".\\data\\报警逻辑\\C2-C3",loc+"\\Alarm")
            else:
                print("未知报警类型",loc)
            #生成set.ini
            create_set_file(dir,station_name,loc)
            #替换alarmset.ini
            #20型不存在DBF
            if (os.path.exists(loc+"\\DBF")is False or os.path.exists(loc+"dbf") is False) and os.path.exists(loc+"\\JK"):
                pass
            else:
                file_copy2(".\\data\\Alarmset.ini",dst_path=loc+"\\DBF\\Alarmset.ini")


if __name__ == '__main__':
    path = r"E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件"  # r表示不使用转义
    main(path)
    #print(check_file_isupdate(path + "\\AD\\Device\\基本设备类型.ini", path + "\\AD\\Release\\Output\\基本设备类型.ini"))








