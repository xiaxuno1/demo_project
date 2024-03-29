# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: pack_layout_
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
root.title(u"pack布局演示")
tk.Button(root, text="side:top").pack(side='top')
tk.Button(root, text="side:bottom").pack(side='bottom')
tk.Button(root, text="side:left").pack(side='left')
tk.Button(root, text="side:right").pack(side='right')
root.mainloop()
