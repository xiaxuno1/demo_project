# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: option_menu
# Author: xiaxu
# DATA: 2023/9/27
# Description:下拉框
# ---------------------------------------------------
#optionmenu 的使用测试
from tkinter import *

root= Tk()
root.geometry("200x100")
v= StringVar(root)
v.set("关关雎鸠")
om= OptionMenu(root,v,"关关雎鸠","在河之洲","窈窕淑女","君子好逑")
om["width"]=10
om.pack(pady=20)
def t1():
    print("最喜爱的诗句:",v.get())
    #v.set("关关雎鸠")	#直接修改了optionmenu中选中的值
Button(root,text="确定",command=t1).pack()
root.mainloop()
