# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: his_env_create
# Author: xiaxu
# DATA: 2023/11/15
# Description:
# ---------------------------------------------------
import configparser,shutil
import rarfile,zipfile
import os,time
from AQJD.base.cfg_info import CFGInfo


his_data_path = 'E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\仿真'
output_cfg_file = 'E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件'
station_name = "MZH"

#修改.ini文件的指定项内容
def create_hisdatasend():
    #复制输出配置文件
    print("开始复制配置文件in："+output_cfg_file+"\\"+station_name)
    if os.path.exists(output_cfg_file+"\\"+station_name):
        if os.path.exists(his_data_path + "\\HisDataSend\\" + station_name):
            #目标文件夹存在时，删除目标文件夹
            shutil.rmtree(his_data_path + "\\HisDataSend\\" + station_name)
        shutil.copytree(output_cfg_file + "\\" + station_name, his_data_path + "\\HisDataSend\\" + station_name)
    else:
        print("配置文件不存在",output_cfg_file+"\\"+station_name)
    #复制解压历史数据
    print("开始复制历史数据in："+his_data_path+"\\历史数据\\"+"data-"+station_name+".rar")
    if os.path.exists(his_data_path+"\\历史数据\\"+"data-"+station_name+".rar"):
        rf = rarfile.RarFile(his_data_path+"\\历史数据\\"+"data-"+station_name+".rar", mode='r')  # mode的值只能为'r'
        '''
        rf_list = rf.namelist()  # 得到压缩包里所有的文件
        for f in rf_list:
            rf.extract(f, folder_abs)  # 循环解压，将文件解压到指定路径
        '''
        # 一次性解压所有文件到指定目录
        rf.extractall(his_data_path+"\\HisDataSend\\") # 不传path，默认为当前目录
        #重命名为data

    else:
        print("文件不存在",his_data_path+"\\历史数据\\"+"data-"+station_name+".rar")

    #获取历史数据时间用于设置开始时间和结束时间syscfg.ini修改
    print("开始修改syscfg.ini："+his_data_path + '\\HisDataSend\\config\\syscfg.ini')
    with open(his_data_path+"\\HisDataSend\\data\\kglall.txt","r") as fp:
        start_time = fp.readline().split(";")[1][1:-1] #开始时间字符串,删除“”字符
        end_time = start_time[:10]+" 23:59:59"#start_time[:11]+
        print("时间设置",start_time,end_time)
        cfg = CFGInfo(his_data_path + '\\HisDataSend\\config\\syscfg.ini')
        cfg.set('站机', "本地电报码", station_name)
        cfg.set('站机', "本地汉字名", station_name)
        cfg.set("站机","开始时间",start_time)
        cfg.set("站机","结束时间",end_time)
        cfg.write()

    #修改setwd.bh.ini的[安全监督服务器]
    print("开始修改setwd_bh.ini")
    cfg = CFGInfo(his_data_path + '\\HisDataSend\\'+station_name+"\\cfg\\setwd_bh.ini")
    cfg.set('安全监督服务器', "IP", '127.0.0.1')
    cfg.set('安全监督服务器', "PORT", '6001')
    cfg.write()

    #压缩文件，打包压缩
    print("开始打包文件："+his_data_path+"\\HisDataSend-"+station_name+".zip")
    zip_path = his_data_path+"\\HisDataSend-"+station_name+".zip"
    with zipfile.ZipFile(zip_path,mode='w',compression=zipfile.ZIP_DEFLATED)as f2zip:
        for root,dir,file_list in os.walk(his_data_path+"\\HisDataSend\\"):
            if len(file_list)>0:  #存在文件，空文件夹则不会压缩，可能会有问题
                for file in file_list:
                    f2zip.write(root+"\\"+file,arcname=root[len(his_data_path+"\\HisDataSend\\"):]+"\\"+file)  #传入一个路径,路径的名称（相对）
            else:  #文件夹路径压缩，将空文件夹也保留，避免程序缺少空文件夹
                f2zip.write(root,
                        arcname=root[len(his_data_path + "\\HisDataSend\\"):])  # 传入一个路径,路径的名称（相对于压缩包）

    #打包完成后恢复环境
    print("恢复环境，删除配置和历史data")
    shutil.rmtree(his_data_path + "\\HisDataSend\\" + station_name)  #删除站配置
    shutil.rmtree(his_data_path + "\\HisDataSend\\data") #删除历史文件

    print("生成文件完成",zip_path)


if __name__ == '__main__':
    create_hisdatasend()
