# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: quit_menu_
# Author: xiaxu
# DATA: 2023/9/27
# Description:快捷菜单
# ---------------------------------------------------
from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *

root= Tk();root.geometry("400x400")

def openAskColor():
    s1= askcolor(color="red", title="选择背景色")
    #((0.0,0.0,255.99609375),'#0000ff')
    root.config(bg=s1[1])

#创建快捷菜单
menubar2= Menu(root)
menubar2.add_command(label="颜色",command=openAskColor)
menuedit= Menu(menubar2,tearoff=0)
menuedit.add_command(label="剪切")
menuedit.add_command(label="复制")
menuedit.add_command(label="粘贴")
menubar2.add_cascade(label="编辑",menu=menuedit)

def t(event):
    #菜单在鼠标右键单击的坐标处显示
    menubar2.post(event.x_root,event.y_root)
#编辑区
w1= Text(root,width=50,height=30)
w1.pack()
w1.bind("<Button-3>",t)
root.mainloop()
