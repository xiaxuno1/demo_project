# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: frame_
# Author: xiaxu
# DATA: 2023/9/28
# Description:
# ---------------------------------------------------
import customtkinter


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.progressbar = customtkinter.CTkProgressBar(self.my_frame, orientation="horizontal")
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.progressbar.grid(row=0, column=1, padx=0, pady=20, sticky="nsew")



app = App()
app.mainloop()