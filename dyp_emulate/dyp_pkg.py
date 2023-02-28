# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dyp_emulate
# Author: xiaxu
# DATA: 2023/2/27
# Description:电源屏组包
# ---------------------------------------------------
import base64,dyp_emulate,file_read_ini
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


if __name__ == '__main__':



