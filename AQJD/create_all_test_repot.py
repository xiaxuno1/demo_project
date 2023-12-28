# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: create_all_test_repot
# Author: xiaxu
# DATA: 2023/12/5
# Description:生成遍历测试报告
# ---------------------------------------------------
import os,time
import shutil

from AQJD.base.op_docx import DOCXOP
from AQJD.base.excel_op import ExcelOP
from AQJD.base.cfg_info import CFGInfo
from AQJD.base.document_convert import *
from AQJD.base.search_file import file_copy2

station_path ="E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\输出配置文件"

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
                    return file_path
    return -1

def report_info(station_path,station_code,xl_rows):
    """
    测试报告生成条件检查
    :param station_path:车站路径 /AD
    :param station_code: 车站站码 AD
    :param xl_rows: 信息表列 列表
    :return:  （报警记录.xlsx path，设备列表.xlsx path,1,2,7,9,10,11,14,15）
    """
    alarm_record_path = check_file_exsits(station_path,"报警记录.xlsx")
    equi_list_path = check_file_exsits(station_path,"设备列表.xlsx")
    for row in xl_rows:
        if row[2].lower() == station_code.lower(): #查找对应站码，不区分大小写
            return (alarm_record_path,equi_list_path,row[1],row[2],row[7],row[9],row[11],row[12],row[14],row[15])
    return (alarm_record_path,equi_list_path,-1,-1,-1,-1,-1,-1,-1,-1,-1)

#获取基础信息
def create_docx_main(row):
    if -1 in row or "#N/A" in row:
        print("信息缺少",row)
        return 0
    station_name = row[2]  #车站名
    station_code = row[3] #站码
    #保存路径：保存在测试结果同目录下
    save_path = os.path.dirname(row[0])+"\\四川网达科技有限公司集中监测系统功能补强"+station_name+"遍历测试报告.docx"
    #如果已经存在报告，不重新生成
    if  os.path.exists(save_path):
        #print("已存在测试报告",save_path)
        #pass
        return 1
    #获取车站信息
    if "四显示" in row[5]:
        ctcs_grade = "普速4显示"
    else: ctcs_grade = "普速3显示"
    block_type = row[4] #闭塞类型
    send_code_type = row[6] #发码制式
    interface = row[7]
    apply_situation = row[9]
    longest_block = row[8] #最长闭塞分区数量
    #进路情况，通过Output\基本设备列表.ini [接车进路-设备列表]+[发车进路-设备列表] 总数之和
    if not os.path.exists(station_path+"\\"+station_code): #配置文件是否存在
        print("配置文件不存在",station_name)
        return 0
    try:
        cfg = CFGInfo(station_path+"\\"+station_code+"\\Release\\Output\\基本设备列表.ini")
        route_num=cfg.get_total("接车进路-设备列表")+cfg.get_total("发车进路-设备列表") #进路情况
    except:
        return 0
    #道岔情况，在XXX-设备列表.xlsx 获取,读取设备列表
    equip_list_path = check_file_exsits(station_path+"\\"+station_code,"设备列表.xlsx")
    if equip_list_path ==-1:
        print(station_name,"没有测试报告")
        return 0
    else:
        equip_list_info = ExcelOP(equip_list_path,"Sheet1").get_rows()
    #将设备列表.xlsx中道岔总分表示不一致的所有项目作为 道岔情况
    dc_situation = ''
    for equip_row in equip_list_info:
        if "道岔总分表示不一致" in equip_row[1]:
            dc_situation = dc_situation+equip_row[1][14:]+"("+equip_row[2]+")"+" "
    if len(dc_situation)==0:
        dc_situation = "无" #无道岔情况
    #获取测试时间
    test_record_path = check_file_exsits(station_path+"\\"+station_code,"测试记录.xlsx")
    start_time = ExcelOP(test_record_path,"Sheet1").get_cols()[1]
    test_start_time = start_time[1][0:4]+"年"+start_time[1][5:7]+"月"+start_time[1][8:10]+"日"#测试开始时间
    test_end_time = start_time[-1][0:4]+"年"+start_time[-1][5:7]+"月"+start_time[-1][8:10]+"日"  #测试结束时间

    #根据模板创建关键字表
    if longest_block =="#N/A" or len(apply_situation) ==0:
        print(station_name,"信息表内缺少关键信息")
        return 0
    keyword_dic = {}
    keyword_dic["#时间段"] = test_start_time+"-"+test_end_time
    keyword_dic["#车站名称"] = station_name
    keyword_dic["#CTCS等级"] = ctcs_grade
    keyword_dic["#闭塞类型"] = block_type
    keyword_dic["#发码制式"] = send_code_type
    keyword_dic["#智能接口"] = interface
    keyword_dic["#适用场景"] = apply_situation
    keyword_dic["#道岔情况"] = dc_situation
    keyword_dic["#塞分区数量"] = str(longest_block)+"个"
    keyword_dic["#进路数量"] = str(route_num)+"条"
    test_result = "   在室内仿真测试平台，根据《铁路信号集中监测系统功能补强专项整治测试大纲》中测试案例的相关技术要求，" \
                  "完成了2010型铁路信号集中监测的7项功能测试的遍历场景测试。详细内容见《"+station_name+"-测试大纲》。"+"\n" \
                  "   受试系统设备所测试项目符合《铁路信号集中监测系统功能补强专项整治测试大纲》中规定的相关技术要求。"
    doc_file = DOCXOP(".\\data\\test_reporter.docx")
    doc_file.replace_paragraphs_by_run(keyword_dic)
    #填入测试项目汇总表格
    doc_file.fill_in_table(2,equip_list_info)
    #根据设备列表，修改测试结论表格，读取测试结论中被测项目情况，测试项目内容在设备列表中查找，没有测试结论项标记为/
    test_projects = doc_file.table_contents_row(3)
    test_project_row_num = 0
    for test_project in test_projects[1:]: #不要
        test_project_row_num = test_project_row_num+1  #从1开始
        count = 0  #记录未匹配到的次数
        for equip_row in equip_list_info[1:]: #查看设备列表中是否有此报警，没有标记为/
            if test_project[1][:-4] in equip_row[1]:  #eg：道岔总分表示不一致 in 4.1.道岔总分表示不一致_多动道岔
                #print("匹配到了",equip_row[1])
                break  #匹配到后就不再进行匹配
            count = count+1
        if count>=len(equip_list_info)-1: #表头不算
            doc_file.fill_cell(3,(test_project_row_num,2),"/")  #设备列表中没有此报警
    #填写测试结论表格
    doc_file.fill_cell(4,(2,1),test_start_time) #填入时间
    doc_file.fill_cell(4,(3,1),test_result) #填入测试结论
    #保存docx
    print("保存路径",save_path)
    doc_file.save_docx(save_path)
    return save_path

