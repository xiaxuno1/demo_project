# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: demeo2
# Author: xiaxu
# DATA: 2023/2/27
# Description:数据转换
# ---------------------------------------------------
import base64

# data = 'hello ..你好'
# data1 = '68656C6C6F202E2EE4BDA0E5A5BD'
# data2 = b'68656C6C6F202E2EE4BDA0E5A5BD'
# print(data.encode()) #b'hello ..\xe4\xbd\xa0\xe5\xa5\xbd' 字符串编码
# print(base64.b16encode(data.encode())) #b'68656C6C6F202E2EE4BDA0E5A5BD' 字节码编为16进制的字节码
# print(base64.b16encode(data.encode()).decode()) #68656C6C6F202E2EE4BDA0E5A5BD 字节码编码
# print(base64.b16decode(data2))
# print(base64.b16decode(data1)) #字节码或类字节码，解码 Base16 编码的类似字节的对象或 ASCII 字符串。


def lchk_sum():
    """
    定义length中校验码计算
    校验码的计算：D11D10D9D8+D7D6D5D4+D3D2D1D0，求和后模16的余数取反加1。
    :return:
    """
    d = '000000010010'
    d_sum = int(d[0:4],2) + int(d[4:8],2) + int(d[8::],2)
    lchksum =(~d_sum % 16) +1 #注意这里的括号，因为+-的优先级要高于^ &的优先级
    return lchksum
if __name__ == '__main__':
    print(lchk_sum())
    data = 'hello ..你好'
    data1 = b'68656C6C6F202E2EE4BDA0E5A5BD'
    data2 = b'hello ..\xe4\xbd\xa0\xe5\xa5\xbd'
    data3 = '01234567abcd' #ascii码
    print(base64.b16decode(data1)) #解码 Base16 编码的类似字节的对象或 ASCII 字符串。b'hello ..\xe4\xbd\xa0\xe5\xa5\xbd'
    print(base64.b16encode(data2)) #编码类字节流对象返回字节流b'68656C6C6F202E2EE4BDA0E5A5BD'
    print(data.encode(encoding='utf8'))#b'hello ..\xe4\xbd\xa0\xe5\xa5\xbd'
    print(data3.encode())    #b'01234567abcd'
    print(base64.b16encode(data3.encode())) #将字节流编码为16进制形式
    print(bytes.fromhex('7e')+data1)
    print("-"*50)
    data4 = 1057
    data5 = 64478
    x = data4%0xff
    y = ~x
    z =y+1
    print(x,y,z)



