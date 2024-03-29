# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: bind_
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
#多种事件绑定方式汇总
from tkinter import *

root = Tk()
root.geometry("270x30")
def mouseTest1(event):
    print("bind()方式绑定，可以获取 event 对象")
    print(event.widget)

def mouseTest2(a, b):
    print("a={0},b={1}".format(a, b))
    print("command 方式绑定，不能直接获取 event 对象")

def mouseTest3(event):
    print("右键单击事件，绑定给所有按钮啦！！")
    print(event.widget)

b1 = Button(root, text="测试 bind()绑定")
b1.pack(side="left")
#bind 方式绑定事件
b1.bind("<Button-1>", mouseTest1)
#command 属性直接绑定事件
b2 = Button(root, text="测试 command2",command=lambda: mouseTest2("关关雎鸠", "hebut"))
b2.pack(side="left")
# 给所有 Button 按钮都绑定右键单击事件<Button-2>
b1.bind_class("Button", "<Button-2>", mouseTest3)
