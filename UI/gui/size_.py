# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: size_
# Author: xiaxu
# DATA: 2023/9/26
# Description:调整大小
# ---------------------------------------------------
from tkinter import *

app = Tk()

app.title('接口仿真工具')

sw = app.winfo_screenwidth()
# 得到屏幕宽度
sh = app.winfo_screenheight()

# 得到屏幕高度
ww = 610
wh = 400

x = (sw - ww) / 2
y = (sh - wh) / 2
app.geometry("%dx%d+%d+%d" % (ww, wh, x, y))


app.resizable(width=False, height=False)
app.mainloop()
