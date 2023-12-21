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
from BjlxBS.base.function import project_path

class INIOp:
    '''
    考虑使用单例模式
    '''
    def __init__(self,path):
        self.cfg = configparser.ConfigParser()
        #config = configparser.RawConfigParser()
        # confierParser默认会见键转化为小写，此句忽略转化
        self.cfg.optionxform = lambda option: option
        #project_path()+'\\cfg_data\\BjlxSet1.ini',encoding='ansi' 改用相对路径解决exe报错
        self.path = path
        self.cfg.read(self.path)

    def get_sections(self):
        return self.cfg.sections()

    def get_items(self,section):
        return self.cfg.items(section)

    def get_options(self):
        return self.cfg.options()

    def get_get(self,section,option):
        return self.cfg.get(section,option)

    #设置section内的键值对
    def set(self,section,option,value):
        return self.cfg.set(section,option,value)

    def write(self):
        with open(self.path,'w') as wcfg:
            self.cfg.write(wcfg)


if __name__ == '__main__':
    ini = INIOp()
    print(ini.cfg.sections()) #list
    print(ini.cfg.items('报警开关量')) #list 所有的内容[('option', 'item'),...]
    print(ini.cfg.options('报警开关量'))#['路数', '1',  所有参数
    print(ini.get_get("报警开关量","总数")) #


