# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: recursion_sum
# Author: xiaxu
# DATA: 2023/3/24
# Description:递归球1-100的和
# ---------------------------------------------------

def rec_sum(i):
    if i==1: #定义递归结束条件
        return i
    else:
        return rec_sum(i-1)+i

if __name__ == '__main__':
    print(rec_sum(100))