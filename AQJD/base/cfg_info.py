# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: cfg_info
# Author: xiaxu
# DATA: 2023/9/21
# Description:读取配置，组装为元组
# ---------------------------------------------------
from AQJD.base.file_read_ini import INIOp


class CFGInfo(INIOp):
    def get_total(self,section_name):
        return eval(self.get_get(section_name,'总数'))

    def get_info(self,section_name):
        total = self.get_total(section_name)
        infos = []
        items = self.get_items(section_name)
        infos.append(items[0]) #总数信息
        for i in range(1,total+1): #根据总数设置路数
            contents = items[i][1].split(',') #按照逗号分离出每部分内容
            #去除空白
            info = [items[i][0]]
            for j in contents:
                info.append(j.strip())
            infos.append(info)
        return infos

if __name__ == '__main__':
    cfg = CFGInfo()
    print(cfg.get_info('报警开关量'))