# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dlcd_main
# Author: xiaxu
# DATA: 2023/6/15
# Description:
# ---------------------------------------------------
import struct
import time

from dlcd_server.content_generater import ContenGenerater
from dlcd_server.dlcd_interface import DLCDInterface
from dlcd_server.type_enum import SubType
from dlcd_server.data_translate import deci_to_str




class DLCD(DLCDInterface):
    """接口实现"""
    def sub_type(self,**kwargs):
        return getattr(SubType,kwargs['type']).value  #反射回子类型的枚举值

    def time_str(self,**kwargs):
        return deci_to_str(int(time.time()),'<i',8)

    def content(self,**kwargs):
        content = ContenGenerater()
        if 'mnl_sub_type' in kwargs :
            return getattr(content,kwargs['generater_name'])(kwargs['mnl_sub_type'])
        else:
            return getattr(content,kwargs['generater_name'])()

    def frame_content_lenth(self,**kwargs):
        if "content" in kwargs:
            length = len(bytes.fromhex(kwargs['content']))
            return deci_to_str(length,'<H',4)
        else:
            print("请传递关键字为content的参数")


if __name__ == '__main__':
    dlcd = DLCD()