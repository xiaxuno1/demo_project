# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: create_data_file
# Author: xiaxu
# DATA: 2023/4/3
# Description:生成文件
# ---------------------------------------------------
with open('user.txt','w+') as fp:
    for i in range(1,900):
        fp.write('sq{0:03},123456\n'.format(i))