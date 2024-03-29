# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: pack_joker
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):	# super()代表的是父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):

        # 通过 place 布局管理器实现扑克牌位置控制
        #self.photo = PhotoImage(file="imgs/puke/puke1.gif")
        #self.puke1 = Label(self.master,image=self.photo)
        #self.puke1.place(x=10,y=50)
        self.photos =[PhotoImage(file="imgs/puke"+str(i+1)+".gif") for i in range(10)]
        self.pukes =[Label(self.master,image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10+i*40,y=50)
            #为所有的 Label 增加事件处理
            self.pukes[0].bind_class("Label","<Button-1>",self.chupai)

    def chupai(self,event):
        print(event.widget.winfo_geometry())
        print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x370+200+300")
    app = Application(master=root)
    root.mainloop()
