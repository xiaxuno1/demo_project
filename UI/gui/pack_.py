# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: pack_
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
# 测试 pack 布局管理
from tkinter import *

root = Tk()
root.geometry("700x220")
# Frame 是一个矩形区域，就是用来防止其他子组件
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
btnText = ("流行风", "中国风", "日本风", "重金属", "轻音乐")
for txt in btnText:
    Button(f1, text=txt).pack(side="left", padx="10")
for i in range(1, 20):
    Button(f2, width=5, height=10, bg="black" if i % 2 == 0 else "white").pack(side="left")
root.mainloop()
