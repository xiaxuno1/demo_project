# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: setDefine
# Author: xiaxu
# DATA: 2023/2/23
# Description:定义set.ini文件的格式;后续怎样指定每个变量的大小，将字节流和解析没有私利
# ---------------------------------------------------

class Set:
    def __init__(self):  #定义变量在struct中的类型
        self.version = '30s' #版本
        self.release_time = '30s' #发布时间
        self.sys_version = '30s' #版本号
        self.port = '>i'


class ZDSet(Set):
    def __init__(self):
        super(ZDSet,self).__init__()  #继承
        self.version = '2000s'
        self.name = '4s' #名字

if __name__ == '__main__':
    zdset = ZDSet()
    print(zdset.version)






