# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dyp_emulate
# Author: xiaxu
# DATA: 2023/2/27
# Description:电源屏info的内容生成
# ---------------------------------------------------
import base64,dyp_emulate.dyp_struct,dyp_emulate.file_read_ini,dyp_emulate.data_deal
import random,struct
from enum import Enum

def input_simulate_info():
    """此为计算发送系统输入模拟量数据（浮点数）
    计算方法为：读入配置，读入路数，设置输入类型默认为03h;根据路数生成浮点型的模拟量；struct打包
    返回ascii码字符串
    """
    nums = dyp_emulate.file_read_ini.INIOp().get("发送系统输入模拟量数据","路数") #路数
    input_type = '03'  #交流输入类型，默认为三相
    ac_nums = '02'
    simulate = b'' #数据内容
    for i in range(0,eval(nums)):
        simulate  = simulate+struct.pack('<f',11.11) #小端模式，低字节在前,本身返回的是元组
    info = ac_nums+input_type+base64.b16encode(simulate).decode() #放回ascii字符串
    return info

def input_ac_toucher():
    """此为计算发送系统输入交流接触器状态
    计算方法为：读入配置，读入路数，设置输入类型默认为03h;根据路数生成浮点型的模拟量；struct打包
    返回ascii码字符串
    """
    nums = dyp_emulate.file_read_ini.INIOp().get("发送系统输入交流接触器状态","路数") #路数
    simulate = '' #数据内容
    for i in range(0,eval(nums)):
        simulate  = simulate+random.choice(('05','00'))#00H：闭合			05H：断开
    info = simulate #放回ascii字符串
    return info

def alarm_status():
    """此为计算发送系统输入模拟量数据（浮点数）
    计算方法为：读入配置，读入路数，设置输入类型默认为03h;根据路数生成浮点型的模拟量；struct打包
    返回ascii码字符串
    """
    nums = dyp_emulate.file_read_ini.INIOp().get("发送系统告警","路数") #路数
    input_type = '03'  #交流输入类型，默认为三相
    ac_nums = '02'
    simulate = '' #数据内容
    for i in range(0,eval(nums)):
        simulate  = simulate+random.choice(('05','00'))#00H：正常			05H：告警
    info = ac_nums+input_type+simulate #放回ascii字符串
    return info

def output_simulate_info():
    """此为计算发送系统输出模拟量数据（浮点数）
    计算方法为：读入配置，读入路数，设置输入类型默认为03h;根据路数生成浮点型的模拟量；struct打包
    返回ascii码字符串
    """
    nums = dyp_emulate.file_read_ini.INIOp().get("发送系统输出模拟量数据","路数") #路数
    simulate = b'' #数据内容
    #single_data = struct.pack('<H',eval(nums)*4) #信号数据
    for i in range(0,eval(nums)):
        simulate  = simulate+struct.pack('<f',random.random()*100) #随机数
    info = base64.b16encode(simulate).decode() #放回ascii字符串
    return info

def module_status():
    """此为计算发送模块状态数据
    计算方法为：读入配置，读入路数，设置输入类型默认为03h;根据路数生成浮点型的模拟量；struct打包
    返回ascii码字符串
    """
    nums = dyp_emulate.file_read_ini.INIOp().get("发送系统模块状态","路数") #路数
    simulate = '' #数据内容
    for i in range(0,eval(nums)):
        module_addr = hex(i)[2::].zfill(2) #填充为两位的字符串格式
        module_status = random.choice(('e3','e4')) #0xE3：工作  0xE4：备用
        module_issue = random.choice(('01','00'))#0x01：故障  0x00：正常
        module_protect = random.choice(('00','02'))#0x02：保护  0x00：工作
        module_communicate = random.choice(('00','E2'))#0xE2：中断  0x00：正常
        simulate  = simulate+module_addr+module_status+module_issue+module_protect+module_communicate
    info = str(nums).zfill(2)+simulate #放回ascii字符串
    return info











if __name__ == '__main__':
    info = input_simulate_info()
    print(info)
    print("-"*50)
    print(dyp_emulate.data_deal.strs_to_ascii(info))



