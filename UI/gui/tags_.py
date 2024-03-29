# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: tags_
# Author: xiaxu
# DATA: 2023/9/26
# Description:通过tags精确控制文本显示
# ---------------------------------------------------
from tkinter import *
import webbrowser

root= Tk();root.geometry("300x300+400+400")
w1= Text(root,width=40,height=20) #宽度 20 个字母(10 个汉字)，高度一个行高
w1.pack()
w1.insert(INSERT,"good goodstudy,day day up!\nhebut\n关关雎鸠\n百度一下")
w1.tag_add("good",1.0,1.9)
w1.tag_config("good",background="yellow",foreground="red")
w1.tag_add("baidu",4.0,4.4)
w1.tag_config("baidu",underline=True)
def webshow(event):
    webbrowser.open("http://www.baidu.com")
    w1.tag_bind("baidu","<Button-1>",webshow)
root.mainloop()
