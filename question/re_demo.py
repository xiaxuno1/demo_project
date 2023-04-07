# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: re_demo
# Author: xiaxu
# DATA: 2023/3/24
# Description:正则的几个函数
# ---------------------------------------------------
import re


parttern = '一行.*'
words = '两个黄鹂鸣翠柳，一行白鹭上青天'
re_par = re.compile(parttern)
print(re_par.match(words))  #仅在位置0匹配None
print(re_par.search(words))
print(re_par.findall(words))