def create_all_test_report(path):
    listdir = os.listdir(path)  #path下所有的文件夹和文件，默认所有站配置都在path下，不存在在子目录下
    xl = ExcelOP(".\\data\\项目管理.xlsx", "10型新增安全监督信息表")
    xl_rows = xl.get_rows()
    for dir in listdir:
        loc = os.path.normpath(path + "\\" + dir)
        if os.path.isdir(loc): #判断目录
            info = report_info(loc,dir,xl_rows) #获取测试报告必要信息
            report_path = create_docx_main(info)  #创建测试报告,转换为pdf
            #将测试大纲转换为pdf,只有重新生成测试报告才会转换
            test_outlook = check_file_exsits(loc,"测试大纲.xlsx")
            #测试报告更新时重新生成pdf
            if test_outlook != -1 and os.path.isfile(report_path):  #找到了路径
                #如果文件存在，就不重新生成
                excel2pdf(test_outlook)
            #将测试报告转换为pdf
            if os.path.isfile(report_path):
                docx2pdf_win32com(report_path)

def create_output_test_report(path,dst_path):
    """
    生产输出的测试报告，复制四个文件形成新的
    :param path:存放位置
    :return:
    """
    listdir = os.listdir(path)  #path下所有的文件夹和文件，默认所有站配置都在path下，不存在在子目录下
    xl = ExcelOP(".\\data\\项目管理.xlsx", "10型新增安全监督信息表")
    xl_rows = xl.get_rows()
    for dir in listdir:
        loc = os.path.normpath(path + "\\" + dir)
        test_outlook = check_file_exsits(loc, "测试大纲.pdf")
        alarm_record = check_file_exsits(loc, "报警记录.xlsx")
        test_record = check_file_exsits(loc, "测试记录.xlsx")
        test_report = check_file_exsits(loc, "遍历测试报告.pdf")
        if os.path.isfile(test_report):  #生成了报告
            station_info = report_info(loc, dir, xl_rows)  # 获取车站信息
            if not os.path.isdir(dst_path + "\\" + station_info[2]):
                os.mkdir(dst_path + "\\" + station_info[2])
            file_copy2(test_outlook, dst_path + "\\" + station_info[2])
            file_copy2(alarm_record, dst_path + "\\" + station_info[2])
            file_copy2(test_record, dst_path + "\\" + station_info[2])
            file_copy2(test_report, dst_path + "\\" + station_info[2])


