# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: input_dialog
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
#简单对话框
from tkinter.simpledialog import *

root= Tk();root.geometry("400x100")
show= Label(root,width=40,height=3,bg="green")
show.pack()
a=askinteger(title="输入年龄",prompt="请输入年龄 ",initialvalue=18,minvalue=1,maxvalue=150) #简单对话框
show["text"]="年龄："+str(a) #设置label标签的属性
#askfloat,askstring 自行测试
root.mainloop()
