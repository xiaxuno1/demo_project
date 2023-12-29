# --------------------------------------------------
#coding=gbk
# !/usr/bin/python
# PN: interface_test
# FN: yaml_read
# Author: xiaxu
# DATA: 2022/10/9
# Description:对yaml文件的读取
# ---------------------------------------------------
import yaml


def yaml_load(path):
    """读取yaml文件，返回list，返回字典组成的列表，"""
    stream = open(path,"r",encoding='gbk')
    yaml_data = yaml.load(stream,Loader=yaml.FullLoader)
    return yaml_data

if __name__ == '__main__':
    user_data = yaml_load('..//data//cfg.yaml')
    print(type(user_data[0]['rebuild_all']))
    print(user_data[0]['rebuild_all'])