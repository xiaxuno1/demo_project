# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: scale_
# Author: xiaxu
# DATA: 2023/9/27
# Description:拖动滑块
# ---------------------------------------------------
#optionmenu 的使用测试
from tkinter import *

root= Tk()
root.geometry("400x150")
def t1(value):
    print("滑块的值:",value)
    newFont= ("宋体",value)
    a.config(font=newFont)

s1=Scale(root,from_=10,to=50,length=200,orient=HORIZONTAL,command=t1)
s1.pack()
a= Label(root,text="关关雎鸠",width=10,height=1,bg="black",fg="white")
a.pack()
root.mainloop()
