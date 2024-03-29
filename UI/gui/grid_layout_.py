# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: grid_layout
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
import sys
if sys.version_info.major == 3:
    import tkinter as tk
elif sys.version_info.major == 2:
    import Tkinter as tk
root = tk.Tk()
root.title(u"grid布局演示")
for row in range(3):
    for col in range(4):
        text_ = "row=%d, col=%d" % (row, col)
        tk.Button(root, text=text_).grid(row=row, column=col)
root.mainloop()
