# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: app
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
from tkinter import *
import customtkinter
from tkinter import messagebox
from BjlxBS.equipment_status import Status

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("接口仿真")


    def set_kgl(self):
        print("应该获取开关量信息")
        infos = Status().cfg.get_info('继电器开关量')
        for i in range(1, len(infos)):
            list_data = (infos[i][0],infos[i][1],infos[i][-1])
            self.lb1.insert(i,list_data)


if __name__ == '__main__':
    app = App()
    app.mainloop()