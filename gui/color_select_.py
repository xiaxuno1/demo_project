# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: color_select_
# Author: xiaxu
# DATA: 2023/9/27
# Description:颜色选择框
# ---------------------------------------------------
# askcolor 颜色选择框的测试，改变背景色
from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry("400x150")


def t1():
    s1 = askcolor(color="red", title="选择背景色") #颜色选框的默认选项为red,标题为 选择背景色
    # ((0.0,0.0,255.99609375),'#0000ff')
    root.config(bg=s1[1]) #重新配置背景色


Button(root, text="选择背景色", command=t1).pack()
root.mainloop()
