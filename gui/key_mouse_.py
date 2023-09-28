# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: key_mouse_
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
#测试键盘和鼠标事件
from tkinter import	*

root = Tk()
root.geometry("530x300")
c1 = Canvas(root,width=200,height=200,bg="green")
c1.pack()
def mouseTest(event):
    print("鼠标左键单击位置(相对于父容器)：{0},{1}".format(event.x,event.y))
    print("鼠标左键单击位置(相对于屏幕)：{0},{1}".format(event.x_root,event.y_root))
    print("事件绑定的组件：{0}".format(event.widget))

def dragTest(event):
    c1.create_oval(event.x,event.y,event.x+1,event.y+1)

def keyboardTest(event):
    print("键的 keycode:{0},键的 char:{1},键的 keysym:{2}".format(event.keycode,event.char,event.keysym))

def press_a_test(event):
    print("press a")

def release_a_test(event):
    print("release a")

c1.bind("<Button-1>",mouseTest)
c1.bind("<B1-Motion>",dragTest)
root.bind("<KeyPress>",keyboardTest)
root.bind("<KeyPress-a>",press_a_test)	#只针对小写的a，大写的 A 不管用
root.bind("<KeyRelease-a>",release_a_test)
root.mainloop()
