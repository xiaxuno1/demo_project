# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: I LOVE CHINA
# Author: xiaxu
# DATA: 2023/3/24
# Description:输入i lover China 输出 china love i
# ---------------------------------------------------

def spilt_reverse(words:str):
    word_revers = ''
    for  i in  words.split(' '):
        word_revers = i+' '+word_revers
    return word_revers.strip()

if __name__ == '__main__':
    words = 'I LOVE CHINA'
    print(spilt_reverse(words))