#判断最后一个记录时间是否超出指定时间
def is_outtime(path,sheet_name,index,dead_timestamp = 1701705600.0):
    xl = ExcelOP(path,sheet_name)
    row_total = xl.get_row_total()  #总共多少行
    last_time = xl.get_cell(row_total,index) #最后一条时间记录,cell中是从1开始
    print("最后一条测试记录时间为：",last_time,row_total,os.path.split(path)[1])
    last_test_time = time.mktime(time.strptime(last_time,"%Y-%m-%d %H:%M:%S"))#字符串转换为时间格式
    #dead_timestamp = 1701705600.0  #截止时间
    if last_test_time-dead_timestamp>=0:
        return 1
    return 0

#按照列索引修改exell表列的内容
def change_xl_time(path,sheet_name,index,dead_timestamp = 1701705600.0):
    xl = ExcelOP(path,sheet_name)
    row_total = xl.get_row_total()  #总共多少行
    last_time = xl.get_cell(row_total,index) #最后一条时间记录,cell中是从1开始
    last_test_time = time.mktime(time.strptime(last_time,"%Y-%m-%d %H:%M:%S"))#字符串转换为时间格式
    cols = xl.get_cols()
    serial_col  = cols[0] #序号列
    time_col = cols[index-1]
    delay_time =  (2+((last_test_time-dead_timestamp)// 86400))*86400 #往前推的秒数
    #重新写入时间,从序号1开始
    start_index = 0
    for j in range(len(serial_col)): #序号
        if serial_col[j].strip() == "1":  #序号开始的地方
            start_index = j
            break
    for i in range(start_index,len(time_col)):
        #将时间字符串转换为时间戳减去往前时间，再次转换为字符串格式，写入excel表中
        new_data = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.mktime(time.strptime(time_col[i],"%Y-%m-%d %H:%M:%S"))-delay_time),)
        xl.write_data(i+1,index,new_data) #这里excel中从1开始的
    xl.save_xl() #保存excel

#修改超出时间
def change_all_outtime():
    listdir = os.listdir(station_path)  # 列出所有文件和子目录
    for dir in listdir:
        loc = station_path + "\\" + dir
        if os.path.isdir(loc):
            dst_path = loc +"\\Release"
            test_record_path = check_file_exsits(dst_path,"测试记录.xlsx")
            alarm_record_path = check_file_exsits(dst_path,"报警记录.xlsx")
            if test_record_path ==-1 or alarm_record_path ==-1:
                continue
            if is_outtime(test_record_path,"Sheet1",2)==0:
                print("时间符合")
            else:
                print("时间超过截止时间，将修改开始时间和结束时间",dir)
                change_xl_time(test_record_path,"Sheet1",2)
                change_xl_time(test_record_path,"Sheet1",3)
                change_xl_time(alarm_record_path, "Sheet1", 5)
                change_xl_time(alarm_record_path, "Sheet1", 6)

#查找指定目录下的所有文件
def serach_files(path,file_name):
    count = 0  #数量
    for root,dir,files in os.walk(path):
        for file in files:
            if file_name in file:
                count = count+1
                #print(file)
    print("找到目标文件总数：",count)


if __name__ == '__main__':
    #change_all_outtime()  #修改超限时间
    create_all_test_report(station_path)
    dst_path = "E:\\配置文件过程库\\10型以前车站\\10型增加安全监督\\10安全监督测试报告"  #测试报告输出目录
    create_output_test_report(station_path,dst_path)
    #xl = ExcelOP(station_info_path,"10型新增安全监督信息表")
    #print(report_info(station_path + "\\MZG", "MZG", xl.get_rows()))
    #serach_files(station_path,"遍历测试报告.docx")

