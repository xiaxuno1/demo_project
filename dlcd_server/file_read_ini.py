# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: file_read
# Author: xiaxu
# DATA: 2023/2/28
# Description:配置文件的读取操作 .ini文件
# ---------------------------------------------------
import config,configparser

class INIOp:
    '''
    考虑使用单例模式
    '''
    def __init__(self,file_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(file_path,encoding='ansi')
    def sections(self):
        return self.cfg.sections()

    def items(self,section):
        """获取指定section的内容 ，以（key,value）形式"""
        return self.cfg.items(section)

    def options(self):
        """获取keys"""
        return self.cfg.options()

    def get(self,section,option):
        """获取指定项"""
        return self.cfg.get(section,option)

    def get_section_content(self,section,split_method=','):
        """使用生成器生成，避免内容过多占用过多空间"""
        section_keys = self.cfg.options(section)
        for key in section_keys:
            item = self.cfg.get(section,key)
            yield item.split(split_method)


if __name__ == '__main__':
    ini = INIOp("DlcdjcSet1.ini")
    print(ini.cfg.sections()) #list
    #print(ini.cfg.items("模拟量配置"))
    print(ini.cfg.options('模拟量配置'))
    print(ini.cfg.get('模拟量配置','1'))
    for i in ini.get_section_content('模拟量配置'):
        print(i)



