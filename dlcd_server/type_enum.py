# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: sub_type_enum
# Author: xiaxu
# DATA: 2023/6/15
# Description:枚举定义
# ---------------------------------------------------
from enum import Enum


class SubType(Enum):
    DLGP = "01"
    DLWD = '02'
    HJXX = '03'
    LDSJ = '04'
    LDBX = '05'
    HWWD ='06'
    OTHERS = "FF"