# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: app
# Author: xiaxu
# DATA: 2023/9/27
# Description:UI
# ---------------------------------------------------
import os
from tkinter import StringVar
import tkinter
import customtkinter
from BjlxBS.base.cfg_info import CFGInfo

#设置系统显示主题和显示模式
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    #带有lable名称和button的滚动条框架
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []

    def add_item(self, label_text,button_text, image=None):
        # compound 图像位置（上下左右）， anchor 文字位置 padx 在文本x方形增加额外空间（左，右）
        label = customtkinter.CTkLabel(self, text=label_text, image=image, compound="left", padx=5, anchor="w")
        #button
        button = customtkinter.CTkButton(self, text=button_text, width=100, height=24)
        if self.command is not None:
            button.configure(command=lambda: self.command(label_text))
        #sticky 如果cell更大，将粘贴在那里（方向） "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("test_doemo") #标题
        self.geometry(f"{1100}x{580}") #尺寸

        # configure grid layout (4x4)
        # grid整体的布局，weight权重 决定了多大如1/2
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        #ctk_Frame 一个单独的结构,一个块
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew") #rowspan 这个部件将跨多少行，占多少行
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        #ctk_label 标签，展示功能，
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="名称", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        #ctk_button，点击触发事件
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        #CTkOptionMenu 可选菜单（下拉选择） 下拉值 触发事件
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.set("100%")
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #信息显示框 ctk_tabveiw
        self.info_frame = customtkinter.CTkScrollableFrame(self)
        self.info_frame.grid(row = 0,column=1,padx=(20, 20), pady=(20, 0), sticky="nsew")
        #段按钮组件 CTkSegmentedButton
        cfg = CFGInfo("..\\cfg_data\\BjlxSet1.ini").get_info("继电器开关量")
        print(cfg)
        for i in range(1,len(cfg)):
            label = customtkinter.CTkLabel(self.info_frame,text=str(i))
            label2 = customtkinter.CTkLabel(self.info_frame,text=cfg[i][1])
            label3 = customtkinter.CTkLabel(self.info_frame,text=cfg[i][3])
            button = customtkinter.CTkButton(self.info_frame,text =cfg[i][5],command=self.sidebar_button_event )
            label.grid(row = i+1,column = 0,padx=(20, 20), pady=(10, 0), sticky="nsew")
            label2.grid(row = i+1,column = 1,padx=(20, 20), pady=(10, 0), sticky="nsew")
            label3.grid(row = i+1,column = 2,padx=(20, 20), pady=(10, 0), sticky="nsew")
            button.grid(row = i+1,column = 3,padx=(20, 20), pady=(10, 0), sticky="nsew")


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    #设置显示模式 黑夜、白天
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    #设置 显示缩放
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    #定义button事件
    def sidebar_button_event(self):
        print("sidebar_button click")
    #定义输入事件
    def input_event(self):
        print("输入内容：",self.entry.get())  #get获取当前输入的内容



if __name__ == '__main__':
    app = App()
    app.mainloop()
