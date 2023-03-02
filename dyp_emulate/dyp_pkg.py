# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dyp_pkg
# Author: xiaxu
# DATA: 2023/3/1
# Description:生成数据包
# ---------------------------------------------------
import base64
from dyp_emulate import dyp_struct,file_read_ini,data_deal,dyp_info
import random,struct
from enum import Enum


class EquCode(Enum):
    INPUT = "40"
    OUTPUT = '41'
    SYSOUTPUT = '42'
    RESERVED1 = '44'
    RESERVED2 = '90'
    DEFINE ='D0'

class INFOCode(Enum):
    """
    信息分类编码定义为枚举类型
    """
    SIMULATION = '41'
    TOUCHERDIGIT = '43'
    ALARMSTATUS = '44'
    SYSPARM = '46'
    SYSPARM2 = '48'
    HISDATA = '4A'
    HISALARM = '4C'
    VERSION = '4F'
    DAAR = '50'
    FACINOFO = '51'
    USERDEFINE = '80'

def input_sim():
    equ_type = EquCode.INPUT.value
    info_type = INFOCode.SIMULATION.value
    info = dyp_info.input_simulate_info()
    #print(len(info))
    dyp = dyp_struct.DYPChck(equ_type = equ_type,info_type = info_type,info = info)
    info_length = base64.b16encode(struct.pack('>H',dyp.info_length())).decode()  #将接收的整型转换为16进制字符串
    checksum = base64.b16encode(struct.pack('>H',dyp.checksum(info_length))).decode() #先传高字节
    return  dyp.dyp_package(info_length,checksum)

def input_ac_toucher():
    equ_type = EquCode.INPUT.value
    info_type = INFOCode.TOUCHERDIGIT.value
    info = dyp_info.input_ac_toucher()
    #print(len(info))
    dyp = dyp_struct.DYPChck(equ_type = equ_type,info_type = info_type,info = info)
    info_length = base64.b16encode(struct.pack('>H',dyp.info_length())).decode()  #将接收的整型转换为16进制字符串
    checksum = base64.b16encode(struct.pack('>H',dyp.checksum(info_length))).decode() #先传高字节
    return  dyp.dyp_package(info_length,checksum)

def alarm_status():
    equ_type = EquCode.INPUT.value
    info_type = INFOCode.ALARMSTATUS.value
    info = dyp_info.alarm_status()
    #print(len(info))
    dyp = dyp_struct.DYPChck(equ_type = equ_type,info_type = info_type,info = info)
    info_length = base64.b16encode(struct.pack('>H',dyp.info_length())).decode()  #将接收的整型转换为16进制字符串
    checksum = base64.b16encode(struct.pack('>H',dyp.checksum(info_length))).decode() #先传高字节
    return  dyp.dyp_package(info_length,checksum)

def output_simulate():
    equ_type = EquCode.SYSOUTPUT.value
    info_type = INFOCode.SIMULATION.value
    info = dyp_info.output_simulate_info()
    #print(len(info))
    dyp = dyp_struct.DYPChck(equ_type = equ_type,info_type = info_type,info = info)
    info_length = base64.b16encode(struct.pack('>H',dyp.info_length())).decode()  #将接收的整型转换为16进制字符串
    checksum = base64.b16encode(struct.pack('>H',dyp.checksum(info_length))).decode() #先传高字节
    return  dyp.dyp_package(info_length,checksum)

def module_status():
    equ_type = EquCode.OUTPUT.value
    info_type = INFOCode.TOUCHERDIGIT.value
    info = dyp_info.module_status()
    #print(len(info))
    dyp = dyp_struct.DYPChck(equ_type = equ_type,info_type = info_type,info = info)
    info_length = base64.b16encode(struct.pack('>H',dyp.info_length())).decode()  #将接收的整型转换为16进制字符串
    checksum = base64.b16encode(struct.pack('>H',dyp.checksum(info_length))).decode() #先传高字节
    return  dyp.dyp_package(info_length,checksum)



if __name__ == '__main__':
    #生成四种类型
    sim = (input_sim()+input_ac_toucher()+alarm_status()+output_simulate()+module_status()).decode()
    #print(sim)
    sim_str = ''
    for i in range(0,len(sim),2):
        sim_str = sim_str+sim[i:i+2]+' '
    sim_str.strip() #去除两边的空格（前导和尾部）
    print(sim_str.strip())



