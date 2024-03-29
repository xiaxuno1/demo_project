# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: label_
# Author: xiaxu
# DATA: 2023/9/26
# Description:标签
# ---------------------------------------------------
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建组件
        self.label01 = Label(self, text='关关雎鸠', width=10, height=2,
                             bg='black', fg='white')
        self.label01.pack()
        self.label02 = Label(self, text='hebut', width=10, height=2,
                             bg='blue', fg='white', font=('黑体', 30))
        self.label02.pack()
        # 显示图像
        global photo
        # photo = PhotoImage(file='puke1.gif')
        # self.label03 = Label(self, image=photo)
        # self.label03.pack()
        # 显示多行文本
        self.label04 = Label(self, text='hebut\n关关雎鸠', borderwidth=1, relief='groove', justify='right')
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('400x500+200+300')
    app = Application(master=root)
    root.mainloop()
