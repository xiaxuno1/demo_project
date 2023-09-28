# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: ttk_
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
#记事本软件,练习主菜单的设计
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

root= Tk();root.geometry("400x400")
#创建主菜单栏
menubar= Menu(root)
#创建子菜单
menuFile= Menu(menubar)
menuEdit= Menu(menubar)
menuHelp= Menu(menubar)
#将子菜单加入到主菜单栏
menubar.add_cascade(label="文件(F)",menu=menuFile)
menubar.add_cascade(label="编辑(E)",menu=menuEdit)
menubar.add_cascade(label="帮助(H)",menu=menuHelp)

filename= ""
def openFile():
    global filename
    with askopenfile(title="打开文件") as f:
        content =f.read()
        w1.insert(INSERT,content)
        filename =f.name
        print(f.name)

def saveFile():
    with open(filename,"w") as f:
        content =w1.get(1.0,END)
        f.write(content)

def exit():
    root.quit()

#添加菜单项
menuFile.add_command(label="打开",accelerator="^O",command=openFile)
menuFile.add_command(label="保存",command=saveFile)
menuFile.add_separator() #添加分割线
menuFile.add_command(label="退出",command=exit)

#将主菜单栏加到根窗口
root["menu"] =menubar
w1= Text(root,width=50,height=30)
w1.pack()
root.mainloop()
