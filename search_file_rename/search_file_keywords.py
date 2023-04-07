# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: search_file_keywords
# Author: xiaxu
# DATA: 2023/4/7
# Description:搜索文件中是否包含关键字
# ---------------------------------------------------
"""
读取文件
搜索文件是否含有关键字（多个）
返回含有关键字的行
"""
import configparser
import os
import re
from collections import Iterable
import cchardet

"""
经常报错，弃用
def file_read_(filename):
    cfg = configparser.RawConfigParser(allow_no_value=True)
    cfg.read(filename)
    #print(cfg.sections()) #获取所有的section
    #print(dir(cfg)) #获取所有方法
    #print(cfg.options(cfg.sections()[0])) #获取=左边的选项
    return (cfg.items(i) for i in cfg.sections()) #返回一个生成器节约内存
    #print( list(i for i in cfg.keys())) #生成所有的key
"""
def file_read(filename,encod):
    with open(filename,'r',encoding=encod) as fp:
        line = fp.readline()
        while line:
            line =fp.readline()
            yield line

def get_file_encoding(filepath):
    """获取文件的编码方式"""
    with open(filepath, 'rb') as f:
        encoding = cchardet.detect(f.read())['encoding']
        if encoding in ["ISO-8859-1", "ASCII"]:
            return "GB2312"
        if encoding == "EUC-TW":
            return "GBK"
        return encoding

def find_file_by_type(path,file_type):
    """
    读取指定文件目录下的指定文件
    :return:
    """
    real_path = []  # 返回目标文件的绝对路径
    for root, dir, files in os.walk(path):
        partern = '{0}$'.format(file_type)
        for file in files:
            if re.search(partern,file):
                real_path.append(root+'\\'+file)
    return real_path

def flatten(str_item, ignore_types=(str, bytes)):
    """
    解除嵌套
    :param str_item:
    :param find_str:
    :return:
    """
    for i in str_item:
        #判断是否为可迭代对象
        if isinstance(i,Iterable) and not isinstance(i, ignore_types):
            #ignore为了防止出现字符串或者整数，永远递归无退出
            yield from flatten(i)
        else:
            yield i

if __name__ == '__main__':
    path =r'E:\配置文件过程库\10型以前车站\XLX_滁宁城际铁路\配置文件制作\JSX'
    file_type = 'ini'
    key_words = ['技术学院站','滁阳路南站']
    files = find_file_by_type(path, file_type)
    #全体文件目录
    for file in files:
        print(file)
        encod = get_file_encoding(file)
        #print(encod)
        for content in file_read(file,encod):
            if content is None:
                continue
            for key_word in key_words:
                if key_word in content:
                    print(content)