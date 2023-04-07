# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: setDefine
# Author: xiaxu
# DATA: 2023/2/23
# Description:定义set.ini文件的格式;后续怎样指定每个变量的大小，将字节流和解析没有私利
# ---------------------------------------------------
import struct
from PZFileDecode.setFileDecode import *


class Set:
    def __init__(self):  #定义变量在struct中的类型
        self.version = '30c' #版本
        self.release_time = '30c' #发布时间
        self.sys_version = '30c' #版本号

        self.ip1 = '20c'
        self.port1 = '100i'
        self.code1 = '4c' #服务器的电报码

        self.local_code = '4c' #本地电报码
        self.name_cn = '100c'
        self.code_id = 'H' #WORD类型 2B的无符号整型

        self.num = 'i' #数量，姐入服务器的数量

class ZDSet(Set):
    def __init__(self):
        super(ZDSet,self).__init__()  #继承
        self.ip1 = '2000s' #重写ip的长度
    def zd_set_struct(self):
        #Only the first character in the format string can be > to use big-endian:在开头定义模式
        strct_partt = '<'+self.num+self.ip1+self.port1 +self.code1+self.local_code+\
                      self.name_cn+self.code_id+self.version+self.release_time+self.sys_version

        return strct_partt

    def set_decode(self,data):
        print(self.zd_set_struct())
        s = struct.Struct(self.zd_set_struct())
        return s.unpack(data)

    def set_content(self,data):
        """将解析后的结构体解码为能看懂的数据"""
        #先实现ip的解码

def char_array_to_list(data,length):
    """将字符串数组解码转换为列表"""
    array_list= []
    if len(data)%length != 0:
        print('输入的字符串数组长度不能整除规定长度')
        return False
    with open('test.txt', 'w', encoding='ansi') as fp:
        for i in range(0,len(data),length):
            a = data[i:i+length].decode('ansi')
            fp.write(a+'\n')
            array_list.append(a)
    return array_list

if __name__ == '__main__':
    zdset = ZDSet()
    file_name = 'set.pz'
    bin_code = file_read(file_name)
    data =xor(bin_code)
    print(len(data))
    zd_content = zdset.set_decode(data)
    print(zd_content)
    char_list = char_array_to_list(zd_content[1],20)







