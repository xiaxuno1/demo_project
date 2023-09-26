# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dlcd_interface
# Author: xiaxu
# DATA: 2023/6/15
# Description:定义的电缆成端的接口
# ---------------------------------------------------
import base64
import struct
from dlcd_server import crc16
from dlcd_server.type_enum import SubType


class DLCDInterface():
    """电源屏校验的整体结构，包含需要计算校验的部分数据"""
    frame_head = "EF EF EF EF" #静态属性，类的全体对象共享
    frame_tail = "FE FE FE FE"
    data_version = "01 00 00 00 "
    def __init__(self,version="10",frame_type="20"):
        """
        初始化帧结构中固定的部分
        :param version: 协议版本
        :param data_version:
        :param frame_type: 帧类型
        :param frame_head: 帧头
        :param rame_hail: 帧尾
        """
        self.vesion = version
        self.frame_type = frame_type

    def sub_type(self,**kwargs):
        """
        子类型
        :param sub_type:子类型名称
        :return:
        """
        type = ''
        return type

    def time_str(self,**kwargs):
        """
        时间hex
        :return:
        """
        time = ''
        return time

    def frame_content_lenth(self,**kwargs):
        """
        帧内容长度
        :return:
        """
        content = ''
        return content

    def content(self,**kwargs):
        """
        帧内容
        :param args:
        :return:
        """
        content = ''
        return content


    def pkg(self,type,timestr,content_length,content,crc):
        pkg = self.frame_head+self.vesion+self.data_version+self.frame_type+type+timestr+\
              content_length+content+crc+self.frame_tail
        return pkg



