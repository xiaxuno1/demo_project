# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: tempfile
# Author: xiaxu
# DATA: 2023/3/24
# Description:临时文件
# ---------------------------------------------------
import tempfile


with tempfile.TemporaryFile(mode = 'w+',encoding='utf8') as fp:
    fp.write('两个黄鹂鸣翠柳，一行白鹭上青天')
    fp.seek(0)  #准备读取
    print(fp.read())
