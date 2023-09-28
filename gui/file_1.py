# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: file_1
# Author: xiaxu
# DATA: 2023/9/27
# Description:文件操作
# ---------------------------------------------------
from tkinter import *
from tkinter.filedialog import *

root= Tk();root.geometry("400x100")
def t1():
    f= askopenfilename(title="上传文件",initialdir="f:/code",filetypes=[("文本文件",".txt")])
    #print(f)
    show["text"]=f
Button(root,text="选择编辑的文本文件",command=t1).pack()
show= Label(root,width=40,height=3,bg="green")
show.pack()
root.mainloop()
