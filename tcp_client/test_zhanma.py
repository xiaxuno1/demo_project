# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: interface_test
# FN: test_zhanma
# Author: xiaxu
# DATA: 2022/12/9
# Description:测试站码
# ---------------------------------------------------
upalpha_str = [chr(i) for i in range(65,91)] #大写A-z
lowalpha_str = [chr(i) for i in range(ord('a'),ord('z')+1)]
number_str = [chr(i) for i in range(ord('1'),ord('9')+1)]
station_frist_alpha = [chr(i) for i in range(65,78)]  #车站首字母A-M
terminal_frist_alpha =[chr(i) for i in range(78,91)] #终端首字母N-Z
other_alpha = upalpha_str+lowalpha_str+number_str
print(other_alpha)
with open('./zhanmabiao.txt','w') as fp:
    for i in terminal_frist_alpha:
        n = 0
        for j in other_alpha:
            for k in other_alpha:
                station_code = i+j+k+'\n'
                n = n+1
                if n<=100: #根据设置的客户端个数设置，目前定位一个工具最多设置200个客户端
                    fp.write(station_code)
                else:
                    break