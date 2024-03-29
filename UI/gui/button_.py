# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: button_
# Author: xiaxu
# DATA: 2023/9/26
# Description:
# ---------------------------------------------------
#测试Button组件的基本用法，使用面向对象的方式
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):  # super()代表的是父类的
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.btn01 = Button(root, text="登录", width=6, height=3, anchor=CENTER, command=self.login)
        self.btn01.pack()

        global photo
        # photo = PhotoImage(file="puke1.gif")
        # self.btn02 = Button(root,image=photo,command=self.login)
        # self.btn02.pack()
        # self.btn02.config(state="disabled")	#设置按钮为禁用

    def login(self):
        messagebox.showinfo("学习系统", "登录成功！欢迎开始学习！")


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x400+200+300")
    app = Application(master=root)
    root.mainloop()

