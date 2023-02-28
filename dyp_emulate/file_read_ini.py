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
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read('DypSet1.ini',encoding='ansi')
    def sections(self):
        return self.cfg.sections()

    def items(self,section):
        return self.cfg.items(section)

    def options(self):
        return self.cfg.options()

    def get(self,section,option):
        return self.cfg.get(section,option)


if __name__ == '__main__':
    ini = INIOp()
    print(ini.cfg.sections()) #list
    #print(ini.cfg.items('发送系统输入模拟量数据')) #list 所有的内容[('路数', '36'),...]
    print(ini.cfg.options('发送系统输入模拟量数据'))#['路数', '1',  所有参数
    print(ini.cfg.get('发送系统输入模拟量数据', '路数')) #


