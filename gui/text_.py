# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: test_
# Author: xiaxu
# DATA: 2023/9/26
# Description:
# ---------------------------------------------------
# 测试 Text 多行文本框组件的基本用法，使用面向对象的方式
from tkinter import *
import webbrowser


class Application(Frame):
    def __init__(self, master=None):  # super()代表的是父类的定义，而不是父类对象
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.w1 = Text(root, width=40, height=12, bg="gray")
        # 宽度 20 个字母(10 个汉字)，高度一个行高
        self.w1.pack()
        self.w1.insert(1.0, "0123456789\nabcdefg")
        self.w1.insert(2.3, "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦\n")

        Button(self, text="重复插入文本", command=self.insertText).pack(side="left")
        Button(self, text="返回文本", command=self.returnText).pack(side="left")
        Button(self, text="添加图片", command=self.addImage).pack(side="left")
        Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        Button(self, text="通过 tag 精确控制文本", command=self.testTag).pack(side="left")

    def insertText(self):
        # INSERT 索引表示在光标处插入
        self.w1.insert(INSERT, '关关雎鸠')

        # END 索引号表示在最后插入
        self.w1.insert(END, '[hebut]')
        self.w1.insert(1.8, "关关雎鸠")

    def returnText(self):
        # Indexes(索引)是用来指向 Text 组件中文本的位置，Text 的组件索引也是对应实际字符之间的位置。
        # 核心：行号以 1 开始 列号以 0 开始
        print(self.w1.get(1.2, 1.6))
        print("所有文本内容：\n" + self.w1.get(1.0, END))

    def addImage(self):
        # global photo
        self.photo = PhotoImage(file="puke1.gif")
        self.w1.image_create(END, image=self.photo)

    def addWidget(self):
        b1 = Button(self.w1, text='爱学习')
        # 在text 创建组件的命令
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        self.w1.delete(1.0, END) #删除文本框的所有内容
        self.w1.insert(INSERT, "good good study,day day up!\nhebut\n关关雎鸠\n百度一下") #插入
        self.w1.tag_add("good", 1.0, 1.9)  #添加TagName,起点和终点之间
        self.w1.tag_config("good", background="yellow", foreground="red") #配置TagName的背景等信息
        self.w1.tag_add("baidu", 4.0, 4.4)
        self.w1.tag_config("baidu", underline=True) #下划线
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow) #标签

    def webshow(self, event):
        webbrowser.open("http://www.baidu.com")


if __name__ == '__main__':
    root = Tk()
    root.geometry("450x300+200+300")
    app = Application(master=root)
    root.mainloop()
