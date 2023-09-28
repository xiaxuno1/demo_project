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
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(project_path()+'\\cfg_data\\BjlxSet1.ini',encoding='ansi')

    def get_sections(self):
        return self.cfg.sections()

    def get_items(self,section):
        return self.cfg.items(section)

    def get_options(self):
        return self.cfg.options()

    def get_get(self,section,option):
        return self.cfg.get(section,option)


if __name__ == '__main__':
    ini = INIOp()
    print(ini.cfg.sections()) #list
    print(ini.cfg.items('报警开关量')) #list 所有的内容[('option', 'item'),...]
    print(ini.cfg.options('报警开关量'))#['路数', '1',  所有参数
    print(ini.get_get("报警开关量","总数")) #


